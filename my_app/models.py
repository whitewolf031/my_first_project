from django.db import models

# Ma'lumotlar basasi uchun table
class Person(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    about = models.CharField(max_length=255)
    admin_or_not = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ismi: {self.first_name}, familyasi: {self.last_name}"
