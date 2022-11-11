from django.urls import path

from API.views import PositionView, PositionDetailView, EmployeeView, EmployeeDetailView

urlpatterns = [
    path('position', PositionView.as_view()),
    path('position/<int:pk>', PositionDetailView.as_view()),

    path('employee', EmployeeView.as_view()),
    path('employee/<int:pk>', EmployeeDetailView.as_view())
]
