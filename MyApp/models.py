from django.db import models

# Create your models here
class Bacteria(models.Model):
    properties = models.CharField(max_length=300)
    type = models.CharField(max_length=300)
    size = models.IntegerField()

class Fungi(models.Model):
    properties = models.CharField(max_length=300)
    type = models.CharField(max_length=200)
    size = models.IntegerField()

class Microorganisms(models.Model):
    bacteria = models.ForeignKey(Bacteria, on_delete=models.CASCADE)
    fungi = models.OneToOneField(Fungi, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)



# class Microorganisms(models.Model):
    # properties = models.CharField(max_length=150, default='default_value_here')
    # type = models.CharField(max_length=150)
    # size = models.IntegerField()
# 