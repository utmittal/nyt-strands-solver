class PuzzleBoard:
    __grid: list[list[str]]

    def __init__(self, letters_csv: str):
        """
        Initialized puzzle board.
        :param letters_csv: Grid in the form of a comma separated list, where each value is the characters in a row.
        Example: xyz,abc,pqr
        """
        self.__grid = []

        rows = letters_csv.split(',')
        if len(rows) != 8:
            raise ValueError(f"Expected 8 rows, got {len(rows)}.")
        for i, row in enumerate(rows):
            if len(row) != 6:
                raise ValueError(f"Expected 6 letters in row, got {len(row)} (row = {row}).")

            spaced_row = '   '.join(row)
            self.__grid.append([char.upper() for char in spaced_row])
            self.__grid.append([' ' for _ in range(21)])

        self.__grid = self.__grid[:-1]

    def pretty_print(self) -> None:
        for row in self.__grid:
            print(''.join(row))
