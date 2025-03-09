import unittest
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_leaf_to_html_paragraph(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "example", props={"href":"http://example.com"})
        self.assertEqual(node.to_html(), '<a href="http://example.com">example</a>')

    def test_leaf_to_html_bold(self):
        node = LeafNode("b", "bold text")
        self.assertEqual(node.to_html(), '<b>bold text</b>')

    def test_leaf_to_html_image(self):
        node = LeafNode("img", '', {"src":"http://example.com"})
        self.assertEqual(node.to_html(), '<img src="http://example.com"/>')

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "I'm raw text!")
        self.assertEqual(node.to_html(), "I'm raw text!")

    def test_leaf_to_html_inline_code(self):
        node = LeafNode("code", "nums = [1,2,3]")
        self.assertEqual(node.to_html(), "<code>nums = [1,2,3]</code>")


if __name__ == "__main__":
    unittest.main()
