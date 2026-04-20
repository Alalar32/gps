from django.urls import path
from app_staff import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='staff_dashboard'),
    path('manage_teachers/', views.manage_teachers_view, name='manage_teachers'),
    path('editteacher/<int:teacher_id>/', views.edit_teachers_view, name='edit_teachers'),
    path('delete-teacher/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    path('manage_subjects/', views.manage_subjects_view, name='manage_subjects'),
    path('edit_subject/<int:subject_id>/', views.edit_subject_view, name='edit_subject'),
    path('delete-subject/<int:subject_id>/', views.delete_subject, name='delete_subject'),
    path('manage-class/', views.manage_classes_view, name='manage_classes'),
    path('delete-class/<int:class_id>/', views.delete_class, name='delete_class'),
    path('create-report/', views.create_report_view, name='create_report'),
    path('edit-report/<int:report_id>/', views.edit_report, name='edit_report'),
    path('class_schedule/', views.class_schedule_view, name='class_schedule'),
    path('attendance/', views.attendance_view, name='attendance'),
    path('reports/', views.reports_view, name='reports'),
    path('enroll_student/', views.enroll_student, name='enroll_student'),
    path("delete-student/<student_id>/", views.delete_student, name="delete_student"),
    path("editstudent/<student_id>/", views.edit_student, name='edit_student'),
]