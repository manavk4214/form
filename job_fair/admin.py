from .models import form_m
from django.contrib import admin
from django.http import HttpResponse
import csv





def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="form_m_registrations.csv"'

    writer = csv.writer(response)

    # write header with proper column names
    writer.writerow([
        'Email', 'Full Name', 'Gender', 'Father Name', 'Phone Number',
        'Highest Qualification', 'State', 'NIELIT Student',
        'Training Center', 'Course', 'Passing Year',
        'Skills', 'Employed', 'Experience', 'Declaration'
    ])

    # write data rows with proper formatting
    for obj in queryset:
        writer.writerow([
            obj.email,
            obj.fullName,
            obj.gender,
            obj.fatherName,
            obj.phoneNumber,
            obj.highestQualification,
            obj.state,
            obj.nielitStudent,
            obj.trainingCenter,
            obj.course,
            obj.passingYear,
            ", ".join(obj.skills) if obj.skills else '',
            obj.employed,
            obj.experience,
            obj.dec,
        ])

    return response

export_as_csv.short_description = "Download selected as CSV"



@admin.register(form_m)
class FormMAdmin(admin.ModelAdmin):
    actions = [export_as_csv]
    list_display = ['fullName', 'email', 'phoneNumber', 'gender', 'employed']
    search_fields = ['fullName', 'email', 'phoneNumber']
    list_filter = ['gender', 'employed']
