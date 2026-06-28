import unittest
from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):

    def test_parent_1(self):
        node = ParentNode("p", [LeafNode("b", "ligma balls"), LeafNode(None, "this is some text")],)
        result = '<p><b>ligma balls</b>this is some text</p>'
        self.assertEqual(node.to_html(), result)

    def test_parent_2(self):
        leaf1 = LeafNode("b", "Header")
        leaf2 = LeafNode(None, "text here")
        leaf3 = LeafNode("a", "click here", {"href": "https://google.com"})
        parent = ParentNode("p", [leaf1, leaf2, leaf3])
        self.assertEqual(parent.to_html(), '<p><b>Header</b>text here<a href="https://google.com">click here</a></p>')


    def test_parent_3(self):
        leaf1 = LeafNode("b", "Header")
        parent = ParentNode("p", [leaf1])
        grandparent = ParentNode("div", [parent], {"align": "center"})
        self.assertEqual(grandparent.to_html(), '<div align="center"><p><b>Header</b></p></div>')

    def test_parent_4(self):
        leaf = LeafNode("b", "help")
        parent = ParentNode("a", [leaf], {"href":"https://google.com"})
        grandparent = ParentNode("p", [parent])
        self.assertEqual(grandparent.to_html(), '<p><a href="https://google.com"><b>help</b></a></p>')

if __name__ == "__main__":
    unittest.main()