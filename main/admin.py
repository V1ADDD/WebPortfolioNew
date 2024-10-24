from django.contrib import admin

from main.models import User, PortfolioWork, Category, ContactInfo, BlogPost, Testimonial, SkillTag

# Register your models here.
admin.site.register(User)
admin.site.register(PortfolioWork)
admin.site.register(Category)
admin.site.register(ContactInfo)
admin.site.register(BlogPost)
admin.site.register(Testimonial)
admin.site.register(SkillTag)
