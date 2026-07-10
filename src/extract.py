import re
from textnode import TextNode

def extract_markdown_images(text: str) -> list[tuple]:
     results = re.findall(r"!\[([^\[\]]+)\]\(([^\(\)]+)\)", text)
     return results
     

def extract_markdown_links(text: str) -> list[tuple]:
     results = re.findall(r"\[([^\[\]]+)\]\(([^\(\)]+)\)", text)
     return results

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
     pass

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
     new_list = []
     for old_node in old_nodes:
          link_list = extract_markdown_links(old_node.text)
          split_nodes = re.split(r"\[[^\[\]]+\]\([^\(\)]+\)", old_node.text)
          if split_nodes[len(split_nodes)] == "":
               split_nodes.pop()
          for i in range(0,len(split_nodes)):
               if i % 2 == 0:
                    new_list.append(TextNode(split_nodes[i], TextType.TEXT))
               else:
                    new_list.append(Text)
                    