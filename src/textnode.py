from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type # member of the TextType Enum
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type.value == other.text_type.value and
            self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def textnode_to_htmlnode(text_node):
    if not isinstance(text_node, TextNode):
        raise ValueError(f"text_node type must be TextNode. Received {type(text_node).__name__}.")

    text = text_node.text

    match text_node.text_type.value:
        case TextType.TEXT.value:
            return LeafNode(None, text)
        case TextType.BOLD.value:
            return LeafNode("b", text)
        case TextType.ITALIC.value:
            return LeafNode("i", text)
        case TextType.CODE.value:
            return LeafNode("code", text)
        case TextType.LINK.value:
            return LeafNode("a", text, {
                "href": text_node.url or ""
            })
        case TextType.IMAGE.value:
            return LeafNode("img", "", {
                "src": text_node.url or "",
                "alt": text
            })
        case _:
            raise ValueError("text_node.text_type type must be TextType Enum.")
