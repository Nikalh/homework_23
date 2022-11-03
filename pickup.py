from typing import Optional, Iterable, List, Generator

from utils import filter_query, map_query, unique_query, sort_query, limit_query, regex_query

FILE_NAME = 'data/apache_logs.txt'
CMD_TO_UTILS = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,
    'regex': regex_query,

}


# запускаем генератор
def iter_file(file_name: str):
    with open(file_name) as file:
        for line in file:
            yield line


# собираем данные
def query_builder(cmd, value, data: Optional[Iterable[str]]) :
    if data is None:
        prepared_data = iter_file(FILE_NAME)
    else:
        prepared_data = data
    result = CMD_TO_UTILS[cmd](param=value, data=prepared_data)

    return list(result)
