from django.db import models
from user.models import User


class CurriculumVitae(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cvs')
    name = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='upload/%Y/%m')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
