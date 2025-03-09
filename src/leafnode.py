from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node must have values.")

        if not self.tag:
            return self.value

        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}/>"

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
