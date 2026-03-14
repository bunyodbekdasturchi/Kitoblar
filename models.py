from django.db import models

class telefon(models.Model):
    nomi=models.CharField(max_length=40)
    model=models.CharField(max_length=50)
    narx=models.DecimalField(max_digits=60, decimal_places=3)

    def __str__(self):
            return self.nomi


class xaridor(models.Model):
    ism=models.CharField(max_length=30)
    famila=models.CharField(max_length=30)
    books=models.ForeignKey(telefon,on_delete=models.CASCADE)

    def __str__(self):
            return self.nomi
