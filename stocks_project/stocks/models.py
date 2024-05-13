from django.db import models

class Uzivatel(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    narozeni = models.DateField()

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Akcie(models.Model):
    nazev = models.CharField(max_length=100)
    tickerSymbol = models.CharField(max_length=10)
    oSpolecnosti = models.TextField(max_length=10000)

    def __str__(self):
        return self.nazev

class Portfolio(models.Model):
    uzivatel = models.ManyToManyField(Uzivatel)
    akcie = models.ManyToManyField(Akcie)

    def __str__(self):
        return f'{self.uzivatel} {self.akcie}'