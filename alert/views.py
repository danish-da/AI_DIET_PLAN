from django.shortcuts import render
from alert.models import Alert
import datetime
# Create your views here.
def postalert(request):
    if request.method == 'POST':
        obj = Alert()
        obj.alert = request.POST.get('alert')
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.now()
        obj.save()

    return render(request, 'alert/food_alerts.html')