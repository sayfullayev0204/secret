from django.db import models

class Bolimlar(models.Model):
    Bolim = models.CharField(max_length=500)

    def __str__(self):
        return self.Bolim

class Fan(models.Model):
    Bolim = models.ForeignKey(Bolimlar, on_delete=models.CASCADE)
    Fan_nomi = models.CharField(max_length=200)
    Rasm = models.ImageField(upload_to='img')
    Ustoz = models.CharField(max_length=500)
    Ustoz_rasmi = models.ImageField(upload_to='ustoz')
    Malumot = models.TextField()

    def __str__(self):
        return self.Fan_nomi
class Vazifa(models.Model):
    Fan = models.ForeignKey(Fan, on_delete=models.CASCADE)
    nomi = models.TextField()
    video = models.FileField(upload_to='video')

    def __str__(self):
        return self.nomi

class Question(models.Model):
    nomi = models.ForeignKey(Vazifa, on_delete=models.CASCADE)
    text = models.TextField()
    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
