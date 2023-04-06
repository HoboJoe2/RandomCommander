class Card:
    def __init__(self, raw_json):
        self.raw_json = raw_json
        self.one_name = self.generate_name()
        self.color_id = self.get_color_id()

    def generate_name(self):
        return f"1 {self.raw_json['name']}"

    def get_color_id(self):
        return f"{self.raw_json['color_identity']}"
