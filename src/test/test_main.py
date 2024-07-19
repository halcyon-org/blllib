import blllib


class TestOpenApiClient:
    def test__can_call_client(self):
        configuration = blllib.Configuration(host="http://localhost:4010")
        configuration.api_key["ApiKeyAuth"] = "TEST_API_KEY"

        with blllib.ApiClient(configuration) as api_client:
            api_instance = blllib.ServerApi(api_client)

            api_response = api_instance.status_get()
            print(api_response)

    def test__can_call_create_client(self):
        bll = blllib.create(on_start=None, on_update=None, algo_info=None)
        print(bll)
