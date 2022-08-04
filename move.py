class Move:
    def __init__(self, value):
        self._value = value

    @ property
    def value(self):   # metoda ktora zwraca wartosc artybutu value
        return self._value

    def is_valid(self):  # metoda sprawdzajaca poprawnosc value przedzial 1 -9
        return 1 <= self._value <= 9


    def get_row(self):
        if self._value in (1, 2, 3):
            return 0 # First row
        elif self._value in (4, 5, 6):
            return 1 # second row
        else:
            return 2 # third row

    def get_column(self):           # metoda zwrcajaca kolumne z planszy
        if self._value in (1, 4, 7):
            return 0 #first column
        elif self._value in (2, 5, 8):
            return 1 # second column
        else:
            return 2 #Third column

#         col0 col1 col2
# row 0 : | 1 | 2 | 3 |
# row 1 : | 4 | 5 | 6 |
# row 2 : | 7 | 8 | 9 |




