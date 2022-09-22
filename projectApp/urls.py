from django.urls import path
from projectApp import views

urlpatterns = [
    path('',views.login, name= "login"),
    path('home/',views.home, name = "home"),
    path('disp_index/',views.disp_index, name = "disp_index"),
    path('sel_index/<int:id>',views.select_index, name = "sel_index"),
    path('upd_index/<int:id>',views.update_index, name = "upd_index"),
    path('del_index/<int:id>',views.delete_index, name = "del_index"),
    path('register/',views.register, name = "register"),
    path('index/',views.index, name = "index"),
    path('error/',views.error, name = "error"),
    path('logout_student/',views.logout_student, name = "logout_student"),
    path('emp_insert/',views.emp_insert, name = "emp_insert"),
    path('emp_disp/',views.emp_disp, name = "emp_disp"),
    path('emp_select/<int:id>',views.emp_select, name = "emp_select"),
    path('emp_update/',views.emp_update, name = "emp_update"),
]
