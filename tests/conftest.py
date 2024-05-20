"""It defines useful pytest fixture for testing."""

import numpy as np
import pytest
from rasterio import Affine, MemoryFile


@pytest.fixture(name="default_testing_profile")
def fixture_default_testing_profile():
    """Default profile for testing. Check https://stackoverflow.com/a/57015304/2641038 to learn how
    to name fixture function properly."""
    return {
        "count": 1,
        "driver": "GTiff",
        "dtype": "float32",
        "nodata": -999999.0,
        "width": 20,
        "height": 20,
        "transform": Affine(1.0, 0.0, 0.0, 0.0, 1.0, 0.0),
        "tiled": True,
        "interleave": "band",
        "compress": "lzw",
        "blockxsize": 256,
        "blockysize": 256,
    }


@pytest.fixture()
def default_testing_dataset(default_testing_profile):
    """Default dataset for testing."""
    with MemoryFile() as memoryfile:
        with memoryfile.open(**default_testing_profile) as dataset:
            dataset.write(np.zeros((1, 20, 20)))
            yield dataset
