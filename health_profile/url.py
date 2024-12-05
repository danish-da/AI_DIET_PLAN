from django.conf.urls import url
from health_profile import views

urlpatterns=[
    url('add_health_profile/',views.addhealth),
    url('manage_health/',views.viewhealth),
    url('edit_health/(?P<idd>\w+)', views.edithealth)
]