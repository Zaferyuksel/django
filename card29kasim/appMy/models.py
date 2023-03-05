from django.db import models

# Create your models here.


class Card(models.Model):
    brand = models.CharField(("Marka"), max_length=50, null=True)
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("İçerik"),max_length=500)
    date_now = models.DateTimeField(("Tarih Saat"), auto_now=False, auto_now_add=False)
    image = models.FileField(("Resim"), upload_to=None, max_length=100, null=True)
    price = models.IntegerField(("Fiyat"),null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    card = models.ForeignKey(Card, verbose_name=("Card"), on_delete=models.CASCADE)
    name = models.CharField(("Yorumcu"), max_length=50)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    text = models.TextField(("Yorum"),max_length=500)
    date_now = models.DateTimeField(("Yorum Yapılma Zamanı"), auto_now_add=True)

    def __str__(self):
        return self.card