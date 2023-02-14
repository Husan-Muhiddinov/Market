from django.test import TestCase
from django.urls import reverse,get_user
from .models import CustomUser

# Create your tests here.


class SignupTestCase(TestCase):
    def test_signup_view(self):
        response=self.client.post(
            reverse('users:signup'),
            data={
                "first_name":"Husan",
                "username":'husan',
                'email':'aa@aa.aa',
                'password1':'aaaa7777',
                'password2':'aaaa7777',
            }
        )
        user=CustomUser.objects.get(username='husan')
        self.assertEqual(user.first_name, 'Husan')
        self.assertEqual(user.email, 'aa@aa.aa')
        self.assertTrue(user.check_password('aaaa7777'))

        second_response=self.client.get("/users/profile/husan")
        self.assertEqual(second_response.status_code, 200)

        # login

        self.client.login(username='husan',password='aaaa7777')

        third_response=self.client.post(
            reverse('users:update'),
            data={
                'username':'husan2',
                'first_name':'Husan2',
                'last_name':'Muhiddinov',
                'email':'aa@aa.aa',
                'phone_number':'+998912323',
                'tg_username':'username',

            }

        )


        user=get_user(self.client)
        print(user.is_authenticated)

        self.assertEqual(user.phone_number,'+998912323')
        self.assertEqual(third_response.status_code, 302)   # post metodim to'g'ri ishlasa 302 bo'lib qaytadi