from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudySessions(models.Model):
    
    Subject_Choices = [
        ("Python", "Python"),
        ("Django", "Django"),
        ("REST API", "REST API"),
        ("MySQL", "MySQL"),
        ("MongoDB", "MongoDB"),
        ("JavaScript", "JavaScript"),
        ("NumPy", "NumPy"),
        ("Pandas", "Pandas"),
        ("Matplotlib", "Matplotlib"),
        ("React", "React"),
        ("HTML", "HTML"),
        ("CSS", "CSS"),
        ("Bootstrap", "Bootstrap"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.CharField(max_length=20, choices=Subject_Choices)
    planned_topic = models.CharField(max_length=200)
    covered_topic = models.CharField(max_length=200, blank=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.subject} - {self.date}"
    