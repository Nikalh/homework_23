import re
from typing import Union, Generator, List, Iterable, Optional


def filter_query(param: str, data: Union[Generator, List[str]]):
    return list(filter(lambda x: param in x, data))


def map_query(param: str, data: Iterable[str]):
    col_number = int(param)
    return map(lambda x: x.split(' ')[col_number], data)


def unique_query(data: Iterable[str], *args, **kwargs):
    return set(data)


def sort_query(param: str, data: Iterable[str]):
    return sorted(data, reverse=param == 'desc')


def limit_query(param: str, data: Iterable[str]):
    limit = int(param)
    return list(data)[:limit]


def regex_query(param: str, data: Iterable[str]):
    filtered_values = filter(lambda v: re.match(param, v), data)
    return list(filtered_values)
