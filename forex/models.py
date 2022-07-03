from locale import currency
from urllib import request
from django.db import models


class ReportStatus(models.Model):
    request_id = models.CharField(max_length=200)
    status = models.IntegerField()
    comment = models.TextField(max_length=200)
    user_id = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.request_id


class ReportHistoryPrediction(models.Model):
    request_id = models.CharField(max_length=200)
    currency = models.CharField(max_length=20)
    interval = models.CharField(max_length=200)
    prediction_high = models.FloatField()
    prediction_low = models.FloatField()
    target_datetime = models.DateTimeField()
    predicted_hit_high = models.DateTimeField(null=True)
    predicted_hit_low = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.request_id