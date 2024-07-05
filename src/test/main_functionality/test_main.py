import unittest

import blllib
from blllib import ApiException


class TestMain(unittest.TestCase):
    def test__can_call(self):
        configuration = blllib.Configuration(host="http://localhost:4010")
        configuration.api_key["ApiKeyAuth"] = "TEST_API_KEY"

        with blllib.ApiClient(configuration) as api_client:
            api_instance = blllib.ServerApi(api_client)

            api_response = api_instance.status_get()
            print(api_response)


if __name__ == "__main__":
    unittest.main()
