from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path("users", views.UserList.as_view()),
    path("answers", views.AnswerList.as_view()),
    path("surveys", views.SurveyList.as_view()),
    path("submit", views.AnswerSurvey.as_view(), name="submit"),
    path("token", obtain_auth_token, name="get_token"),
    path("register", views.RegisterUser.as_view(), name="register"),
    path("journals", views.JournalStubList.as_view(), name="stubs"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
