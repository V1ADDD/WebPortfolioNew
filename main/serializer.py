from django.contrib.auth.hashers import check_password
from rest_framework import serializers, exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User
from .models import PortfolioWork, Category, ContactInfo, BlogPost, Testimonial, SkillTag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):

        user = User.objects.get(email=attrs.get('email'))
        if user:
            data = {}
            if not check_password(attrs.get('password'), user.password):
                raise exceptions.AuthenticationFailed('Incorrect password')
            refresh = self.get_token(user)
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)
            return data
        else:
            raise exceptions.AuthenticationFailed('No account found with the given credentials')


# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PortfolioWorkSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = PortfolioWork
        fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class SkillTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillTag
        fields = '__all__'
