from django.shortcuts import render,redirect,get_object_or_404
from .models import *
# Create your views here.


def home(request):
    return render(request,'Attendance.html')




def assignteacher(request):
    if request.method == "POST":
        class_id = request.POST.get('class_id')
        teacher_id = request.POST.get('teacher_id')
        
        teacher = get_object_or_404(User, id=teacher_id)
        class_instance = get_object_or_404(Class, id=class_id)
    

        class_instance.teacher = teacher
        class_instance.save()
        return redirect('/')

    return render(request,'assignteacher.html')


# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import College, User

@csrf_exempt
def search_class(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        if query:
            classes = Class.objects.filter(name__icontains=query).values('id', 'name')
            return JsonResponse(list(classes), safe=False)
    return JsonResponse([], safe=False)

@csrf_exempt
def search_teacher(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        if query:
            teachers = User.objects.filter(username__icontains=query).values('id', 'username')
            return JsonResponse(list(teachers), safe=False)
    return JsonResponse([], safe=False)

@csrf_exempt
def add_class(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        college = request.user.collage # Modify as per your logic for assigning a college
        cls = Class.objects.create(name=name, description=description, college=college)
        if not name or not description: 
            return JsonResponse({'success':False,"error":"All fields are required"})
        return JsonResponse({'success': True, 'class': {'id': cls.id, 'name': cls.name}})
    return JsonResponse({'success': False, 'errors': 'Invalid request'})

@csrf_exempt
def add_teacher(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password :
            return JsonResponse({'success': False, 'errors': 'Username, password, and college ID are required.'})

        try:
            college = request.user.collage if request.user.collage else None
            print(request.user.collage)
        except College.DoesNotExist:
            return JsonResponse({'success': False, 'errors': 'Invalid college ID'})

        user = User.objects.create_user(username=username,usertype = "teacher", password=password, collage=college)
        user.save()
        return JsonResponse({'success': True, 'teacher': {'id': user.id, 'username': user.username}})

    return JsonResponse({'success': False, 'errors': 'Invalid request'})
