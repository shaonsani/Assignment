from rest_framework.generics import ListCreateAPIView
from app.models import GlucoseReading
from app.serializers import GlucoseReadingBaseSerializer


class GlucoseReadingListCreateAPIView(ListCreateAPIView):
    permission_classes = ()
    serializer_class = GlucoseReadingBaseSerializer
    queryset = GlucoseReading.objects.all()