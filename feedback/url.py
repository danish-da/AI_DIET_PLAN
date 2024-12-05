from django.conf.urls import url
from feedback import views

urlpatterns=[
    url('add_feedback/',views.postfeedback),
    url('view_feedback/',views.viewfeedback)
]