"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR".
Write the code that will take a string and make this conversion given a number of rows:
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        if numRows > len(s):
            numRows = len(s)

        rows = split_to_rows(s, numRows)
        new_str = ''
        for i in range(1, numRows + 1):
            new_str += rows[i]

        return new_str


def split_to_rows(s, numRows):
    rows = {}
    rows_counter = 1
    for index, value in enumerate(s):
        if rows_counter not in rows:
            rows[rows_counter] = ''
        rows[rows_counter] += value

        if rows_counter == numRows:
            direction = False
        elif rows_counter == 1:
            direction = True

        if direction:
            rows_counter += 1
        else:
            rows_counter -= 1

    return rows
