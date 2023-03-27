from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    unique_job_types = set()

    for row in data:
        job_type = row.get('job_type', '').strip()
        if job_type:
            unique_job_types.add(job_type)

    return list(unique_job_types)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = []

    for job in jobs:
        if job.get('job_type') == job_type:
            filtered_jobs.append(job)

    return filtered_jobs
