from textnode import *
from extract import split_nodes_link
from textnode import TextNode, TextType

def main():
   text = TextNode("This is text with [google](https://google) and [facebook](https://facebook.com).", TextType.TEXT)
   print(split_nodes_link([text]))


main()
