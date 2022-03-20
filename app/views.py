from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from app.models import GlucoseReading
from app.serializers import GlucoseReadingBaseSerializer, GlucoseReadingUpdateSerializer


class GlucoseReadingListCreateAPIView(ListCreateAPIView):
    permission_classes = ()
    serializer_class = GlucoseReadingBaseSerializer
    queryset = GlucoseReading.objects.all()


class GlucoseReadingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    serializer_class = GlucoseReadingUpdateSerializer
    lookup_field = "reading_uuid"
    queryset = GlucoseReading.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        