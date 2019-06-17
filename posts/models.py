import uuid

from django.db import models
from django.db.models.signals import pre_save

from posts.utils import unique_slug_generator


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True, allow_unicode=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey('posts.Category', blank=True, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('users.User', related_name='post_creator', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.slug

    class Meta:
        indexes = [
            models.Index(fields=['slug', ]),
        ]


def post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(post_pre_save_receiver, sender=Post)


class Category(models.Model):
    LEVELS = (
        (1, 'Level One'),
        (2, "Level Two"),
    )
    name = models.CharField(max_length=120)
    category_code = models.CharField(max_length=64)
    level = models.IntegerField(choices=LEVELS)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='sub_category', on_delete=models.SET_NULL)
    description = models.TextField(max_length=300, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['parent', ]),
        ]
