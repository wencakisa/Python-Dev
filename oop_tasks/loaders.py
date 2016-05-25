import json
import yaml
import os


class Loader:
    def __init__(self, filename):
        if os.access(filename, os.R_OK) and os.path.isfile(filename):
            self.filename = filename
        else:
            raise ValueError("Inaccessible file '{}'".format(filename))

    def load_data(filename):
        raise NotImplementedError()


class JSONLoader(Loader):
    def load_data(self):
        with open(self.filename) as f:
            input_data = json.load(f)
            return input_data


class YAMLoader(Loader):
    def load_data(self):
        with open(self.filename) as f:
            input_data = yaml.load(f)
            return input_data
