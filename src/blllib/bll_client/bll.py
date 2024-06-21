from pydantic.dataclasses import dataclass, StrictStr
from typing import Callable

import blllib


class BLL:

    def __init__(
        self, on_start: Callable, on_update: Callable[[list[str]], None], algo_info: blllib.AlgorithmAlgorithmData
    ):
        self.on_start = on_start
        self.on_update = on_update
        self.algo_info = algo_info
