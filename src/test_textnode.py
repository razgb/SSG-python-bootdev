import unittest
from textnode import TextType, TextNode, textnode_to_htmlnode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("testing", TextType.BOLD)
        node2 = TextNode("testing", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("testing", TextType.ITALIC)
        node2 = TextNode("test", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("Testing", TextType.TEXT)
        self.assertEqual(node.url, None)

    def test_url(self):
        node = TextNode("Testing", TextType.TEXT, "http://www.example.com")
        self.assertEqual(node.url, "http://www.example.com")

    def test_repr(self):
        node = TextNode("testing", TextType.TEXT)
        self.assertEqual(repr(node), "TextNode(testing, text, None)")

    # below are tests for textnode to htmlnode

    def test_raw_text_to_leafnode(self):
        text_node = TextNode("This is a text node", TextType.TEXT)
        html_node = textnode_to_htmlnode(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic_to_leafnode(self):
        text_node = TextNode("bonjour", TextType.ITALIC)
        html_node = textnode_to_htmlnode(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "bonjour")

    def test_bold_to_leafnode(self):
        text_node = TextNode("go away!", TextType.BOLD)
        html_node = textnode_to_htmlnode(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "go away!")

    def test_code_to_leafnode(self):
        text_node = TextNode("const name = 'raz'", TextType.CODE)
        html_node = textnode_to_htmlnode(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, text_node.text)

    def test_link_to_leafnode(self):
        text_node = TextNode("go to example", TextType.LINK, url="http://example.com")
        html_node = textnode_to_htmlnode(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, text_node.text)
        self.assertEqual(html_node.props["href"], text_node.url)

    def test_image_to_leafnode(self):
        text_node = TextNode("go to image", TextType.IMAGE, url="http://example.com")
        html_node = textnode_to_htmlnode(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["alt"], text_node.text)
        self.assertEqual(html_node.props["src"], text_node.url)


if __name__ == "__main__":
    unittest.main()
