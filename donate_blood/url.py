from django.conf.urls import url
from donate_blood import views

urlpatterns=[
    url('register/',views.adddonate),
    url('view/',views.viewdonate),
    url('register_public',views.adddonatepublic),
    url('view_public',views.viewdonatepublic)
]