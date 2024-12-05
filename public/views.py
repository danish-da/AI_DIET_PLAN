from django.shortcuts import render

from login.models import Login
from public.models import Public
# Create your views here.
def addpublic(request):
    if request.method == 'POST':
        obj = Public()
        obj.pname = request.POST.get('pname')
        obj.age = request.POST.get('age')
        obj.gender = request.POST.get('gender')
        obj.place = request.POST.get('place')
        obj.phone_number = request.POST.get('phone')
        obj.password = request.POST.get('pwd')
        obj.save()

        ob = Login()
        ob.username = obj.pname
        ob.password = obj.password
        ob.type = 'public'
        ob.uid = obj.p_id
        ob.save()
    return render(request,'public/public_reg.html')