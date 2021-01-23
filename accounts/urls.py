from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerpage, name='register'),
    path('login/',views.loginpage, name='login'),
    path('logout/',views.logoutuser, name='logout'),
    path('',views.landing),
    path('records/',views.record, name='records'),
    path('reports/',views.reports, name='reports'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('reports/delete/<str:delete_id>/', views.delete, name='delete'),
    path('api/linechart/data/',views.LineChartData.as_view()),
    path('api/barchart/data/',views.BarChartData.as_view()),
]