from django.db import models


class Preview(models.Model):
    image = models.ImageField(upload_to='images/')
    image_url = models.CharField(max_length=350)

    def __str__(self):
        return self.image_url


class PriceItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    preview = models.ForeignKey(Preview, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " - " + str(self.price)
