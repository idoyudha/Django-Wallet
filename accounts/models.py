from django.db import models

# Create your models here.
class RecordModel(models.Model):
    type            = models.CharField(max_length=40)
    category        = models.CharField(max_length=40)
    sub_category    = models.CharField(max_length=40)
    payment         = models.CharField(max_length=40)
    amount          = models.FloatField()
    date            = models.DateField()
    time            = models.TimeField()

    def __str__(self):
        return "{}. {} - {} - {} - {}".format(self.id, self.type, self.category, self.payment, self.amount)