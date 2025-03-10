import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_nested_parents(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        super_parent_node = ParentNode("main", [parent_node])

        self.assertEqual(
            super_parent_node.to_html(),
            "<main><div><span>child</span></div></main>",
        )

    def test_to_html_parent_with_multiple_siblings(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("strong", "child2")
        parent_node = ParentNode("div", [child_node, child_node2])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span><strong>child2</strong></div>",
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", None)
        works = None

        try:
            parent_node.to_html()
            works = False
        except Exception:
            works = True

        self.assertTrue(works)

    def test_to_html_with_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        works = None

        try:
            parent_node.to_html()
            works = False
        except Exception:
            works = True

        self.assertTrue(works)


if __name__ == "__main__":
    unittest.main()
