from dataclasses import dataclass, field
from typing import List


@dataclass
class News:
    headline: str
    text: str
    most_common: List[str] = field(init=False)

    def __str__(self):
        return f'''\
{self.headline}:
{" ".join(self.most_common)}'''
