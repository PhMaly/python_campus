import pytest
from src.diamond import create_diamond


def test_diamond_b():
    assert create_diamond("B") == """\
 A
B B
 A"""


def test_diamond_c():
    assert create_diamond("C") == """ A
 B B
C   C
 B B
  A"""



