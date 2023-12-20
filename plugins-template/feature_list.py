from navigate.tools.decorators import FeatureList
from navigate.plugins.plugin_name.model.features.example_feature import (
    ExampleFeature,
)


@FeatureList
def example_feature():
    return [
        {"name": ExampleFeature},
    ]