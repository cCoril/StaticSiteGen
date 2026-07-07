import unittest
from  delimit import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class TestDelmiiter(unittest.TestCase):

    def test_delmit_1(self):
        text1 = TextNode("this is a ", TextType.TEXT)
        text2 = TextNode("BOLD", TextType.BOLD)
        text3 = TextNode(" test", TextType.TEXT)
        test_list = [text1, text2, text3]
        example = split_nodes_delimiter([TextNode("this is a **BOLD** test", TextType.TEXT)], "**", TextType.BOLD)
        self.assertEqual(example, test_list)

    def test_delimit_2(self):
        text1 = TextNode("this is a ", TextType.TEXT)
        text2 = TextNode("code", TextType.CODE)
        text3 = TextNode(" test", TextType.TEXT)
        test_list = [text1, text2, text3]
        example = split_nodes_delimiter([TextNode("this is a `code` test", TextType.TEXT)], "`", TextType.CODE)
        self.assertEqual(example, test_list)

    def test_delimit_3(self):
        text1 = TextNode("code example", TextType.CODE)
        self.assertEqual(split_nodes_delimiter([text1], "`", TextType.CODE), [text1])

    def test_delimit_4(self):
        img1 = TextNode("click here", TextType.IMAGE, "https://google.com")
        self.assertEqual(split_nodes_delimiter([img1], "!", TextType.IMAGE), [img1])

    def test_image_1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)" 
        image_results = extract_markdown_images(text)
        self.assertEqual(image_results, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
