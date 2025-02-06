from django.db import models

class TimeEntry(models.Model):
    employee_id = models.CharField(max_length=100)
    date = models.DateField()
    hours_spent = models.FloatField()

    def __str__(self):
        return f"{self.employee_id} - {self.date}"
