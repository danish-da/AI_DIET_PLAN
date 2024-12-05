from django.shortcuts import render
from feedback.models import Feedback
import datetime
# Create your views here.
def postfeedback(request):
    ss= request.session["uid"]
    if request.method == 'POST':
        obj=Feedback()
        obj.feedback=request.POST.get('Feedback')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.user_id = ss
        obj.save()
    return render(request,'feedback/feedback.html')
def viewfeedback(request):
    obj = Feedback.objects.all()
    context ={
        'a':obj
    }
    return render(request,'feedback/view_feedback.html',context)
