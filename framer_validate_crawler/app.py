from typing import Literal, Self

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pyquery import PyQuery as pq


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

    def wait_element_time(self, sec_time: int) -> Self:
        self.browser.implicitly_wait(sec_time)

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


if __name__ == "__main__":
    url = (
        "https://epv.afa.gov.tw/Home/FriendlyIndustryQuery?SearchByField=0&SearchByKeyWords=&CropCategory_Produce=13&SearchByCropCategoryIDs=&SearchByGroup=",
    )
    framer_validate_crawler = FramerValidateCrawler()
    elements: dict[str, WebElement] = (
        framer_validate_crawler.get(url[0])
        .wait_element_time(2)
        .find_element(By.ID, "navbarDropdown4", "click")
        .find_element(
            By.XPATH, "/html/body/header/div/nav/div/ul/li[9]/div/a[1]", "click"
        )
        .find_element(
            By.XPATH, "/html/body/main/div[2]/div/div[3]/div/div/select[1]", "click"
        )
        .find_element(
            By.XPATH,
            "/html/body/main/div[2]/div/div[3]/div/div/select[1]/option[5]",
            "click",
        )
        .wait_element_time(10)
        .find_element(
            By.XPATH,
            "/html/body/main/div[2]/div/div[2]/div/div[201]",
            "get_web_element",
            "element",
        )
        .find_element(
            By.XPATH,
            "/html/body/main/div[2]/div/div[3]/div/div",
            "get_web_element",
            "max_page",
        )
        .find_element(
            By.XPATH,
            "/html/body/main/div[2]/div/div[2]/div",
            "get_web_element",
            "framer_info_rows",
        )
    ).get_value()  # type: ignore

    print(elements)
    max_page_element = elements["max_page"].text
    framer_info_rows = elements["framer_info_rows"].get_attribute("outerHTML")
    print(
        max_page := int(
            extract_string(string=max_page_element, regex_string=r"第 \d+/(\d+) 頁")
        )
    )

    print(framer_info_rows)

    all_framer_info_rows = [
        {
            index: (
                framer_validate_crawler.wait_element_time(10)
                .find_element(
                    By.XPATH, "/html/body/main/div[2]/div/div[3]/div/div/a[2]", "click"
                )
                .wait_element_time(10)
                .find_element(
                    By.XPATH,
                    "/html/body/main/div[2]/div/div[2]/div",
                    "get_web_element",
                    "framer_info_rows",
                )
                .get_value("framer_info_rows")
                .get_attribute("outerHTML")  # type: ignore
            )
        }
        for index in range(2, max_page + 2, 1)
    ]

    print(len(all_framer_info_rows))
    print(all_framer_info_rows[-1])

# browser.get(url[0])
# evealed = browser.implicitly_wait(2)
# browser.find_element(By.ID, "navbarDropdown4").click()
# browser.find_element(
#     By.XPATH, "/html/body/header/div/nav/div/ul/li[9]/div/a[1]"
# ).click()
# browser.find_element(
#     By.XPATH, "/html/body/main/div[2]/div/div[3]/div/div/select[1]"
# ).click()# V
# browser.find_element(
#     By.XPATH, "/html/body/main/div[2]/div/div[3]/div/div/select[1]/option[5]"
# ).click()

# browser.implicitly_wait(10)
# element = browser.find_element(
#     By.XPATH, "/html/body/main/div[2]/div/div[2]/div/div[201]"
# )

# print(element.text)

# page = browser.find_element(By.XPATH, "/html/body/main/div[2]/div/div[3]/div/div").text


# # print(browser.page_source)  # 獲得page的html

# html_string = browser.page_source  # noqa: E999
