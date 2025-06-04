from django.db import models


# Create your models here.
class Task(models.Model):

    task = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.id} {self.task} '
    
class TodoItem(models.Model):
    """
    Model representing a single todo item.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    project = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='tasks')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} {self.title} {self.description}'
    

