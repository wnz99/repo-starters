import pytest
from pydantic import ValidationError

from starter_python import Name


def test_name_normalizes_whitespace() -> None:
    assert Name(value=" Ada ").value == "Ada"


def test_name_rejects_empty_input() -> None:
    with pytest.raises(ValidationError):
        Name(value="   ")
