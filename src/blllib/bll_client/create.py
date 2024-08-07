from typing import Callable, Self

from pydantic import StrictStr

import blllib.bll_client as blllib_client
import openapi_client


def create(
    on_start: Callable[[blllib_client.BLL], None],
    on_update: Callable[[blllib_client.BLL, list[StrictStr]], None],
    algo_info: openapi_client.AlgorithmAlgorithmInfomation,
):
    return blllib_client.BLL(on_start=on_start, on_update=on_update, algo_info=algo_info)
