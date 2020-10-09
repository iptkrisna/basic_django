from django.shortcuts import render
from . import models


def template_views(request):
    student = models.Student.objects.all()
    major = models.Major.objects.all()

    if request.method == 'POST':
        if request.POST['major'] is not '*':
            student = models.Student.objects.filter(major=request.POST['major'])

    context = {
        'student': student,
        'major': major
    }
    return render(request, 'template.html', context)
