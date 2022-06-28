import json

class Pybox:
    def __init__(self, *, style="single"):
        """
        Style:
            Either 'single', 'double', or 'curved'. 
            Is 'single' by default. 
        """

        chars = Pybox.__read_style(style)

        self.horizontal = chars["horizontal"]
        self.vertical = chars["vertical"]
        self.top_left = chars["topLeft"]
        self.top_right = chars["topRight"]
        self.bottom_left = chars["bottomLeft"]
        self.bottom_right = chars["bottomRight"]
    

    @staticmethod
    def __read_style(style_name):
        # Box characters are taken from https://www.unicode.org/charts/PDF/U2500.pdf

        with open("pybox/outline.json", "r", encoding="utf8") as f: # TODO: Package pybox, so this open path should be different
            return json.loads(f.read())[style_name]


    def print(self, text: str):
        print(self.write(text))


    def write(self, text: str):
        text = f" {str(text)} "
        length = len(text)

        out = ""

        out += f"{self.top_left}{self.horizontal*length}{self.top_right}"
        out += f"\n{self.vertical}{text}{self.vertical}"
        out += f"\n{self.bottom_left}{self.horizontal*length}{self.bottom_right}"

        return out