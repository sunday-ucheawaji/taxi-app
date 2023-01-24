from django.contrib.auth import get_user_model
from trips.models import Trip
from rest_framework import generics, viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, LoginSerializer, TripSerializer


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LogInView(TokenObtainPairView):
    serializer_class = LoginSerializer


class TripView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class TripView(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'id'  # new
    lookup_url_kwarg = 'trip_id'  # new
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
