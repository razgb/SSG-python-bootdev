import unittest
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "example.com",
            "target": "_blank",
        }
        node = HTMLNode("p", "testing", None, props)
        self.assertEqual(node.props_to_html(), ' href="example.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode("span", "testing")
        self.assertEqual(repr(node), "HTMLNode(span, testing, None, None)")

    def test_to_html_error(self):
        node = HTMLNode("span", "testing")
        works = None

        try:
            node.to_html()
            works = False
        except Exception:
            works = True
        self.assertTrue(works)

    def test_base_case(self):
        node = HTMLNode("p", "testing", None, {"class": "text-sm"})
        self.assertTrue((
            node.tag == "p" and
            node.value == "testing" and
            node.children is None and
            node.props_to_html() == ' class="text-sm"'
        ))

    def test_none_case(self):
        node = HTMLNode()
        self.assertTrue((
            node.tag is None and
            node.value is None and
            node.children is None and
            node.props is None
        ))


if __name__ == "__main__":
    unittest.main()
