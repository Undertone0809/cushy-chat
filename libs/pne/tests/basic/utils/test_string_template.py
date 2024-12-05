import pytest

from pne.utils.string_template import StringTemplate


def test_fstring_template_simple():
    template = "Hello {name}!"
    st = StringTemplate(template, template_format="f-string")
    result = st.format(name="World")
    assert result == "Hello World!"
    assert st.variables == ["name"]


def test_fstring_template_multiple_vars():
    template = "My name is {name} and I am {age} years old."
    st = StringTemplate(template, template_format="f-string")
    result = st.format(name="Alice", age=25)
    assert result == "My name is Alice and I am 25 years old."
    assert sorted(st.variables) == sorted(["name", "age"])


def test_jinja2_template_simple():
    template = "Hello {{ name }}!"
    st = StringTemplate(template, template_format="jinja2")
    result = st.format(name="World")
    assert result == "Hello World!"
    assert st.variables == ["name"]


def test_jinja2_template_complex():
    template = """
    {% for item in items %}
        - {{ item }}
    {% endfor %}
    Total: {{ total }}
    """
    st = StringTemplate(template, template_format="jinja2")
    result = st.format(items=["apple", "banana"], total=2)
    expected = """

        - apple

        - banana

    Total: 2
    """
    assert result == expected
    assert sorted(st.variables) == sorted(["items", "total"])


def test_invalid_template_format():
    template = "Hello {name}!"
    with pytest.raises(ValueError) as excinfo:
        StringTemplate(template, template_format="invalid")
    assert "template_format must be one of 'f-string' or 'jinja2'" in str(excinfo.value)


def test_missing_variable():
    template = "Hello {name}!"
    st = StringTemplate(template, template_format="f-string")
    with pytest.raises(KeyError):
        st.format(wrong_name="World")


def test_jinja2_template_with_conditional():
    template = """
    {% if age >= 18 %}
        You are an adult.
    {% else %}
        You are a minor.
    {% endif %}
    Name: {{ name }}
    """
    st = StringTemplate(template, template_format="jinja2")
    result = st.format(age=20, name="Alice")
    expected = """

        You are an adult.

    Name: Alice
    """
    assert result == expected
    assert sorted(st.variables) == sorted(["age", "name"])
