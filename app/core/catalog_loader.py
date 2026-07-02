import json


class CatalogLoader:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_catalog(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            catalog = json.load(file)

        return catalog