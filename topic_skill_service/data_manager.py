#data_manager.py
# This module provides a simple JSON data manager for reading and writing data files.

import json
import os

class JsonDataManager:
    def __init__(self, base_path):
        self.base_path= base_path

    def read_data(self, filename):
        file_path = os.path.join(self.base_path, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: {file_path} not found.")
            return []
        except json.JSONDecodeError:
            print(f"Error: {file_path} contains invalid JSON.")
            return []

    def write_data(self, filename, data):
        file_path = os.path.join(self.base_path, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
