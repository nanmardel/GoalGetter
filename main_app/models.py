from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
  name = models.CharField(max_length=100)
  subject = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} has id of {self.id}'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'course_id': self.id})

TASK=(
  ('E', 'Essay'),
  ('P', 'Project'),
  ('H', 'Homework'),
  ('T', 'Test'),
  ('O', 'Other'),
)

class Assignment(models.Model):
  name = models.CharField('Assignment Name', max_length=100)
  date = models.DateField('Due Date')
  category = models.CharField(
    max_length=1, 
    choices=TASK,
    default=TASK[2][0]
  )
  todo = models.TextField('Goal', max_length=250) 
  course = models.ForeignKey(Course, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} {self.get_category_display()} on {self.date}'
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'pk': self.id})

  class Meta:
    ordering = ['date']
