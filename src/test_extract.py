import unittest
from  extract import  extract_markdown_images, extract_markdown_links


class TestExtract(unittest.TestCase):
    
    def test_image_1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)" 
        image_results = extract_markdown_images(text)
        self.assertEqual(image_results, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])


    def test_image_2(self):
        text = "testing ![google](https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjUj4vg68aVAxWaTDABHSBoNBwQPAgI)."
        image_results = extract_markdown_images(text)
        self.assertEqual(image_results, [("google", "https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwjUj4vg68aVAxWaTDABHSBoNBwQPAgI")])

    def test_link_1(self):
        text = "this is a test of a link to [google](https://google.com)."
        link_results = extract_markdown_links(text)
        self.assertEqual(link_results, [("google", "https://google.com")])

    def test_link_2(self):
        text = "if you still use [facebook](https://facebook.com) or [myspace](https://myspace.com) you are ancient."
        link_results = extract_markdown_links(text)
        self.assertEqual(link_results, [("facebook", "https://facebook.com"), ("myspace", "https://myspace.com")])


    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)