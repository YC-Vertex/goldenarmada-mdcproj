class AIError(Exception):
    def __init__(self, type, mess):
        self.e_type = type
        self.e_message = mess