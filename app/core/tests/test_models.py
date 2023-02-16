"""
Test for models
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from core.models import User


class ModelTest(TestCase):
    """Test Models"""

    def test_create_user_with_email_successful(self):
        """올바른 데이터에 대해서 정상작동"""
        email = "user1@example.com"
        password = "password"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)  # 이메일이 같아야함
        self.assertTrue(user.check_password(password))  # 비밀번호가 같아야함

    def test_new_user_without_email_raise_error(self):
        """올바르지 않은 데이터에 대해서 에러 발생"""
        email = ""
        password = "password"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email, password)

    def test_create_superuser(self):
        """올바른 데이터에 대해서 관리자 계정 생성"""
        email = "admin@admin.com"
        password = "testpassword"
        name = "admin"

        user = get_user_model().objects.create_superuser(email, password, name=name)

        self.assertEqual(user.email, email)
        self.assertEqual(user.name, name)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
