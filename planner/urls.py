from django.urls import path
from . import views

urlpatterns = [
    path("", views.routine),
    path("complete/<int:session_id>/", views.toggle_complete),
    path("export/", views.export_excel, name="export_excel"),
    # path("api/study_sessions/", views.StudySessionList.as_view()),
]
