from django.db import models



class Thread(models.Model):
    participants = models.ManyToManyField('accounts.CustomUser')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField()

class Maessage(models.Model):
    text = models.TextField()
    sender = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
