from django import forms
from django.contrib import admin
from redactor.widgets import RedactorEditor
from reports.models import CountryReport, Map, Section, MapPoint
from suit.admin import SortableStackedInline


class SectionAdminForm(forms.ModelForm):
    class Meta:
        exclude = []
        widgets = {
            'content': RedactorEditor(),
        }


class SectionAdmin(SortableStackedInline):
    form = SectionAdminForm
    model = Section
    extra = 0


class CountryReportAdmin(admin.ModelAdmin):
    model = CountryReport
    inlines = [SectionAdmin]


class MapPointAdmin(admin.StackedInline):
    model = MapPoint
    extra = 0


class MapAdmin(admin.ModelAdmin):
    model = Map
    inlines = [MapPointAdmin]

admin.site.register(CountryReport, CountryReportAdmin)
admin.site.register(Map, MapAdmin)
