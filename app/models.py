from django.db import models


class Major(models.Model):
    major_option = (
        ('Software Engineering', 'SE'),
        ('Computer System Engineering', 'CSE'),
        ('Renewable Energy Engineering', 'REE'),
        ('Product Design Engineering', 'PDE'),
        ('Food Business Technology', 'FBT'),
        ('Business Mathematics', 'BM'),
    )
    name = models.CharField(choices=major_option, default=0, max_length=256)
    description = models.TextField(null=True, blank=True, max_length=512)

    def __str__(self):
        return '{}'.format(self.name)


class Student(models.Model):
    name = models.CharField(null=True, blank=True, max_length=256)
    image = models.ImageField(upload_to='image/student')
    nim = models.CharField(null=True, blank=True, max_length=32)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return '{} - {}'.format(self.name, self.nim)
