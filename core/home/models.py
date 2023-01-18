from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
# Create your models here.


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    text = models.CharField(max_length=250, blank=True, null=True)
    is_seen = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        notification_objects = Notification.objects.filter(is_seen=False).count()
        data = {'count': notification_objects, 'current_notification': self.text}

        async_to_sync(channel_layer.group_send)(
            'test_consumer_group', {
                'type': 'send_notifications',
                'data': json.dumps(data)
            }
        )
        super(Notification, self).save(*args, **kwargs)


class TestData(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    body = models.CharField(max_length=250, blank=True, null=True)