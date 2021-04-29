from django.urls import path
from jobs.api.views import JobDetailsView, JobListView

urlpatterns = [
    path("jobs/", JobListView.as_view(), name='job-list'),
    path("jobs/<int:pk>", JobDetailsView.as_view(), name='job-detail'),
]
