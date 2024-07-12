from typing import Callable, Self

import openapi_client
from pydantic import StrictStr
import blllib.bll_client as blllib_client


def create(
    on_start: Callable[[], None],
    on_update: Callable[[list[StrictStr]], None],
    algo_info: openapi_client.AlgorithmAlgorithmInfomation,
):
    return blllib_client.BLL(on_start=on_start, on_update=on_update, algo_info=algo_info)
