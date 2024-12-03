import re
from pathlib import Path


def add_multiplications(content: str) -> int:
    search = re.finditer(r'mul\((\d+),(\d+)\)', content)
    result: int = sum([int(mul.groups()[0]) * int(mul.groups()[1])
                      for mul in search])
    return result


contents: str = Path('./input.txt').read_text()
do_list: list[str] = contents.split('do()')
does_without_donts: list[str] = list(
    map(lambda do: do.split('don\'t()')[0], do_list))
print('Found total:', sum(list(map(add_multiplications, does_without_donts))))
