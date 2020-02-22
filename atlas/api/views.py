from api.models import Answer, Survey
from api.serializers import (
    UserSerializer,
    AnswerSerializer,
    RegisterUserSerializer,
    AnswerListSerializer,
    SurveyListSerializer,
)
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class AnswerList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = Answer.objects.all()
    serializer_class = AnswerListSerializer


class SurveyList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = Survey.objects.all()
    serializer_class = SurveyListSerializer


class RegisterUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            user = User.objects.create_user(
                username=username,
                email=f"{username}@example.com",
                password=serializer.validated_data["password"],
            )
            user.save()

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerSurvey(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = AnswerSerializer(data=request.data, many=True)
        if serializer.is_valid():
            validated_data = serializer.validated_data

            # Ensure there are no duplicate answers
            question_ordinals = [
                answer["question_ordinal"] for answer in validated_data
            ]
            if len(question_ordinals) != len(set(question_ordinals)):
                return Response(
                    "Multiple answers to same question",
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Each list posted to this endpoint is treaded as a separate survey
            survey = Survey.objects.create(
                user=request.user,
                ordinal=Survey.objects.filter(user=request.user).count() + 1,
            )
            survey.save()

            for validated_answer in validated_data:
                answer = Answer.objects.create(
                    user=request.user,
                    survey=survey,
                    question_ordinal=validated_answer["question_ordinal"],
                    answer=validated_answer["answer"],
                    timestamp=validated_answer["timestamp"],
                )
                answer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
