from django.test import SimpleTestCase,Client
from django.urls import resolve,reverse
from wordcount.views import count,about

class TestUrls(SimpleTestCase):

    def test_count(self):
        url = reverse('count')
        print(resolve(url))
        self.assertEquals(resolve(url).func,count)

    def test_about(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func,about)

    def test_count_get(self):
        client = Client()

        response = client.get(reverse('about'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'about.html')

    
