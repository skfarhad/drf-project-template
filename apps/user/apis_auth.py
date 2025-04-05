from drf_spectacular.types import OpenApiTypes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from apps.user.serializers import (
    PasswordLoginSerializer,
    SignupSerializer,
    PasswordChangeOTPSerializer,
    SignupResponseSerializer,
    CommonResponseSerializer,
    PasswordSetSerializer,
    ErrorResponseSerializer
)
from apps.user.serializers import ProfileSerializer

def get_profile_details(user):
    return ProfileSerializer(user).data


class Signup(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(
        summary="User Signup",
        request=SignupSerializer,
        responses={
            200: SignupResponseSerializer,
            400: ErrorResponseSerializer
        }
    )
    def post(self, request, format=None):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user, jwt_token = serializer.signup_user(serializer.validated_data)
            data = {
                'user_details': get_profile_details(user),
                'jwt_token': jwt_token,
            }
            return Response(data, status=200)
        return Response({'detail': str(serializer.errors)}, status=400)


class PasswordLogin(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(
        summary="User Login",
        request=PasswordLoginSerializer,
        responses={
            200: SignupResponseSerializer,
            400: ErrorResponseSerializer
        }
    )

    def post(self, request, format=None):
        serializer = PasswordLoginSerializer(data=request.data)
        if serializer.is_valid():
            user, jwt_token = serializer.authenticate(serializer.validated_data)
            data = {
                'user_details': get_profile_details(user),
                'jwt_token': jwt_token,
            }
            return Response(data, status=200)
        return Response({'detail': str(serializer.errors)}, status=400)


class PasswordChange(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        # print("Request", serializer.data)
        old_password = request.data.get('old_password', False)
        new_password = request.data.get('new_password', False)
        if not (old_password or new_password):
            return Response({'detail': 'Provide old and new password!'}, status=400)

        if len(new_password) < 8:
            return Response({'detail': 'Provide a valid password!'}, status=400)

        user = request.user
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response({'msg': 'OK'}, status=200)
        msg = 'Password do not match'
        return Response({'detail': msg}, status=400)


class PasswordChangeOtp(APIView):
    permission_classes = (AllowAny,)


    @extend_schema(
        summary="Password Change",
        request=PasswordChangeOTPSerializer,
        responses={
            200: CommonResponseSerializer,
            400: ErrorResponseSerializer
        }
    )

    def post(self, request, format=None):
        serializer = PasswordChangeOTPSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.authenticate(serializer.validated_data)
            data = {
                'message': 'OK',
            }
            return Response(data, status=200)
        return Response({'detail': str(serializer.errors)}, status=400)


class PasswordSet(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        summary="Password Set",
        request=PasswordSetSerializer,
        responses={
            200: CommonResponseSerializer,
            400: ErrorResponseSerializer
        }
    )

    def post(self, request, format=None):
        user = request.user
        if user.has_usable_password():
            return Response({'message': 'Use OTP method!'}, status=406)
        password = request.data.get('password', False)
        if not password or len(password) < 8:
            return Response({'message': 'Provide a valid password!'}, status=400)

        user.set_password(password)
        user.save()
        return Response({'message': 'OK'}, status=200)
