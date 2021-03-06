from django import forms
from django.contrib import admin
from suit_ckeditor.widgets import CKEditorWidget
from reports.models import CountryReport, Map, Section, MapPoint, Country
from suit.admin import SortableStackedInline


class SectionAdminForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Section
        widgets = {
            'content': CKEditorWidget(),
        }


class SectionAdmin(SortableStackedInline):
    form = SectionAdminForm
    model = Section
    extra = 1


class CountryReportAdmin(admin.ModelAdmin):
    model = CountryReport
    inlines = [SectionAdmin]


class MapPointAdmin(admin.StackedInline):
    model = MapPoint
    extra = 0


class MapAdmin(admin.ModelAdmin):
    model = Map
    inlines = [MapPointAdmin]


class CountryAdmin(admin.ModelAdmin):
    model = Country

admin.site.register(CountryReport, CountryReportAdmin)
admin.site.register(Map, MapAdmin)
admin.site.register(Country, CountryAdmin)
