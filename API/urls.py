from django.urls import path

from API.views import PositionView, PositionDetailView, ConsultantView, ConsultantDetailView

urlpatterns = [
    path('position', PositionView.as_view()),
    path('position/<int:pk>', PositionDetailView.as_view()),

    path('consultant', ConsultantView.as_view()),
    path('consultant/<int:pk>', ConsultantDetailView.as_view())
]
