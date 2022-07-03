from django.contrib import admin
from .models import *


class ReportStatusAdmin(admin.ModelAdmin):
    list_display = ('request_id', 'status', 'comment', 'user_id')

class ReportHistoryPredictionAdmin(admin.ModelAdmin):
    list_display = ('request_id', 'currency', 'interval', 'prediction_high', 'prediction_low', 'target_datetime', 'predicted_hit_high', 'predicted_hit_low')


admin.site.register(ReportStatus, ReportStatusAdmin)
admin.site.register(ReportHistoryPrediction, ReportHistoryPredictionAdmin)