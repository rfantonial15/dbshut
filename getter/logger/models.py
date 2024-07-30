from django.db import models

class KeyLog(models.Model):
    keys = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keys

class KeyLogRevoke(models.Model):
    keys = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keys

class KeyLogArbiscan(models.Model):
    keys = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keys