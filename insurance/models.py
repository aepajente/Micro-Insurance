from django.db import models


class Branch(models.Model):
	name = models.TextField(max_length=50)