from pyquery import PyQuery as pq

from typing import Any, Callable


def get_html_element(html_string: str, context: str) -> pq:
    return pq(html_string)(context)


def extract_data_from_pq(
    elements: pq, transformer: type, func: Callable[[pq], Any]
) -> list[Any]:
    return [transformer(func(element)).to_dict() for element in elements]
