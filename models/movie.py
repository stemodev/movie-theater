class movie:
    def __init__(self, dictionary):
        for key in dictionary:
            #print(key)
            setattr(self, key, dictionary[key])