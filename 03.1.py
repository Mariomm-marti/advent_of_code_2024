import re
from pathlib import Path

contents: str = Path('./input.txt').read_text()
search = re.finditer(r'mul\((\d+),(\d+)\)', contents)
result: int = sum([int(mul.groups()[0]) * int(mul.groups()[1])
                  for mul in search])
print('Found total:', result)
