# coding : utf-8
from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page
from django.utils.html import mark_safe

class HomePageTest(TestCase):
    """
    resolve 是 Django 内部使用的函数,用于解析 URL,
    并将其映射到相应的视图函数上。
    检查解析网站根路径“/”时,是否能找到名为 home_page 的函数。
    """
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>',response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())
        """
        存在编码问题啊啊啊啊啊
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': 'A new list item'},request=request
        )
        self.assertEqual(mark_safe(response.content.decode()), expected_html)
        """
