# kedro-hooks-test-project

Test project for [kedro-psutil-telemetry](https://github.com/saemeon/kedro-psutil-telemetry).

Demonstrates two hook setup modes for a dummy three-node pipeline.

## Setup

```bash
uv sync
```

## Run

### Auto-discovery (default) — hook registered via entry point, no `settings.py` changes needed

```bash
uv run kedro run
```

### Explicit setup — hook manually instantiated with custom `interval`, `prefix`, and `sink`

```bash
KEDRO_HOOK_SETUP=explicit uv run kedro run
```

## License

MIT
