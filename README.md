# Library for algorithm functions

## Getting started

### Generating openAPI schema

*This script will create a open_api dir in the repository root. Please be sure to run this in the root of the repository. You might need to install the `openapi-generator-cli` to make this work.*

```bash
openapi-generator-cli generate -i belifeline-schema/schema/\@typespec/openapi3/openapi.v0.7.2.yaml -g python -o openapi_client/
```

### Updating submodules

Updating the submoduless within the projects is highly recomendded before the begining of further development. Do the submodule update by runnign the following command in your repository root.

```bash
git submodule update --remote --recursive
```

### testing the API client

The API is now (05.07.2024) tested using pytest
just run the pytest in the directory of choise from the repository root.

Before running the tests. Make sure to have run the just setup succesfully to be sure that you have everything installed within your virtual environment 😀

```bash
pytest src/test/open_API/
```

> **_🚧Broken stuff?🚧_**
Please ask author of tests (walterairs)

### Prequisites

- just: [installation page](https://github.com/casey/just/releases)
- pnpm: [installation page](https://pnpm.io/installation)

```bash
just setup
```
