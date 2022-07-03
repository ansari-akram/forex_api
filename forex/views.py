from operator import mod
from pyexpat import model
from xml.etree.ElementTree import Comment
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import JsonResponse
from .past_prediction import past_predict
from datetime import datetime


@csrf_exempt
def predict(request):
    user_id = request.POST['user_id']
    request_id = request.POST['request_id']
    from_date = request.POST['from_date']
    to_date = request.POST['to_date']
    currency_id = request.POST['currency_id']
    interval = request.POST['interval_list'].strip().split(",")
    model_id = request.POST['model_id']

    from_date = datetime.strptime(from_date, "%d/%m/%Y")
    to_date = datetime.strptime(to_date, "%d/%m/%Y")

    ReportStatus.objects.create(request_id=request_id, status='0', comment='in process', user_id=user_id)

    past_predict(user_id, request_id, from_date, to_date, currency_id, interval, model_id)

    ReportStatus.objects.filter(request_id=request_id).update(status='1', comment='done')

    return JsonResponse({'result': f'{user_id} {request_id} {from_date} {to_date} {currency_id} {interval} {model_id}'})