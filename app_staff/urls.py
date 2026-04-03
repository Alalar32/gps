from django.urls import path
from app_staff import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='staff_dashboard'),
    path('class_schedule/', views.class_schedule_view, name='class_schedule'),
    path('attendance/', views.attendance_view, name='attendance'),
    path('reports/', views.reports_view, name='reports'),
    path('enroll_student/', views.enroll_student, name='enroll_student'),
    path("delete-student/<student_id>/", views.delete_student, name="delete_student"),
    path("editstudent/<student_id>/", views.edit_student, name='edit_student'),
]