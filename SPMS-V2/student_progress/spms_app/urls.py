from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teacher-register/', views.teacher_register, name='teacher_register'),
    path('teacher-login/', views.teacher_login, name='teacher_login'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('manage-students/', views.manage_students, name='manage_students'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('add-attendance/', views.add_attendance, name='add_attendance'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('attendance/<slug:date>/', views.view_attendance_date, name='view_attendance_date'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('delete-subject/<int:id>/', views.delete_subject, name='delete_subject'),
    path('enter-marks/<int:subject_id>/', views.enter_marks, name='enter_marks'),
    path('student-login/', views.student_login, name='student_login'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher-logout/', views.teacher_logout, name='teacher_logout'),
    path('student-logout/', views.student_logout, name='student_logout'),
    path('edit-subject/<int:subject_id>/', views.edit_subject, name='edit_subject'),
    path('edit-attendance/<str:date>/', views.edit_attendance, name='edit_attendance'),
    path('delete-attendance/<str:date>/', views.delete_attendance, name='delete_attendance'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('download-attendance-excel/', views.download_attendance_excel,
     name='download_attendance_excel'),
    path('download-marksheet-pdf/', views.download_marksheet_pdf,
     name='download_marksheet_pdf'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('resend-otp/', views.resend_otp, name='resend_otp'),


]
