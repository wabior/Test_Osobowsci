from django.db import models

# Create your models here.

class Pytanie(models.Model):
    nazwa = models.CharField(max_length=30)
    tresc = models.TextField(blank = True)
    grupa = models.CharField(max_length=1,choices=[('a','A'),('b','B'),('c','C'),('d','D'),])

    def __str__(self):
        return self.nazwa

class Odp2(models.Model):
    odps2 = models.CharField(max_length=1, choices=[('A', 'A'),('B','B'),])
    licznik = models.IntegerField(default=0)

    def __str__(self):
        return self.odps2

class Wybory(models.Model):
    nr_pytania = models.ForeignKey(Pytanie, on_delete=models.CASCADE)
    wybor_odp  = models.ForeignKey(Odp2,     on_delete=models.CASCADE)

