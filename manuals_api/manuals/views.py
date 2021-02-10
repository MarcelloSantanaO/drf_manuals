from rest_framework import viewsets
from .models import Manual, Practices
from .serializers import ManualSerializer, PracticesSerializer


class ManualViewsSet(viewsets.ModelViewSet):
    queryset = Manual.objects.all().order_by('id')
    serializer_class = ManualSerializer


class PracticesViewsSet(viewsets.ModelViewSet):
    queryset = Practices.objects.all().order_by('id')
    serializer_class = PracticesSerializer
