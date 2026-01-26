import json
import os


class JsonStorage:

    FILE_NAME = "urls.json"

    def save(self, data):
        with open(self.FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)
