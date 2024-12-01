from collections import Counter
from pathlib import Path

contents: str = Path('./input.txt').read_text()
lines: list[str] = list(filter(None, contents.split('\n')))
left_column: list[int] = list(
    map(lambda row: int(list(filter(None, row.split(' ')))[0]), lines))
right_column: list[int] = list(
    map(lambda row: int(list(filter(None, row.split(' ')))[1]), lines))
right_column_count: dict[int, int] = Counter(right_column)
scores: list[int] = list(
    map(lambda column: column * right_column_count[column], left_column))
print(f'Sum of scores: {sum(scores)}')
