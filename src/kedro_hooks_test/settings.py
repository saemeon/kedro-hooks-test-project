import os

# i)  auto-discovery (default):  uv run kedro run
# ii) explicit setup:             KEDRO_HOOK_SETUP=explicit uv run kedro run

if os.environ.get("KEDRO_HOOK_SETUP") == "explicit":
    from kedro_psutil_telemetry import PipelinePsutilTelemetry, console_sink

    DISABLE_HOOKS_FOR_PLUGINS = ("kedro-psutil-telemetry",)
    HOOKS = (
        PipelinePsutilTelemetry(
            interval=2.0,
            prefix="my_pipeline",
            sink=console_sink,
        ),
    )
