from django.db import models


class Thread(models.Model):
    participants = models.ManyToManyField('accounts.CustomUser')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    text = models.TextField()
    sender = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
