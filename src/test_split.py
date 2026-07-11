import unittest
from textnode import TextNode, TextType
from extract import split_nodes_image, split_nodes_link

class Testsplit(unittest.TestCase):
    
    def test_split_link_1(self):
        text = TextNode("This is text with [google](https://google.com) and [facebook](https://facebook.com)", TextType.TEXT)
        result = split_nodes_link([text])
        expected_result = [TextNode("This is text with ", TextType.TEXT), TextNode("google", TextType.LINK, "https://google.com"), TextNode(" and ", TextType.TEXT), TextNode("facebook", TextType.LINK, "https://facebook.com")]
        self.assertEqual(result, expected_result)

    def test_split_link_2(self):
        text = TextNode("Here's another test: [boot.dev](https://boot.dev)  ", TextType.TEXT)
        result = split_nodes_link([text])
        expected_result = [TextNode("Here's another test: ", TextType.TEXT), TextNode("boot.dev", TextType.LINK, "https://boot.dev"), TextNode("  ", TextType.TEXT)]
        self.assertEqual(result, expected_result)

    def test_split_link_3(self):
        text = TextNode("Test 3 [yahoo](https://yahoo.com).", TextType.TEXT)
        text_2 = TextNode("Test 3, the [testening] [google](https://google.com)", TextType.TEXT)
        result = split_nodes_link([text, text_2])
        expected_result = [
            TextNode("Test 3 ", TextType.TEXT),
            TextNode("yahoo", TextType.LINK, "https://yahoo.com"),
            TextNode(".", TextType.TEXT),
            TextNode("Test 3, the [testening] ", TextType.TEXT),
            TextNode("google", TextType.LINK, "https://google.com")
        ]
        self.assertEqual(result, expected_result)

    def test_split_image_1(self):
        text = TextNode("This is an image: ![peter griffin](https://petergriffin.com)", TextType.TEXT)
        result = split_nodes_image([text])
        expected_result = [
            TextNode("This is an image: ", TextType.TEXT),
            TextNode("peter griffin", TextType.IMAGE, "https://petergriffin.com")
        ]
        self.assertEqual(result, expected_result)
    
    def test_split_image_2(self):
        text = TextNode("fart ![pic of a butt](https://fartpoop.com) and poop ![pic of poop](https://doodoo.com) are gross",TextType.TEXT)
        result = split_nodes_image ([text])
        expected_result = [
            TextNode("fart ", TextType.TEXT),
            TextNode("pic of a butt", TextType.IMAGE, "https://fartpoop.com"),
            TextNode(" and poop ", TextType.TEXT),
            TextNode("pic of poop", TextType.IMAGE, "https://doodoo.com"),
            TextNode(" are gross", TextType.TEXT)
        ]
        self.assertEqual(result, expected_result)

    def test_split_image_3(self):
        text = TextNode("image ![image](https://image.com) ", TextType.TEXT)
        result = split_nodes_image([text])
        expected_result = [
            TextNode("image ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://image.com"),
            TextNode(" ", TextType.TEXT)
        ]
        self.assertEqual(result, expected_result)

    

