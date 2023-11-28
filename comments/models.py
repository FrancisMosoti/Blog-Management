from django.db import models


# Create your models here.
class Comments(models.Model):
    comment = models.CharField(max_length=255, blank=False, null=False)
    comment_user = models.CharField(max_length=255, blank=False, null=False)
    post_id = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
