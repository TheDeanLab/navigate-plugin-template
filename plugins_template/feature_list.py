from navigate.tools.decorators import FeatureList
from navigate.model.features.feature_related_functions import (
    ExampleFeature,
)


@FeatureList
def example_feature():
    return [
        {"name": ExampleFeature},
    ]
