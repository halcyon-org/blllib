from datetime import datetime

import pytest

import blllib

check_start = False
check_update = False


class TestBllib:
    def test__use_case_create(self):

        def on_start(self: blllib.BLL):
            global check_start
            check_start = True

            self.entry()

        def on_update(self: blllib.BLL, data: list[str]):
            global check_update
            check_update = True

        bll = blllib.create(
            on_start=on_start,
            on_update=on_update,
            koyo_info=blllib.KoyoKoyoInfomation(
                koyo_id="test",
                koyo_name="test",
                koyo_description="test",
                need_external=[],
                koyo_params={},
                koyo_scales=[],
                koyo_data_ids=[],
                version="0.0.1",
                license="test",
                ext_licenses=[],
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
