from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
import time
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.decorators import api_view

# Create your views here.


def home(request):
    for i in range(1, 10):
        channel_layer = get_channel_layer()
        data = {'count': i}

        async_to_sync(channel_layer.group_send)(
            'test_consumer_group', {
                'type': 'send_notifications',
                'data': json.dumps(data)
            }
        )
        time.sleep(1)
    return render(request, 'index.html')


@api_view(['POST'])
def postdata(request):

    title = request.data['title']
    body = request.data['body']

    if title and body :
        test_data = TestData.objects.create(title=title, body=body)
        return Response({'message':'Data created'})
    else:
        return Response({'message':'Field missing'})

