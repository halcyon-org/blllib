import algorithm_lib
from algorithm_lib import ApiException


class Test:
    def test__can_call(self):
        configuration = algorithm_lib.Configuration(host="http://localhost:4010")
        configuration.api_key["ApiKeyAuth"] = "TEST_API_KEY"

        with algorithm_lib.ApiClient(configuration) as api_client:
            api_instance = algorithm_lib.ServerApi(api_client)

            api_response = api_instance.status_get()
            print(api_response)
