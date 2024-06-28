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

### Prequisites

- just: [installation page](https://github.com/casey/just/releases)
- pnpm: [installation page](https://pnpm.io/installation)

```bash
just setup
```
