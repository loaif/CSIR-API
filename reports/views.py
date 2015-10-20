from rest_framework import viewsets
from reports.models import Maps, Section, CountryReport
from reports.serializers import MapsSerializer, SectionSerializer, CountryReportSerializer


class CountryReportViewSet(viewsets.ModelViewSet):
    queryset = CountryReport.objects.all()
    serializer_class = CountryReportSerializer

class MapsViewSet(viewsets.ModelViewSet):
    queryset = Maps.objects.all()
    serializer_class = MapsSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
