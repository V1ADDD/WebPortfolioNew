from django.db import models
from django.db.models import JSONField


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PortfolioWork(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.ImageField(upload_to='portfolio_images/', blank=True, null=True)  # For file/image upload
    link_url = models.URLField(blank=True, null=True)  # External link to the project
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)  # Controls visibility on the site

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    social_links = JSONField()  # Stores links in a JSON format
    address = models.CharField(max_length=255, blank=True, null=True)  # Optional

    def __str__(self):
        return self.email


class SkillTag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    tags = models.ManyToManyField(SkillTag, blank=True)  # Tags related to the blog post

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    client_name = models.CharField(max_length=255)
    client_title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.client_name} - {self.client_title}"
