from pathlib import Path

contents: str = Path('./input.txt').read_text()
lines: list[str] = list(filter(None, contents.split('\n')))
left_column: list[str] = list(
    map(lambda row: list(filter(None, row.split(' ')))[0], lines))
right_column: list[str] = list(
    map(lambda row: list(filter(None, row.split(' ')))[1], lines))
sorted_left_column: list[int] = sorted(list(map(int, left_column)))
sorted_right_column: list[int] = sorted(list(map(int, right_column)))
column_differences: list[int] = list(
    map(lambda a, b: abs(a - b), sorted_left_column, sorted_right_column))
print(f'Difference: {sum(column_differences)}')
