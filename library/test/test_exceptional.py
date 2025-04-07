
from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.models import Book
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver

class BookExceptionalTest(APITestCase):
    
    @patch("library.models.Book.objects.all")  # Mock the database query
    def test_fetch_books_database_error(self, mock_all):
        """Test if database errors are handled properly"""
        test_obj = TestUtils()
        try:
            mock_all.side_effect = Exception("Database Connection Error")  # Force an error
            response = self.client.get(reverse("book-list"))

            if response.status_code == 500 and "Something went wrong" in response.json().get("error", ""):
                test_obj.yakshaAssert("TestDatabaseErrorHandling", True, "exceptional")
                print("TestDatabaseErrorHandling = Passed")
            else:
                test_obj.yakshaAssert("TestDatabaseErrorHandling", False, "exceptional")
                print("TestDatabaseErrorHandling = Failed")

        except Exception as e:
            test_obj.yakshaAssert("TestDatabaseErrorHandling", False, "exceptional")
            print("TestDatabaseErrorHandling = Failed")
            
