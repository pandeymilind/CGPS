from django.urls import path 
#from . import views
from gatepassapp.views import *


urlpatterns=[
     
    path('',website_view, name='website_view'),
    path('login/',login_view, name='login_view'),  
    path('logout/',logout_view, name='logout_view'),
    path('dashboard/',dashboard, name='dashboard'),
    path('chat/',chat, name = 'chat'),
    path('applicationform/',applicationfrom, name='applicationform'),
    path('approvals/',approvals, name='approvals'),
    path('requestform/',requestform, name='requestform'),
    path('staff/',staff, name='staff'),
    path('hod/',hod, name='hod'),
    path('warden/',warden, name='warden'),
    path('approve_studentstaff/<int:student_id>/',approve_studentstaff, name='approve_studentstaff'),
    path('approve_studenthod/<int:student_id>/',approve_studenthod, name='approve_studenthod'),
    path('approve_studentwarden/<int:student_id>/',approve_studentwarden,name='approve_studentwarden'),
    path('rejection/<int:student_id>/',rejection, name='rejection'),
]