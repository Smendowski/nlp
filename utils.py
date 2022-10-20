import os
import glob
from dataclasses import dataclass
from typing import Dict, List, Optional, Protocol

import pandas as pd

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BILLS_DIR = f"{ROOT_DIR}/bills"


@dataclass
class Bill:
    filename: str
    content: str


class BillProcessor(Protocol):
    @classmethod
    def process(self, content: str):
        ...


class CorpusProcessor:
    _bills: List[Bill]
    _processors: List[BillProcessor]

    def __init__(self, bills: List[Bill], processors: List[BillProcessor]):
        self._bills = bills
        self._processors = processors
        self._result = []

    def __call__(self) -> pd.DataFrame:
        for bill in self._bills:
            self._result.append([
                bill.filename,
                *[processor.process(bill.content) for processor in self._processors]
            ])

        return pd.DataFrame(self._result)


def load_bills(
    path: Optional[str] = BILLS_DIR,
    extension: Optional[str] = "txt"
) -> Dict[str, str]:
    paths: List[str] = glob.glob(f"{path}/*.{extension}")
    for file_path in paths:
        with open(file_path) as f:
            yield Bill(
                filename=file_path.split("/")[-1],
                content=f.read(),
            )
