from unicodedata import name
from  django.urls import path 
from . import views
from requests import request

urlpatterns = [
    path('', views.HomeView.as_view(), name= "home"),
    path('information/<int:pk>/', views.InfoDetailView.as_view(), name = "information"),
    path('cvgen/', views.cvgen, name= "cvgen"),
    path('cvgen/cv1/', views.cv1, name= "cv1"),
    path('cvgen/cv2/', views.cv2, name= "cv2"),
    path('cvgen/cv3/', views.cv3, name= "cv3"),
    path('cvgen/cv4/', views.cv4, name= "cv4"),
    path('cvgen/cv5/', views.cv5, name= "cv5"),
    path('cvgen/formlist/', views.listy, name= "formlist"),
    path('cvgen/formlist/cvgen', views.cvgen, name= "cvgen"),
    path('cvgen/formlist/updet', views.DetView.as_view(), name= "updet"),
    path('cvgen/updet/', views.updet, name= "updet"),
    path('cvgen/formlist/updet2', views.AddView.as_view(), name= "updet2"),
    path('cvgen/formlist/updet3', views.ObjView.as_view(), name= "updet3"),
    path('cvgen/formlist/updet4', views.EduView.as_view(), name= "updet4"),
    path('cvgen/formlist/updet5', views.WorkView.as_view(), name= "updet5"),
    path('cvgen/formlist/updet6', views.SkillView.as_view(), name= "updet6"),
    path('cvgen/formlist/updet7', views.RefView.as_view(), name= "updet7"),
    # path('cvgen/cv1pdf', views.cv_render_pdf_view, name= "cv1pdf"),
    path('cvgen/cv3pdf/', views.cv3_render_pdf_view, name= "cv3pdf"),
    
]