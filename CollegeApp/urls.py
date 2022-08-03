from . import views
from django.urls import path

urlpatterns = [
     path('',views.index,name='index'),
     path('signup/',views.signup,name='signup'),
     path('login/',views.login,name='login'),
     path('course1/',views.course1,name='course1'),
     path('student1/',views.student1,name='student1'),

     path('user_create/',views.user_create,name='user_create'),
     path('user_logout/',views.user_logout,name="user_logout"),
     path('add_course/',views.add_course,name='add_course'),
     path('user_login/',views.user_login,name='user_login'),
     path('user_logout/',views.user_logout,name='user_logout'),
     path('add_student/',views.add_student,name='add_student'),
     path('show_details/',views.show_details,name="show_details"),
     path('show_teachers/',views.show_teachers,name='show_teachers'),
     path('profile/',views.profile,name='profile'),
     path('edit_profile/',views.edit_profile,name='edit_profile'),
     path('edit_page',views.edit_page,name='edit_page'),

     path('admin_home/',views.admin_home,name='admin_home'),

     path('user_home/',views.user_home,name='user_home'),
]