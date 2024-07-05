# Library for algorithm functions

## Getting started

### Generating openAPI schema

```bash
openapi-generator-cli generate -i belifeline-schema/schema/\@typespec/openapi3/openapi.v0.6.0.yaml -g python -o openapi_client/
```

### Updating submodules

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
