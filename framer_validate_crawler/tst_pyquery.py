from pyquery import PyQuery as pq
from dataclasses import dataclass
from typing import TypedDict

html_string = """
                <div class="table-list mb-3">
                        <div class="row list-body LCGD2-data-row" data-id="1">
                            <div class="cell td" data-title="序號">
                                1
                            </div>
                            <div class="cell td" data-title="農產品經營者名稱">
                                <a href="/Home/IndustryInfo?TillageID=1">虎寮潭茶園</a>
                            </div>
                            <div class="cell td" data-title="友善團體名稱">
                                財團法人慈心有機農業發展基金會
                            </div>
                            <div class="cell td" data-title="產品品項">
                                茶
                            </div>

                        </div>

                        <div class="row list-body LCGD2-data-row" data-id="2">
                            <div class="cell td" data-title="序號">
                                2
                            </div>
                            <div class="cell td" data-title="農產品經營者名稱">
                                <a href="/Home/IndustryInfo?TillageID=2">綠森林農場</a>
                            </div>
                            <div class="cell td" data-title="友善團體名稱">
                                財團法人慈心有機農業發展基金會
                            </div>
                            <div class="cell td" data-title="產品品項">
                                包葉菜、果菜、瓜菜、豆菜
                            </div>

                        </div>

                        <div class="row list-body LCGD2-data-row" data-id="3">
                            <div class="cell td" data-title="序號">
                                3
                            </div>
                            <div class="cell td" data-title="農產品經營者名稱">
                                <a href="/Home/IndustryInfo?TillageID=3">林惠妹</a>
                            </div>
                            <div class="cell td" data-title="友善團體名稱">
                                財團法人慈心有機農業發展基金會
                            </div>
                            <div class="cell td" data-title="產品品項">
                                包葉菜、短期葉菜、根莖菜、花菜、蕈菜、果菜、瓜菜、豆菜、大漿果、小漿果、柑桔、其他
                            </div>

                        </div>

                        <div class="row list-body LCGD2-data-row" data-id="4">
                            <div class="cell td" data-title="序號">
                                4
                            </div>
                            <div class="cell td" data-title="農產品經營者名稱">
                                <a href="/Home/IndustryInfo?TillageID=4">林賢欽</a>
                            </div>
                            <div class="cell td" data-title="友善團體名稱">
                                財團法人慈心有機農業發展基金會
                            </div>
                            <div class="cell td" data-title="產品品項">
                                包葉菜、短期葉菜、根莖菜、花菜、果菜、瓜菜、豆菜、大漿果、小漿果、核果、梨果、柑桔、其他
                            </div>

                        </div>

                        <div class="row list-body LCGD2-data-row" data-id="5">
                            <div class="cell td" data-title="序號">
                                5
                            </div>
                            <div class="cell td" data-title="農產品經營者名稱">
                                <a href="/Home/IndustryInfo?TillageID=5">溫忠榮</a>
                            </div>
                            <div class="cell td" data-title="友善團體名稱">
                                財團法人慈心有機農業發展基金會
                            </div>
                            <div class="cell td" data-title="產品品項">
                                雜糧、包葉菜、短期葉菜、根莖菜、花菜、蕈菜、果菜、瓜菜、豆菜、大漿果、其他
                            </div>

                        </div>
                </div>

"""


class FramerValidateInfo(TypedDict):
    id: str
    framer_name: str
    foundation_name: str
    product_names: list[str]


@dataclass
class RowTransFormer:
    data: list[str]

    def to_framer_validate_info(self) -> FramerValidateInfo:
        return {
            "id": self.data[0],
            "framer_name": self.data[1],
            "foundation_name": self.data[2],
            "product_names": list(self.data[3].split("、")),
        }


doc = pq(html_string)
elements = doc(".row.list-body.LCGD2-data-row")


framer_info: list[FramerValidateInfo] = [
    RowTransFormer(
        pq(element).text().split("\n")  # type: ignore
    ).to_framer_validate_info()
    for element in elements
]

print(framer_info)
