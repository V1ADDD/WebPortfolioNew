from django.urls import path
from .views import (
    get_users, get_user, CustomTokenObtainPairView,
    portfolio_work_list_create, portfolio_work_detail,
    category_list_create, category_detail,
    contact_info_list_create, contact_info_detail,
    blog_post_list_create, blog_post_detail,
    testimonial_list_create, testimonial_detail,
    skill_tag_list_create, skill_tag_detail
)

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/<int:pk>/', get_user, name='get_user'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('portfolio-works/', portfolio_work_list_create, name='portfolio_work_list_create'),
    path('portfolio-works/<int:pk>/', portfolio_work_detail, name='portfolio_work_detail'),
    path('categories/', category_list_create, name='category_list_create'),
    path('categories/<int:pk>/', category_detail, name='category_detail'),
    path('contact-info/', contact_info_list_create, name='contact_info_list_create'),
    path('contact-info/<int:pk>/', contact_info_detail, name='contact_info_detail'),
    path('blog-posts/', blog_post_list_create, name='blog_post_list_create'),
    path('blog-posts/<int:pk>/', blog_post_detail, name='blog_post_detail'),
    path('testimonials/', testimonial_list_create, name='testimonial_list_create'),
    path('testimonials/<int:pk>/', testimonial_detail, name='testimonial_detail'),
    path('skills/', skill_tag_list_create, name='skill_tag_list_create'),
    path('skills/<int:pk>/', skill_tag_detail, name='skill_tag_detail'),
]
