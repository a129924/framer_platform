from src.framer_validate_crawler import (
    FramerValidateCrawler,
    extract_string,
    WebElement,
    By,
)
from src.tools import get_html_element, extract_data_from_pq, pq
from src.collections import unpack
from src.transformer import FrmaerValidatRowTransFormer, FramerValidateInfo


def output_json_file(obj: list | dict, output_path: str, indent: int = 4) -> None:
    from json import dumps

    with open(output_path, "w+", encoding="UTF-8") as json_file:
        json_file.writelines(dumps(obj, ensure_ascii=False, indent=indent))


def job(html_string: str, context: str) -> list[FramerValidateInfo]:
    elements = get_html_element(html_string, context)

    return extract_data_from_pq(
        elements,
        FrmaerValidatRowTransFormer,
        lambda element: pq(element).text().split("\n"),  # type: ignore
    )


url = (
    "https://epv.afa.gov.tw/Home/FriendlyIndustryQuery?SearchByField=0&SearchByKeyWords=&CropCategory_Produce=13&SearchByCropCategoryIDs=&SearchByGroup=",
)

framer_validate_crawler = FramerValidateCrawler()
elements: dict[str, WebElement] = (
    framer_validate_crawler.get(url[0])
    .implicitly_wait(20)
    .find_element(By.ID, "navbarDropdown4", "click")  # 點選語系
    .find_element(
        By.XPATH, "/html/body/header/div/nav/div/ul/li[9]/div/a[1]", "click"
    )  # 選擇語系
    .find_element(
        By.XPATH, "/html/body/main/div[2]/div/div[3]/div/div/select[1]", "click"
    )  # 點每頁 {page} 筆
    .find_element(
        By.XPATH,
        "/html/body/main/div[2]/div/div[3]/div/div/select[1]/option[5]",
        "click",
    )
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

max_page_element = elements["max_page"].text
framer_info_rows = elements["framer_info_rows"].get_attribute("outerHTML")

max_page = int(extract_string(string=max_page_element, regex_string=r"第 \d+/(\d+) 頁"))

next_page = "/html/body/main/div[2]/div/div[3]/div/div/a[2]"
all_framer_info_rows = unpack(
    [
        job(
            html_string=(
                framer_validate_crawler.wait_element_time(
                    sec_time=60,
                    wait_element_info={
                        "by": By.XPATH,
                        "context": "/html/body/main/div[2]/div/div[3]/div/div",
                        "pattern_string": f"第 {index}/22 頁，",
                    },
                )
                .find_element(
                    By.XPATH,
                    "/html/body/main/div[2]/div/div[2]/div",  # 每一頁農夫驗證資訊
                    "get_web_element",
                    "framer_info_rows",
                )
                .find_element(By.XPATH, next_page, "click")
                .get_value("framer_info_rows")
                .get_attribute("outerHTML")  # type: ignore
            ),
            context=".row.list-body.LCGD2-data-row",
        )
        for index in range(1, max_page + 1, 1)
    ]
)

framer_validate_crawler.browser.quit()
print(len(all_framer_info_rows))  # 4345

output_json_file(all_framer_info_rows, "./framer_validate_info.json")
