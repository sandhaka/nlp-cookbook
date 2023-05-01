import json


class SetElement:
    def __init__(self, id, text, categories):
        self.id = id
        self.text = text
        self.categories = categories


class SetElementEncoder(json.JSONEncoder):
    def default(self, o: SetElement):
        return o.__dict__


class SetElementDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=SetElementDecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("id") is not None:
            return SetElement(d["id"], d["text"], d["categories"])
        return d
