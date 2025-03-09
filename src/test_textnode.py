import unittest
from textnode import TextType, TextNode


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


if __name__ == "__main__":
    unittest.main()
