from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import userserializer
from .models import customuser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
from django.contrib.auth.hashers import check_password
import re
import random


def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)]+ [str(i) for i in range(10)]) for _ in range(length))

@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Please send a post request with valid parameters'})

    username = request.POST['email']
    password = request.POST['password']

#   validating the username and the password field

    if not re.match(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
        return JsonResponse({'error': "Not a valid email address"})
    
    if len(password)<3:
        return JsonResponse({'error': 'Password too short'})

    usermodel = get_user_model()

    try:
        user = usermodel.objects.get(email=username)

        if user.check_password(password):
            user_dict = usermodel.objects.filter(email=username).values().first()
            user_dict.pop('password')

            if user.session_token !="0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error': "previous session exists"})
            
            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token': token, 'user': user_dict})

        else:
            return JsonResponse({'error': "invalid password"})

    except usermodel.DoesNotExist:
        return JsonResponse({'error': "invalid email"})


def signout(request,id):
    logout(request)

    usermodel = get_user_model()

    try:
        user = usermodel.objects.get(pk=id)
        user.session_token="0"
        user.save()
    except usermodel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user ID'})

    return JsonResponse({'success': 'Logout successful'})


class userviewset(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}
    queryset = customuser.objects.all().order_by('id')
    serializer_class = userserializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]