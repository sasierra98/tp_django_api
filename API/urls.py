from django.urls import path

from API.views import PositionView, PositionDetailView, ParticipantView, ParticipantDetailView

urlpatterns = [
    path('position', PositionView.as_view()),
    path('position/<int:pk>', PositionDetailView.as_view()),

    path('participant', ParticipantView.as_view()),
    path('participant/<int:pk>', ParticipantDetailView.as_view())
]
