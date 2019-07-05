from django.test import TestCase
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .views import *

# Create your tests here.

class MyFirstTest(TestCase):
	
	request = HttpRequest()

	def setUp(self):
		self.request.path = 'app/'

	def test_empty(self):
		self.assertEqual(
			index(self.request).content,
			HttpResponse("Hello, world. You're at the app index.").content
		)



