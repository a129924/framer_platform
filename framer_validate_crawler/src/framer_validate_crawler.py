from typing import Literal, Self, TypedDict

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By  # noqa: F401
from selenium.webdriver.remote.webelement import WebElement


class WaitElementIfno(TypedDict):
    by: str
    context: str
    pattern_string: str


def output_html_file(html_string: str) -> None:
    with open(
        "./framer_validate_crawler/framer_info.html", "w+", encoding="UTF-8"
    ) as html:
        html.writelines(html_string)


def extract_string(
    string: str,
    regex_string: str,
) -> str:
    from re import search

    if match_string := search(regex_string, string):
        return match_string.group(1)

    return ""


class FramerValidateCrawler:
    def __init__(self, brower: WebDriver = webdriver.Firefox()):
        self.browser: WebDriver = brower
        self._value: dict[str, WebElement] = {}

    def get(self, url: str) -> Self:
        self.browser.get(url)

        return self

    def implicitly_wait(self, sec_time: int) -> Self:
        self.browser.implicitly_wait(sec_time)

        return self

    def wait_element_time(
        self, sec_time: int, wait_element_info: WaitElementIfno
    ) -> Self:
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support.expected_conditions import (
            text_to_be_present_in_element,
        )

        wait = WebDriverWait(self.browser, sec_time)
        wait.until(
            text_to_be_present_in_element(
                locator=(wait_element_info["by"], wait_element_info["context"]),
                text_=wait_element_info["pattern_string"],
            )
        )

        return self

    def find_element(
        self,
        selector: str,
        web_element: str,
        action: Literal["click", "clear", "get_web_element"],
        get_value_key: str | None = None,
    ) -> Self:
        match (action):
            case "click":
                print(web_element)
                self.browser.find_element(selector, web_element).click()
                return self

            case "clear":
                self.browser.find_element(selector, web_element).clear()
                return self

            case "get_web_element":
                return self.get_web_element(
                    get_value_key if get_value_key else selector,
                    (self.browser.find_element(selector, web_element), self),
                )

            case _:
                raise KeyError(f"the to_do key : '{action}' is not found!")

    def get_web_element(
        self, key: str, find_element_function: tuple[WebElement, Self]
    ) -> Self:
        self._value[key] = find_element_function[0]

        return find_element_function[1]

    def get_value(self, key: str | None = None) -> WebElement | dict[str, WebElement]:
        if key is None:
            return self._value
        elif key not in self._value:
            raise KeyError(f"The key '{key}' is not found")
        else:
            return self._value[key]
