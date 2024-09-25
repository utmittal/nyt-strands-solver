from dataclasses import dataclass


class PuzzleBoard:
    __spaced_grid: list[list[str]]

    @dataclass
    class Node:
        row: int
        col: int
        letter: str
        neighbours: tuple[int, int]

    def __init__(self, letters_csv: str):
        """
        Initialized puzzle board.
        :param letters_csv: Grid in the form of a comma separated list, where each value is the characters in a row.
        Example: xyz,abc,pqr
        """
        self.__spaced_grid = []

        rows = letters_csv.split(',')
        if len(rows) != 8:
            raise ValueError(f"Expected 8 rows, got {len(rows)}.")
        for i, row in enumerate(rows):
            if len(row) != 6:
                raise ValueError(f"Expected 6 letters in row, got {len(row)} (row = {row}).")

            spaced_row = '   '.join(row)
            self.__spaced_grid.append([char.upper() for char in spaced_row])
            self.__spaced_grid.append([' ' for _ in range(21)])

        self.__spaced_grid = self.__spaced_grid[:-1]

    def pretty_print(self) -> None:
        for row in self.__spaced_grid:
            print(''.join(row))
