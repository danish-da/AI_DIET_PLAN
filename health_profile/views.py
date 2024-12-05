from django.shortcuts import render
from health_profile.models import HealthProfile
# Create your views here.
def addhealth(request):
    ss= request.session["uid"]
    if request.method=='POST':
        obj = HealthProfile()
        obj.user_id = ss
        obj.height = request.POST.get('height')
        obj.weight = request.POST.get('weight')
        obj.body_type = request.POST.get('body')
        obj.working_hour = request.POST.get('work')
        obj.save()
    return render(request,'health_profile/heath_profile.html')
def viewhealth(request):
    ss = request.session["uid"]
    obj = HealthProfile.objects.filter(user_id=ss)
    context ={
        'a': obj
    }
    return render(request,'health_profile/manage_healthprofile.html',context)

def edithealth(request, idd):
    ss= request.session["uid"]
    ob = HealthProfile.objects.get(health_id=idd)
    context = {
        'h': ob
    }
    if request.method == 'POST':
        obj = HealthProfile.objects.get(health_id=idd)
        obj.user_id = ss
        obj.height = request.POST.get('height')
        obj.weight = request.POST.get('weight')
        obj.body_type = request.POST.get('body')
        obj.working_hour = request.POST.get('work')
        obj.save()
        return viewhealth(request)
    return render(request, 'health_profile/edit.html', context)

