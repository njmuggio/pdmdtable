import pytest
from pdmdtable import build_table, TableDimensionError


def test_empty_inputs():
    with pytest.raises(TableDimensionError):
        build_table([], [])


def test_no_rows():
    assert """\
+------+-----+
| Name | Age |
+======+=====+
+------+-----+\
""" == build_table(
        ["Name", "Age"], []
    )


def test_simple_table():
    header = ["Name", "Age"]
    body = [
        ["Alice", 32],
        ["Bob", 42],
    ]
    assert """\
+-------+-----+
| Name  | Age |
+=======+=====+
| Alice | 32  |
+-------+-----+
| Bob   | 42  |
+-------+-----+\
""" == build_table(
        header, body
    )


def test_tall_header():
    header = ["Sample", "Age\n(sec)"]
    body = [
        ["A", "1"],
        ["B", "2"],
    ]
    assert """\
+--------+-------+
| Sample | Age   |
|        | (sec) |
+========+=======+
| A      | 1     |
+--------+-------+
| B      | 2     |
+--------+-------+\
""" == build_table(
        header, body
    )


def test_tall_body():
    header = ["Step", "Notes"]
    body = [
        ["1", "Two things happened:\n - Sample turned blue\n - Sample started singing"],
        ["2", "Nothing of note here"],
    ]
    assert """\
+------+---------------------------+
| Step | Notes                     |
+======+===========================+
| 1    | Two things happened:      |
|      |  - Sample turned blue     |
|      |  - Sample started singing |
+------+---------------------------+
| 2    | Nothing of note here      |
+------+---------------------------+\
""" == build_table(
        header, body
    )


def test_short_row():
    header = ["A", "B"]
    body = [
        ["1", "2"],
        ["5"],
        ["3", "4"],
    ]
    assert """\
+---+---+
| A | B |
+===+===+
| 1 | 2 |
+---+---+
| 5 |   |
+---+---+
| 3 | 4 |
+---+---+""" == build_table(
        header, body
    )


def test_empty_row():
    header = ["A", "B"]
    body = [
        ["1", "2"],
        [],
        ["3", "4"],
    ]
    assert """\
+---+---+
| A | B |
+===+===+
| 1 | 2 |
+---+---+
|   |   |
+---+---+
| 3 | 4 |
+---+---+""" == build_table(
        header, body
    )
