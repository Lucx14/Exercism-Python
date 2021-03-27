import re


class MarkdownParser:
    BOLD_PATTERN = re.compile(r"\b__(.*?)__\b")
    ITALICS_PATTERN = re.compile(r"\b_(.*?)_\b")

    def __init__(self, markdown):
        self.markdown = markdown

    def parse(self):
        return "".join(self.wrap_list(self.add_element_tags(self.add_emphasis_tags())))

    def wrap_text(self, text, tag):
        return f"<{tag}>{text}</{tag}>"

    def is_header(self, text):
        return text[0] == "#"

    def is_list_item(self, text):
        return text[0] == "*"

    def crop_and_sub(self, pattern, crop_size, tag, target):
        return re.sub(
            pattern,
            lambda match: self.wrap_text(match.group()[crop_size:-crop_size], tag),
            target,
        )

    def add_emphasis_tags(self):
        return self.crop_and_sub(
            self.ITALICS_PATTERN,
            1,
            "em",
            self.crop_and_sub(self.BOLD_PATTERN, 2, "strong", self.markdown),
        )

    def add_element_tags(self, markdown_text):
        res = []
        for el in markdown_text.split("\n"):
            if self.is_header(el):
                size = len(el.split()[0])
                res.append(self.wrap_text(el[size + 1 :], f"h{size}"))
            elif self.is_list_item(el):
                res.append(self.wrap_text(el[2:], "li"))
            else:
                res.append(self.wrap_text(el, "p"))

        return res

    def wrap_list(self, elements):
        list_active = False
        updated_elements = []

        for i, el in enumerate(elements):
            if el.startswith("<li>"):
                if not list_active:
                    updated_elements.append("<ul>")
                    updated_elements.append(el)
                    list_active = True
                else:
                    updated_elements.append(el)
                    if i == len(elements) - 1:
                        updated_elements.append("</ul>")
                        list_active = False
                    elif not elements[i + 1].startswith("<li>"):
                        updated_elements.append("</ul>")
                        list_active = False
            else:
                updated_elements.append(el)

        return updated_elements


def parse(markdown):
    return MarkdownParser(markdown).parse()
