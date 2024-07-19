import pprint
import urllib.parse
from enum import Enum
from typing import Callable, Self, Type

from pydantic import StrictStr
from pydantic.dataclasses import dataclass

import blllib.bll_client as blllib_client
import openapi_client


class EventTag(Enum):
    START = "start"
    UPDATE = "update"


@dataclass
class BLL:

    def __new__(
        self,
        on_start: Callable[[Self], None],
        on_update: Callable[[Self, list[StrictStr]], None],
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
            self.on_start()  # type: ignore
        elif argv[0] == EventTag.UPDATE.value:
            self.on_update([])  # type: ignore

    def entry(self):
        with openapi_client.ApiClient(self._configuration) as api_client:
            api_instance = openapi_client.AlgorithmApi(api_client)
            request = openapi_client.EachAlgorithmUpdateRequest(
                update_algorithm=openapi_client.AlgorithmAlgorithmInfomationCreateOrUpdate(
                    algorithm_id=self.algo_info.algorithm_id,
                    algorithm_name=self.algo_info.algorithm_name,
                    algorithm_description=self.algo_info.algorithm_description,
                    need_external=self.algo_info.need_external,
                    algorithm_scales=self.algo_info.algorithm_scales,
                    algorithm_data_ids=self.algo_info.algorithm_data_ids,
                )
            )
            import pprint

            pprint.pprint(request)

            try:
                api_response = api_instance.each_algorithm_update(
                    algorithm_id=self.algo_info.algorithm_id, each_algorithm_update_request=request
                )
                return api_response
            except openapi_client.ApiException as e:
                print(f"Exception when calling AlgorithmApi: {e}")
