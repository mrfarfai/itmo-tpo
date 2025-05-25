class Person:
    def __init__(self, name: str, emotion: str):
        self.name = name
        self.emotion = emotion
        self.state = None

    def laugh(self):
        """Человек смеётся."""
        self.emotion = "laughing"

    def transform(self):
        """Человек превращается в газ."""
        self.state = "transformed"


class Girl(Person):
    def __init__(self, name: str, emotion: str):
        super().__init__(name, emotion)

    def hate(self, person: Person):
        """Девушка ненавидит другого человека."""
        # можно, например, учесть чьё именно имя
        self.emotion = f"hating {person.name}"

    def transform(self):
        """Девушка исчезает, превращаясь в облако."""
        self.state = "disappeared"


class Bar:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.is_full = False

    def fill(self):
        """Наполняем бар."""
        self.is_full = True


class Transformation:
    def __init__(self, substance: str, time: float):
        self.substance = substance
        self.time = time

    def transformPerson(self, person: Person):
        """Превращаем человека в газ."""
        person.state = "transformed"
