from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
class Friendship(models.Model):
    request_from = models.ForeignKey(to=User, related_name='request_from', on_delete=models.CASCADE)
    requset_to = models.ForeignKey(to=User, related_name='request_to', on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'friendship'
        verbose_name_plural = 'friendships'
        db_table = 'friendship'
        unique_together = ('request_from', 'requset_to')
        