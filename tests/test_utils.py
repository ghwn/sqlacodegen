import pytest

from sqlacodegen.utils import to_snake_case


@pytest.mark.parametrize(
    "input, expected",
    [
        ("PascalCase", "pascal_case"),
        ("snake_case", "snake_case"),
        ("camelCase", "camel_case"),
        ("PCase", "p_case"),
        ("UPPER", "upper"),
        ("APICall", "api_call"),
        ("TOPICTestAPITestCase", "topic_test_api_test_case"),
    ],
)
def test_to_snake_case(input: str, expected: str) -> None:
    assert to_snake_case(input) == expected
