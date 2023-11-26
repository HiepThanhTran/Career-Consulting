from django.db import models
from user.models import User


class CurriculumVitae(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cvs')
    image = models.CharField(max_length=254, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
