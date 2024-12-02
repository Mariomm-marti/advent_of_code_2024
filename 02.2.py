from pathlib import Path


def is_safe_report(report: list[int]) -> bool:
    is_desc_seq: bool = (report[0] - report[1]) > 0
    for i in range(0, len(report) - 1):
        diff: int = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False
        if is_desc_seq and report[i] < report[i + 1]:
            return False
        if not is_desc_seq and report[i] > report[i + 1]:
            return False
    return True


contents: str = Path('./input.txt').read_text()
lines: list[str] = list(filter(None, contents.split('\n')))
reports: list[list[int]] = list(
    map(lambda line: list(map(int, line.split(' '))), lines))

safe_reports = 0
for report in reports:
    if is_safe_report(report):
        safe_reports += 1
        continue
    for report_index in range(0, len(report)):
        if is_safe_report(report[:report_index] + report[report_index + 1:]):
            safe_reports += 1
            break
print(safe_reports)
