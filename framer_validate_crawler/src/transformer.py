from dataclasses import dataclass
from typing import TypedDict


class FramerValidateInfo(TypedDict):
    framer_name: str
    foundation_name: str
    product_names: list[str] | str


@dataclass
class FrmaerValidatRowTransFormer:
    data: list[str]

    def to_dict(self) -> FramerValidateInfo:
        print(self.data)
        return {
            "framer_name": self.data[1],
            "foundation_name": self.data[2],
            "product_names": (
                list(self.data[3].split("、")) if len(self.data) == 4 else ""
            ),
        }
