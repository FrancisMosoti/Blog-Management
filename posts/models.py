from django.db import models
from PIL import Image
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    post_user = models.CharField(max_length=255, blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    category = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='static/images/img_posts/')

    created = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        super(Posts, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height < 462 or img.width < 340:
            output_size = (462, 340)
            img.thumbnail(output_size)
            img.save(self.image.path)


def __str__(self):
    return self.name
