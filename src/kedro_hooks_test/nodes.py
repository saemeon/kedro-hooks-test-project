import time


def light_node() -> dict:
    """Simulates a quick, light node."""
    time.sleep(2)
    return {"result": 42}


def heavy_node(data: dict) -> dict:
    """Simulates a memory-intensive node."""
    # Allocate ~50 MB to make RSS spike visible in telemetry
    blob = bytearray(50 * 1024 * 1024)
    time.sleep(3)
    del blob
    return {"result": data["result"] * 2}


def slow_node(data: dict) -> None:
    """Simulates a long-running node."""
    time.sleep(4)
