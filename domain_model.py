class Person:
    def __init__(self, name, emotion):
        self.name = name
        self.emotion = emotion
        self.state = None

    def laugh(self):
        """ Человек смеется. """
        self.emotion = "laughing"

    def transform(self):
        """ Человек превращается в газ. """
        self.state = "transformed"


class Girl:
    def __init__(self, name, emotion):
        self.name = name
        self.emotion = emotion
        self.state = None

    def hate(self, person):
        """ Девушка ненавидит человека. """
        self.emotion = "hating"

    def transform(self):
        """ Девушка исчезает, превращаясь в облако. """
        self.state = "disappeared"


class Bar:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.is_full = False

    def fill(self):
        """ Наполняем бар. """
        self.is_full = True


class Transformation:
    def __init__(self, substance, time):
        self.substance = substance
        self.time = time

    def transformPerson(self, person):
        """ Превращаем человека в газ. """
        person.state = "transformed"
