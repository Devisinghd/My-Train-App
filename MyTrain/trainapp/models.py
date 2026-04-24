from django.db import models

# Create your models here.
class Train(models.Model):

    def __str__(self):
        return f"{self.Train_name} ({self.train_code})"
    
    Train_name = models.CharField(max_length=50)
    train_code = models.IntegerField(blank=True)
    total_capacity = models.IntegerField()


class Station(models.Model):


    station_name = models.CharField(max_length=50)
    station_code = models.IntegerField()


class Schedule(models.Model):


    train = models.ForeignKey(Train,on_delete=models.CASCADE)
    source = models.ForeignKey(Station,related_name='departure',on_delete=models.CASCADE)
    destination = models.ForeignKey(Station,related_name='arrival',on_delete=models.CASCADE)
    departure = models.DateTimeField()
    available_seat = models.IntegerField()

