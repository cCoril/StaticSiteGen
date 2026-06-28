import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_unmatch(self):
        node = LeafNode("p", "fart")
        self.assertNotEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_link(self):
        node = LeafNode("a", "Click Here!", {"href": "https://google.com"})
        self.assertEqual(node.to_html(), '<a href="https://google.com">Click Here!</a>')
        
if __name__ == "__main__":
    unittest.main()