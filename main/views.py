from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .models import PortfolioWork, Category, ContactInfo, BlogPost, Testimonial, SkillTag
from .serializer import UserSerializer, CustomTokenObtainPairSerializer
from .serializer import PortfolioWorkSerializer, CategorySerializer, ContactInfoSerializer, BlogPostSerializer, \
    TestimonialSerializer, SkillTagSerializer


@api_view(['GET', 'POST'])
def get_users(request):
    if request.method == 'GET':
        # if not User(request.user).is_admin:
        #    return Response({"error": "Not Authed"}, status=status.HTTP_401_UNAUTHORIZED)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        new_user = request.data

        password = new_user['password']
        try:
            validate_password(password)
        except ValidationError as e:
            return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)
        new_user['password'] = make_password(password)

        serializer = UserSerializer(data=new_user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        update_user = request.data

        password = update_user['password']
        try:
            validate_password(password)
        except ValidationError as e:
            return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)
        update_user['password'] = make_password(password)

        serializer = UserSerializer(user, data=update_user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@api_view(['GET', 'POST'])
def portfolio_work_list_create(request):
    if request.method == 'GET':
        portfolio_works = PortfolioWork.objects.all()
        serializer = PortfolioWorkSerializer(portfolio_works, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PortfolioWorkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def portfolio_work_detail(request, pk):
    portfolio_work = get_object_or_404(PortfolioWork, pk=pk)

    if request.method == 'GET':
        serializer = PortfolioWorkSerializer(portfolio_work)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PortfolioWorkSerializer(portfolio_work, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        portfolio_work.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def category_list_create(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def contact_info_list_create(request):
    if request.method == 'GET':
        contact_infos = ContactInfo.objects.all()
        serializer = ContactInfoSerializer(contact_infos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def contact_info_detail(request, pk):
    contact_info = get_object_or_404(ContactInfo, pk=pk)

    if request.method == 'GET':
        serializer = ContactInfoSerializer(contact_info)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactInfoSerializer(contact_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contact_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def blog_post_list_create(request):
    if request.method == 'GET':
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def blog_post_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)

    if request.method == 'GET':
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BlogPostSerializer(blog_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        blog_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def testimonial_list_create(request):
    if request.method == 'GET':
        testimonials = Testimonial.objects.all()
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TestimonialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def testimonial_detail(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)

    if request.method == 'GET':
        serializer = TestimonialSerializer(testimonial)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TestimonialSerializer(testimonial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        testimonial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def skill_tag_list_create(request):
    if request.method == 'GET':
        skill_tags = SkillTag.objects.all()
        serializer = SkillTagSerializer(skill_tags, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SkillTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def skill_tag_detail(request, pk):
    skill_tag = get_object_or_404(SkillTag, pk=pk)

    if request.method == 'GET':
        serializer = SkillTagSerializer(skill_tag)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SkillTagSerializer(skill_tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        skill_tag.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
