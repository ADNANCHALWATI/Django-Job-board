
from django.db import models

JOB_TYPE=(
    ('full time','full time'),
    ('part time','part time')
)

# Create your models here.
class Job(models.Model):
    title       =models.CharField(max_length=50,null=True)
    #location=
    job_type    =models.CharField(choices=JOB_TYPE,max_length=15)
    description =models.TextField(max_length=1000,null=True)
    published_at=models.DateTimeField(auto_now=True)
    vacancy     =models.IntegerField(default=1)
    salary      =models.IntegerField(default=0)
    category    =models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    experience  =models.IntegerField(default=0)

    def __str__(self):
        return self.title



class Category(models.Model):
    name=models.CharField(max_length=20)

    
    def __str__(self):
        return self.name

