class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """
        Child classes will overide this method.
        Includes: leafnode and parentnode
        """
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""

        output = ""
        for key in self.props:
            output += f' {key}="{self.props[key]}"'
        return output

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
