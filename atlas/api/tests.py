from api.models import Answer, Survey
from api.views import RegisterUser
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate


class RegisterUserTests(APITestCase):
    def test_can_register_user(self):
        url = reverse("register")
        data = {"username": "jebediah", "password": "holy grail"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "jebediah")

    def test_taken_username_rejected(self):
        url = reverse("register")
        data = {"username": "jebediah", "password": "holy grail"}
        data2 = {"username": "jebediah", "password": "holy grail"}
        response = self.client.post(url, data, format="json")
        response2 = self.client.post(url, data2, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)


class SubmitSurveyTests(APITestCase):

    basic_data = [
        {"question_ordinal": 1, "answer": 2, "timestamp": "2020-02-17T18:43:52+0000"},
        {"question_ordinal": 2, "answer": 4, "timestamp": "2020-02-17T18:43:52+0000"},
    ]

    def setUp(self):
        self.token = self.get_auth_token()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)

    def get_auth_token(self):
        data = {"username": "jebediah", "password": "holy grail"}
        response = self.client.post(reverse("register"), data, format="json")
        response2 = self.client.post(reverse("get_token"), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)

        return response2.data["token"]

    def test_can_add_no_answers(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token)
        url = reverse("submit")
        data = []
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Survey.objects.count(), 1)
        self.assertEqual(Answer.objects.count(), 0)

    def test_can_add_single_answer(self):
        url = reverse("submit")
        data = [self.basic_data[0]]
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Survey.objects.count(), 1)
        self.assertEqual(Answer.objects.count(), 1)

    def test_can_add_multiple_answers(self):
        url = reverse("submit")
        data = self.basic_data
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Survey.objects.count(), 1)
        self.assertEqual(Answer.objects.count(), len(data))

    def test_cannot_add_two_answers_to_same_question_in_one_survey(self):
        url = reverse("submit")
        data = self.basic_data
        data[1]["question_ordinal"] = data[0]["question_ordinal"]
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Survey.objects.count(), 0)
        self.assertEqual(Answer.objects.count(), 0)
