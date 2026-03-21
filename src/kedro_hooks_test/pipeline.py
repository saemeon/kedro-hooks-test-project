import logging

from kedro.pipeline import Pipeline, node
from kedro_intercept import intercept_node

from .nodes import heavy_node, light_node, slow_node

log = logging.getLogger(__name__)


# --- global pipeline interceptors ---

def _on_pipeline_start(run_params: dict) -> None:
    log.info("[intercept] pipeline starting — run_id=%s", run_params.get("run_id"))


def _on_pipeline_end(run_params: dict) -> None:
    log.info("[intercept] pipeline finished — run_id=%s", run_params.get("run_id"))


intercept_node(before_pipeline_run=_on_pipeline_start)
intercept_node(after_pipeline_run=_on_pipeline_end)


# --- per-node interceptors ---

def _log_node_start(node) -> None:  # noqa: ANN001
    log.info("[intercept] starting node: %s", node.name)


def _log_node_end(node) -> None:  # noqa: ANN001
    log.info("[intercept] finished node: %s", node.name)


def _check_intermediate(dataset_name: str, data: object) -> None:
    """Validate that the intermediate dataset has a 'result' key."""
    if not isinstance(data, dict) or "result" not in data:
        raise ValueError(f"[intercept] {dataset_name!r} is missing 'result' key: {data!r}")
    log.info("[intercept] %r looks good — result=%s", dataset_name, data["result"])


def create_pipeline() -> Pipeline:
    light = node(light_node, inputs=None, outputs="intermediate", name="light_node")
    heavy = node(heavy_node, inputs="intermediate", outputs="final", name="heavy_node")
    slow = node(slow_node, inputs="final", outputs=None, name="slow_node")

    # node-level logging for every node
    for n in (light, heavy, slow):
        intercept_node(n, before_node_run=_log_node_start, after_node_run=_log_node_end)

    # dataset-level validation: check 'intermediate' after light_node saves it
    intercept_node(light, after_dataset_saved={"intermediate": _check_intermediate})

    return Pipeline([light, heavy, slow])
