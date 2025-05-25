import pytest
from src.domain_model import Person, Girl, Bar, Transformation

@pytest.fixture
def person(girl):
    return Person(name="John", emotion="neutral")

@pytest.fixture
def girl(person):
    return Girl(name="Alice", emotion="neutral")

@pytest.fixture
def bar():
    return Bar(name="The Dive", location="Downtown")

@pytest.fixture
def transformer():
    return Transformation(substance="hydrogen", time=1.5)


def test_person_laugh(person):
    """Person.laugh() устанавливает emotion = 'laughing'."""
    person.laugh()
    assert person.emotion == "laughing"


def test_person_transform(person):
    """Person.transform() устанавливает state = 'transformed'."""
    person.transform()
    assert person.state == "transformed"


def test_girl_inherits_person(person, girl):
    """Girl наследует имя и emotion от Person."""
    assert girl.name == "Alice"
    assert girl.emotion == "neutral"
    girl.hate(person)
    assert "hating" in girl.emotion


def test_girl_transform(girl):
    """Girl.transform() переопределён — state = 'disappeared'."""
    girl.transform()
    assert girl.state == "disappeared"


def test_bar_fill(bar):
    """Bar.fill() устанавливает is_full = True."""
    assert not bar.is_full
    bar.fill()
    assert bar.is_full is True


def test_transformation_transform_person(person, transformer):
    """
    Transformation.transformPerson(person) превращает человека в газ:
    state = 'transformed'
    """
    transformer.transformPerson(person)
    assert person.state == "transformed"
