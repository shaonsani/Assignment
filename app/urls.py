from django.urls import path
from app.views import GlucoseReadingListCreateAPIView

urlpatterns = [
    path("", GlucoseReadingListCreateAPIView.as_view(), name="create_list_api"),
]