from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    unique_industries = set()

    for row in data:
        industry = row.get('industry', '').strip()
        if industry:
            unique_industries.add(industry)

    return list(unique_industries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_industry = []

    for job in jobs:
        if job.get('industry') == industry:
            filtered_industry.append(job)

    return filtered_industry
