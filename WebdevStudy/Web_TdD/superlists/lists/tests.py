from django.shortcuts import render
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest, request, response
from django.template.loader import render_to_string
from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase) :
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = "신규 작업 아이템"

        response = home_page(request)

        self.assertIn("신규 작업 아이템", response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text' : "신규 작업 아이템"},
            request=request
        )
        self.assertEqual(response.content.decode(), expected_html)