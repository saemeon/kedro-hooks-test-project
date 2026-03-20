# kedro-hooks-test-project

Test project for [kedro-psutil-telemetry](https://github.com/saemeon/kedro-psutil-telemetry).

Runs a dummy three-node Kedro pipeline to verify that the hook is auto-discovered via entry points and that telemetry output appears correctly.

## Setup

```bash
uv sync
```

## Run

```bash
uv run kedro run
```

You should see per-node telemetry samples (RSS, CPU, disk I/O, network) in the log, and a peak summary at the end.

## License

MIT
