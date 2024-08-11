from typing import Callable, Self

from pydantic import StrictStr

import blllib.bll_client as blllib_client
import openapi_client


def create(
    on_start: Callable[[blllib_client.BLL], None],
    on_update: Callable[[blllib_client.BLL, list[StrictStr]], None],
    koyo_info: openapi_client.KoyoKoyoInfomation,
):
    return blllib_client.BLL(on_start=on_start, on_update=on_update, koyo_info=koyo_info)
