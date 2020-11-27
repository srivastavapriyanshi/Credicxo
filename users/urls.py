from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from users.serializers import *

app_name = 'users'
router = DefaultRouter()
router.register("teacher",views.TeacherViewset, "teacher_view"),
router.register("admin",views.AdminViewset, "admin_view"),


urlpatterns = [
    path('register/',views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('student/<int:id>/',views.StudentAPIView.as_view()),
    path("", include(router.urls)),

]