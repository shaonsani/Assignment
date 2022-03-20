from django.urls import path
from app.views import GlucoseReadingListCreateAPIView, GlucoseReadingRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("", GlucoseReadingListCreateAPIView.as_view(), name="create_list_api"),
    path("/<uuid:reading_uuid>", GlucoseReadingRetrieveUpdateDestroyAPIView.as_view(), name="update_delete_retrieve_api"),
]