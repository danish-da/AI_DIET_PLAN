from django.db.models import Q
from django.shortcuts import render
from user.models import User
from chat.models import Chat
# Create your views here.


def teacherr(request):
    obj = User.objects.all()
    ob = Chat.objects.all()
    context = {
        'kk': ob,
        'uu': obj,

    }
    # print(ss),
    # print(idd)
    if request.method == 'POST':
        obk = Chat()
        obk.message = request.POST.get('mssg')
        obk.rec_type='admin'
        obk.sender_type='user'
        obk.save()
    return render(request, 'chat/teacher.html',context)


def admii(request):
    obj = User.objects.all()
    ob = Chat.objects.all()
    context = {
        'kk': ob,
        'uu': obj,

    }
    # print(ss),
    # print(idd)
    if request.method == 'POST':
        obk = Chat()
        obk.message = request.POST.get('mssg')
        obk.rec_type='user'
        obk.sender_type='admin'
        obk.save()
    return render(request, 'chat/admin.html',context)
