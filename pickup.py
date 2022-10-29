from typing import Optional, Iterable

from utils import filter_query, map_query, unique_query, sort_query, limit_query

FILE_NAME = 'data/apache_logs.txt'
CMD_TO_UTILS = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'sort': sort_query,
    'limit': limit_query,

}


def iter_file(file_name: str):
    with open(file_name) as file:
        for line in file:
            yield line


def query_builder(cmd, value, data: Optional[Iterable[str]]):
    if data is None:
        prepared_data = iter_file(FILE_NAME)
    else:
        prepared_data = data
    result = CMD_TO_UTILS[cmd](param=value, data=prepared_data)
    return list(result)
    # gen = iter_file(FILE_NAME)
    # filtered = list(filter_query(value, gen))
    # mapped = list(map_query('0', filtered))
    # unique = list(unique_query(mapped))
    # sort = list(sort_query(param='desc', data=unique))
    # limit = list(limit_query(param=2, data=sort))
    # return limit

    # while True:
    #
    #
    #     try:
    #         data = next(gen)
    #         print(data)
    #     except StopIteration:
    #         break

