from functools import partial
from typing import List, Tuple

import pytest
from solver.solver import Move, Pos, Solver


def convert_terrain(t: str) -> List[List[str]]:
    return [x.split() for x in t.split('\n')]


def find_position(terrain: List[List[str]]) -> Tuple[Pos, Pos]:
    start, stop = None, None
    for ri, r in enumerate(terrain):
        for ci, c in enumerate(r):
            if c == 'S':
                start = Pos(ri, ci)
            elif c == 'T':
                stop = Pos(ri, ci)

    print(start, stop)
    if not start or not stop:
        raise Exception("Wrong terrain")
    return start, stop


def test_faulty_terrain_should_raise():
    twisted_terrain = (
        'o x x o o\n'
        'x o o T o\n'
        'o x o o o\n'
        'o x o o o\n'
        'o x o o o\n'
        'o x o o o'
    )

    with pytest.raises(Exception):
        start, stop = find_position(twisted_terrain)


def terrain(t: List[List[str]], p: Pos):
    return (
        (p.col >= 0 and p.col < len(t[0])) and
        (p.row >= 0 and p.row < len(t)) and
        (t[p.row][p.col] != "x"))


def test_case_simple():

    terrain_string = (
        'o x x o o\n'
        'S o o T o\n'
        'o x o o o\n'
        'o x o o o\n'
        'o x o o o'
    )

    t = convert_terrain(terrain_string)
    print("\n" + terrain_string)

    start, stop = find_position(t)
    solver = Solver(start, stop, partial(terrain, t))
    assert solver.solve() == [Move.RIGHT, Move.RIGHT]


def test_case_1():

    terrain_string = (
        'o x x o o\n'
        'o o o T o\n'
        'o x o o o\n'
        'o x o o o\n'
        'S x o o o'
    )

    t = convert_terrain(terrain_string)
    print("\n" + terrain_string)

    start, stop = find_position(t)
    solver = Solver(start, stop, partial(terrain, t))
    assert solver.solve() == [Move.UP, Move.UP, Move.RIGHT, Move.RIGHT]


def test_case_2():
    terrain_string = (
        'o x x o o\n'
        'x o o T o\n'
        'o x o o o\n'
        'o x o o o\n'
        'o x o o o\n'
        'o x S o o'
    )

    t = convert_terrain(terrain_string)
    print("\n" + terrain_string)

    start, stop = find_position(t)
    solver = Solver(start, stop, partial(terrain, t))
    assert solver.solve() == [Move.RIGHT, Move.UP,
                              Move.LEFT, Move.UP, Move.RIGHT, Move.UP]
