from django.shortcuts import render
from donate_blood.models import DonateBlood
# Create your views here.
def adddonate(request):
    # ss= request.session["uid"]
    if request.method == 'POST':

        obj = DonateBlood()
        obj.user_id = 1
        obj.name = request.POST.get('uname')
        obj.blood_group = request.POST.get('bloodgroup')
        obj.health_condition = request.POST.get('health')
        obj.phn = request.POST.get('phone')
        obj.save()
    return render(request,'donate_blood/donate_blood.html')


def viewdonate(request):
    obj = DonateBlood.objects.all()
    context = {
        'a': obj
    }
    return render(request,'donate_blood/view_blooddonours.html', context)
def adddonatepublic(request):
    ss= request.session["uid"]
    if request.method=='POST':
        obj = DonateBlood()
        obj.user_id = ss
        obj.name = request.POST.get('uname')
        obj.blood_group = request.POST.get('bloodgroup')
        obj.health_condition = request.POST.get('health')
        obj.phn = request.POST.get('phone')
        obj.save()

    return render(request,'donate_blood/donate_blood_public.html')
def viewdonatepublic(request):
    obj = DonateBlood.objects.all()
    context = {
        'a': obj
    }
    return render(request,'donate_blood/view_donours_public.html',context)
