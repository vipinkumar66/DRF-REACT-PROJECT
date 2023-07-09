from django.db import models
from django.conf import settings
from django.db.models.query import QuerySet
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self) -> QuerySet:
            """
            This is a custom manaager and this is replacement
            of the queryset in the view, there we have to call
            this directly
            """
            return super().get_queryset().filter(status="published")

    options = (
        ("draft", "Draft"),
        ("published", "Published")
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date="published")
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts")
    status = models.CharField(max_length=10, choices=options, default="published")
    content = models.TextField()

    objects = models.Manager() #defult manager
    postobjects = PostObjects() #custom manager

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return self.title

