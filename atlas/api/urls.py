from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path("api/users", views.UserList.as_view()),
    path("api/answers", views.AnswerList.as_view()),
    path("api/surveys", views.SurveyList.as_view()),
    path("api/submit", views.AnswerSurvey.as_view(), name="submit"),
    path("api/token", obtain_auth_token, name="get_token"),
    path("api/register", views.RegisterUser.as_view(), name="register"),
    path("api/journals", views.JournalStubList.as_view(), name="stubs"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
