from django.shortcuts import render
from user.models import User
from login.models import Login
# Create your views here.
def adduser(request):
    if request.method == 'POST':
        obj = User()
        obj.name = request.POST.get('name')
        obj.age = request.POST.get('age')

        obj.gender = request.POST.get('gender')
        obj.email = request.POST.get('email')
        obj.address = request.POST.get('address')
        obj.phn_number = request.POST.get('phone')
        obj.password = request.POST.get('pwd')
        obj.save()

        ob=Login()
        ob.username=obj.name
        ob.password=obj.password
        ob.type='user'
        ob.uid=obj.user_id
        ob.save()
    return render(request,'user/user.html')
def viewuser(request):
    obj = User.objects.all()
    context={
        'a':obj
    }
    return render(request,'user/view_user.html',context)