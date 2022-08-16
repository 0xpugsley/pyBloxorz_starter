from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List, Tuple


class Move:
    # TODO
    pass


@dataclass(frozen=True)
class Pos:
    row: int
    col: int

    def drow(self, d) -> Pos:
        return Pos(self.row + d, self.col)

    def dcol(self, d) -> Pos:
        return Pos(self.row, self.col + d)


@dataclass(frozen=True)
class Block:
    """ A block is represented by the position of the two cubes.
        b1 has to be lexicographically smaller than b2
    """
    b1: Pos
    b2: Pos

    def __post_init__(self):
        assert self.b1.row <= self.b2.row and self.b1.col <= self.b2.col,\
            f"Invalid block position b1 = {self.b1}, b2 = {self.b2}"

    def drow(self, d1: int, d2: int) -> Block:
        return Block(self.b1.drow(d1), self.b2.drow(d2))

    def dcol(self, d1: int, d2: int) -> Block:
        return Block(self.b1.dcol(d1), self.b2.dcol(d2))

    def is_standing(self) -> bool:
        return self.b1 == self.b2

    def left(self) -> Block:
        if self.is_standing():
            return self.dcol(-2, -1)
        elif self.b1.row == self.b2.row:
            return self.dcol(-1, -2)
        else:
            return self.dcol(-1, -1)

    def right(self) -> Block:
        # TODO
        pass

    def up(self) -> Block:
        if self.is_standing():
            return self.drow(-2, -1)
        elif self.b1.row == self.b2.row:
            return self.drow(-1, -1)
        else:
            return self.drow(-1, -2)

    def down(self) -> Block:
        # TODO
        pass

    def neighbors(self) -> Tuple[Tuple[Block, Move]]:
        """ Suggestion: visit them in the order: left, right, up, down """
        # TODO
        pass


class Solver:
    def __init__(self, start: Pos, goal: Pos, terrain: Callable[[Pos], bool]) -> None:
        self.goal = goal
        self.start = start
        self.terrain = terrain

    def done(self, block: Block) -> bool:
        return block.is_standing() and block.b1 == self.goal

    def is_legal(self, b1: Pos, b2: Pos) -> bool:
        return self.terrain(b1) and self.terrain(b2)

    def solve(self) -> List[Move]:
        # TODO
        return []
