from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    max_salary = 0

    for row in data:
        max_salary_row = row.get('max_salary', '').strip()
        if max_salary_row:
            try:
                max_salary = max(max_salary, int(max_salary_row))
            except ValueError:
                pass

    return max_salary


def get_min_salary(path: str) -> int:
    data = read(path)
    min_salary = float('inf')
    for row in data:
        min_salary_row = row.get('min_salary', '').strip()
        if min_salary_row:
            try:
                min_salary = min(min_salary, int(min_salary_row))
            except ValueError:
                pass

    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if ("min_salary" not in job or "max_salary" not in job or
            (not isinstance(job["min_salary"], (int, str)) or
             not isinstance(job["max_salary"], (int, str))) or
            int(job["min_salary"]) > int(job["max_salary"]) or
            not isinstance(salary, (int, str))):
        raise ValueError("Invalid job or salary information")

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass
    return filtered_jobs
