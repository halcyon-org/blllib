from pydantic.dataclasses import dataclass, StrictStr
from typing import Callable
from enum import Enum

import blllib


class EventTag(Enum):
    START = "start"
    UPDATE = "update"


@dataclass
class BLL:

    def __init__(
        self,
        on_start: Callable,
        on_update: Callable[[list[StrictStr]], None],
        algo_info: blllib.AlgorithmAlgorithmInfomation,
    ):
        self.on_start = on_start
        self.on_update = on_update
        self.algo_info = algo_info

    def start(self, argv: list[str]):
        if len(argv) != 1:
            raise ValueError("Expected exactly one argument")

        if argv[0] == EventTag.START.value:
            self.on_start()
        elif argv[0] == EventTag.UPDATE.value:
            self.on_update()

    def entry(self):
        blllib.AlgorithmAlgorithmInfomationCreateOrUpdate(
            algorithm_id=self.algo_info.algorithm_id,
            algorithm_name=self.algo_info.algorithm_name,
            algorithm_description=self.algo_info.algorithm_description,
            need_external=self.algo_info.need_external,
            algorithm_scales=self.algo_info.algorithm_scales,
            algorithm_data_ids=self.algo_info.algorithm_data_ids,
        )
