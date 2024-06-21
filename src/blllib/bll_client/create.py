from typing import Callable

import blllib


def create(on_start: Callable, on_update: Callable[[list[str]], None], algo_info: blllib.AlgorithmAlgorithmInfomation):
    return blllib.BLL(on_start=on_start, on_update=on_update, algo_info=algo_info)
