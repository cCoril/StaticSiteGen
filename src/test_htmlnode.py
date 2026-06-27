import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):

    def test_prop1(self):
        node1 = node1 = HTMLNode(tag="<a>", props={"href": "https://google.com", "target": "_blank"})
        result =  ' href="https://google.com" target="_blank"'
        self.assertEqual(node1.props_to_html(), result)

    def test_prop2(self):
        node = HTMLNode(tag="<a>", props={"href": "https://boot.dev"})
        result =  ' href="https://google.com" target="_blank"'
        self.assertNotEqual(node.props_to_html(), result)
    
    def test_prop3(self):
        node = HTMLNode(tag="<a>", props={"href": "https://boot.dev"})
        result = ' href="https://boot.dev"'
        self.assertEqual(node.props_to_html(), result)