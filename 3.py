import unittest
from domain_model import Person, Girl, Bar, Transformation

class TestPerson(unittest.TestCase):
    def test_laugh(self):
        """ Проверяем, что человек смеется. """
        person = Person(name="John", emotion="neutral")
        person.laugh()
        self.assertEqual(person.emotion, "laughing", "Person should laugh")

    def test_transform(self):
        """ Проверяем, что человек превращается. """
        person = Person(name="John", emotion="neutral")
        person.transform()
        self.assertEqual(person.state, "transformed", "Person should be transformed")


class TestGirl(unittest.TestCase):
    def test_hate(self):
        """ Проверяем, что девушка ненавидит человека. """
        girl = Girl(name="Alice", emotion="neutral")
        person = Person(name="John", emotion="laughing")
        girl.hate(person)
        self.assertEqual(girl.emotion, "hating", "Girl should hate the person")

    def test_transform(self):
        """ Проверяем, что девушка исчезает. """
        girl = Girl(name="Alice", emotion="hating")
        girl.transform()
        self.assertEqual(girl.state, "disappeared", "Girl should disappear")


class TestBar(unittest.TestCase):
    def test_fill(self):
        """ Проверяем, что бар наполняется. """
        bar = Bar(name="The Dive", location="Downtown")
        bar.fill()
        self.assertTrue(bar.is_full, "Bar should be filled")


class TestTransformation(unittest.TestCase):
    def test_transformation(self):
        """ Проверяем, что человек превращается в газ. """
        person = Person(name="John", emotion="laughing")
        transformation = Transformation(substance="hydrogen", time=1.5)
        transformation.transformPerson(person)
        self.assertEqual(person.state, "transformed", "Person should be transformed into gas")


if __name__ == "__main__":
    unittest.main()
