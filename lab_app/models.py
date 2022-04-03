from tabnanny import verbose
from django.db import models
from datetime import datetime
class lab_task_summary(models.Model):
    name = models.CharField(max_length=25,blank =False)
    age =models.IntegerField()
    research_type = models.CharField(max_length=50)
    equipments = models.CharField(max_length=255)
    findings = models.TextField()
    email = models.EmailField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f'{self.name}--{self.research_type}'
    class Meta:
        verbose_name_plural = "Laboratory Tasks"