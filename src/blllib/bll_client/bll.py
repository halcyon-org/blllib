from pydantic.dataclasses import dataclass
from pydantic import StrictStr
from typing import Callable, Self, Type
from enum import Enum

import urllib.parse
import openapi_client
import pprint


class EventTag(Enum):
    START = "start"
    UPDATE = "update"


@dataclass
class BLL:

    def __new__(
        self,
        on_start: Callable[[], None],
        on_update: Callable[[list[StrictStr]], None],
        algo_info: openapi_client.AlgorithmAlgorithmInfomation,
    ):
        self.on_start = on_start
        self.on_update = on_update
        self.algo_info = algo_info
        return super().__new__(self)

    def start(self, argv: list[StrictStr], api_key: StrictStr, host: StrictStr):
        if len(argv) != 1:
            raise ValueError("Expected exactly one argument")
        if api_key == "":
            raise ValueError("API key cannot be empty")

        self._configuration = openapi_client.Configuration(host=host)
        self._configuration.api_key["ApiKeyAuth"] = api_key
        if argv[0] == EventTag.START.value:
            self.on_start()
        elif argv[0] == EventTag.UPDATE.value:
            self.on_update([])

    def entry(self):
        with openapi_client.ApiClient(self._configuration) as api_client:
            openapi_client.AlgorithmAlgorithmInfomationCreateOrUpdate(
                api_client,
                algorithm_id=self.algo_info.algorithm_id,
                algorithm_name=self.algo_info.algorithm_name,
                algorithm_description=self.algo_info.algorithm_description,
                need_external=self.algo_info.need_external,
                algorithm_scales=self.algo_info.algorithm_scales,
                algorithm_data_ids=self.algo_info.algorithm_data_ids,
            )
