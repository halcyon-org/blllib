import pytest
from datetime import datetime

import blllib

check_start = False
check_update = False


class TestBllib:
    def test__use_case_create(self):

        def on_start(self):
            global check_start
            check_start = True

            self.entry()

        def on_update(self: blllib.BLL, data: list[str]):
            global check_update
            check_update = True

        bll = blllib.create(
            on_start=on_start,
            on_update=on_update,
            algo_info=blllib.AlgorithmAlgorithmInfomation(
                algorithm_id="test",
                algorithm_name="test",
                algorithm_description="test",
                need_external=[],
                algorithm_scales=[],
                algorithm_data_ids=[],
                first_entry_at=datetime.now(),
                last_entry_at=datetime.now(),
                last_updated_at=datetime.now(),
            ),
        )

        assert bll is not None

        bll.start([blllib.EventTag.START.value], "API_KEY", "http://localhost:4010")
        assert check_start is True

        bll.start([blllib.EventTag.UPDATE.value], "API_KEY", "http://localhost:4010")
        assert check_update is True
