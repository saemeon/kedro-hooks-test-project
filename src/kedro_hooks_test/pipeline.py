from kedro.pipeline import Pipeline, node

from .nodes import heavy_node, light_node, slow_node


def create_pipeline() -> Pipeline:
    return Pipeline(
        [
            node(light_node, inputs=None, outputs="intermediate", name="light_node"),
            node(heavy_node, inputs="intermediate", outputs="final", name="heavy_node"),
            node(slow_node, inputs="final", outputs=None, name="slow_node"),
        ]
    )
