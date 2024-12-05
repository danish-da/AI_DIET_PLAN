from django.conf.urls import url
from user import views

urlpatterns=[
    url('register/',views.adduser),
    url('view_user/',views.viewuser)

]