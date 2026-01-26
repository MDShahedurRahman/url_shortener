import json
import os


class JsonStorage:

    FILE_NAME = "urls.json"

    def save(self, data):
        with open(self.FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        with open(self.FILE_NAME, "r") as f:
            return json.load(f)
