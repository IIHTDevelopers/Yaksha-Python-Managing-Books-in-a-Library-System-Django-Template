from rest_framework.test import APITestCase
from django.urls import reverse
from library.models import Book
from library.test.TestUtils import TestUtils

class BookFunctionalTest(APITestCase):

    def test_fetch_books_successfully(self):
        """Test if the book list API returns all books successfully"""
        test_obj = TestUtils()
        try:
            Book.objects.create(title="Django for Beginners", author="William S. Vincent", published_date="2020-01-15", isbn="1234567890123", available_copies=5)
            Book.objects.create(title="Python Crash Course", author="Eric Matthes", published_date="2019-06-10", isbn="9876543210987", available_copies=10)

            response = self.client.get(reverse("book-list"))
            if response.status_code == 200 and len(response.json()) == 2:
                test_obj.yakshaAssert("TestFetchBooksSuccessfully", True, "functional")
                print("TestFetchBooksSuccessfully = Passed")
            else:
                test_obj.yakshaAssert("TestFetchBooksSuccessfully", False, "functional")
                print("TestFetchBooksSuccessfully = Failed")
        except:
            test_obj.yakshaAssert("TestFetchBooksSuccessfully", False, "functional")
            print("TestFetchBooksSuccessfully = Failed")

    def test_fetch_books_empty(self):
        """Test if the API returns a 404 message when no books are available"""
        test_obj = TestUtils()
        try:
            response = self.client.get(reverse("book-list"))
            if response.status_code == 404 and "No books found" in response.json().get("message", ""):
                test_obj.yakshaAssert("TestFetchBooksEmpty", True, "functional")
                print("TestFetchBooksEmpty = Passed")
            else:
                test_obj.yakshaAssert("TestFetchBooksEmpty", False, "functional")
                print("TestFetchBooksEmpty = Failed")
        except:
            test_obj.yakshaAssert("TestFetchBooksEmpty", False, "functional")
            print("TestFetchBooksEmpty = Failed")
