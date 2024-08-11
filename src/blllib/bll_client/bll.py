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
        koyo_info: openapi_client.KoyoKoyoInfomation,
    ):
        self.on_start = on_start
        self.on_update = on_update
        self.koyo_info = koyo_info
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
            api_instance = openapi_client.KoyoApi(api_client)
            request = openapi_client.EachKoyoUpdateRequest(
                update_koyo=openapi_client.KoyoKoyoInfomationCreateOrUpdate(
                    koyo_id=self.koyo_info.koyo_id,
                    koyo_name=self.koyo_info.koyo_name,
                    koyo_description=self.koyo_info.koyo_description,
                    need_external=self.koyo_info.need_external,
                    koyo_params=self.koyo_info.koyo_params,
                    koyo_scales=self.koyo_info.koyo_scales,
                    koyo_data_ids=self.koyo_info.koyo_data_ids,
                    version=self.koyo_info.version,
                    license=self.koyo_info.license,
                    ext_licenses=self.koyo_info.ext_licenses,
                )
            )
            import pprint

            pprint.pprint(request)

            try:
                api_response = api_instance.each_koyo_update(
                    koyo_id=self.koyo_info.koyo_id, each_koyo_update_request=request
                )
                return api_response
            except openapi_client.ApiException as e:
                print(f"Exception when calling KoyoApi: {e}")
