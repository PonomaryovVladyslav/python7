class Figure:
    color: str = 'white'
    position_x: int = 0
    position_y: int = 0

    def change_color(self) -> None:
        self.color = 'black' if self.color == 'white' else 'white'

    def move(self, x: int, y: int) -> None:
        self.position_x = x
        self.position_y = y

    def count_absolute_difference(self, x: int, y: int) -> tuple[int, int]:
        return abs(self.position_x - x), abs(self.position_y - y)

    def check_move(self, x: int, y: int) -> bool:
        raise NotImplementedError


class Pawn(Figure):
    def check_move(self, x: int, y: int) -> bool:
        if x == self.position_x:
            if self.color == 'white':
                return y == self.position_y + 1
            else:
                return y == self.position_y - 1
        return False


class Knight(Figure):
    def check_move(self, x: int, y: int) -> bool:
        x_diff, y_diff = self.count_absolute_difference(x, y)
        return (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1)


class Bishop(Figure):
    def check_move(self, x: int, y: int) -> bool:
        x_diff, y_diff = self.count_absolute_difference(x, y)
        return x_diff == y_diff and x_diff > 0


class Rook(Figure):
    def check_move(self, x: int, y: int) -> bool:
        return (x == self.position_x and y != self.position_y) or (x != self.position_x and y == self.position_y)


class Queen(Figure):

    def check_move(self, x: int, y: int) -> bool:
        x_diff, y_diff = self.count_absolute_difference(x, y)
        as_bishop = x_diff == y_diff and x_diff > 0
        as_rook = (x == self.position_x and y != self.position_y) or (x != self.position_x and y == self.position_y)
        return as_bishop or as_rook


class King(Figure):

    def check_move(self, x: int, y: int) -> bool:
        x_diff, y_diff = self.count_absolute_difference(x, y)
        return x_diff <= 1 and y_diff <= 1 and not (not x_diff == 0 and not y_diff == 0)


queen = Queen()
queen.move(5, 3)
print(queen.check_move(5, 7))
rook = Rook()
rook.move(2, 3)
print(rook.check_move(6, 3))
bishop = Knight()
bishop.move(3, 4)
print(bishop.check_move(5, 5))
