class view_bag():
    def __init__(self):
        self.view_dict = {}
    def set(self, key, value):
        self.view_dict[key] = value
    def get(self, key):
        if key in self.view_dict.keys():
            return self.view_dict[key]
        return None
    def get_all(self):
        return self.view_dict
    def clear(self):
        self.view_dict = {}