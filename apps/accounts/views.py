from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.views import UserDetailsView
from .serializers import CustomUserSerializer, UserSerializer
from .models import Account

from rest_framework.generics import ListAPIView

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:3000/"
    client_class = OAuth2Client

class CustomUserDetailView(UserDetailsView):
    serializer_class = CustomUserSerializer
