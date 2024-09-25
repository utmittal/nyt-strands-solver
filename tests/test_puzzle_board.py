import pytest

from puzzle_board import PuzzleBoard


def test_init_too_many_rows_raises_value_error():
    with pytest.raises(ValueError):
        PuzzleBoard('aaaaaa,aaaaaa,aaaaaa,aaaaaa,aaaaaa,aaaaaa,aaaaaa,aaaaaa,aaaaaa')


def test_init_too_few_rows_raises_value_error():
    with pytest.raises(ValueError):
        PuzzleBoard('aaaaaa,aaaaaa,aaaaaa,aaaaaa,aaaaaa,aaaaaa,aaaaaa')


def test_init_too_many_letters_in_row_raises_value_error():
    with pytest.raises(ValueError):
        PuzzleBoard('aaaaaa,aaaaaa,aaaaaa,aaaaaa,aaaaaa,aaaaaa,aaaaaa,bbbbbbb')


def test_init_too_few_letters_in_row_raises_value_error():
    with pytest.raises(ValueError):
        PuzzleBoard('aaaaaa,aaaaaa,aaaaaa,aaaaaa,aaaaaa,aaaaaa,aaaaaa,bbbbb')


def test_pretty_print(capsys):
    puzzle = PuzzleBoard('ircirh,rbtsac,elorgh,lahiab,rbeybs,lngewi,nakltn,epyapg')

    puzzle.pretty_print()

    captured = capsys.readouterr()
    assert captured.out == """I   R   C   I   R   H
                     
R   B   T   S   A   C
                     
E   L   O   R   G   H
                     
L   A   H   I   A   B
                     
R   B   E   Y   B   S
                     
L   N   G   E   W   I
                     
N   A   K   L   T   N
                     
E   P   Y   A   P   G
"""
