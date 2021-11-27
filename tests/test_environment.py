import pytest
import sys

from pathingSim.environment import Environment


@pytest.mark.parametrize("dimen", [
    (1.0, 1.0),
    (1, 1),
    (sys.float_info.max, sys.float_info.max),
    (sys.float_info.min, sys.float_info.min)
])
def test_empty_field(dimen):
    my_env = Environment(dimen, None)
    assert my_env is not None


@pytest.mark.parametrize("dimen, error", [
    (('x', 'y'), TypeError),
    ((1, 'y'), TypeError),
    (('x', 1), TypeError),
    ((0, 0), ValueError),
    ((1, 0), ValueError),
    ((0, 1), ValueError),
    ((-1, -1), ValueError),
    ((-1, 1), ValueError),
    ((1, -1), ValueError),
    ((-sys.float_info.min, -sys.float_info.min), ValueError),
    ((-sys.float_info.min, sys.float_info.min), ValueError),
    ((sys.float_info.min, -sys.float_info.min), ValueError),
    ((-sys.float_info.max, -sys.float_info.max), ValueError),
    ((-sys.float_info.max, sys.float_info.max), ValueError),
    ((sys.float_info.max, -sys.float_info.max), ValueError)
])
def test_field_errors(dimen, error):
    with pytest.raises(error):
        Environment(dimen, None)


def test_multidimension():
    dimen = (1, 1, 1)
    with pytest.warns(UserWarning):
        Environment(dimen, None)


def test_str_no_obstacles():
    dimen = (1, 1)
    EXPECTED_STR = f"Size: ({dimen[0]}, {dimen[1]}) with 0 obstacles"
    my_env = Environment(dimen, None)

    assert my_env.__str__ == EXPECTED_STR


def test_repr_no_obstacles():
    dimen = (1, 1)
    EXPECTED_REPR = f"Evironment({dimen[0]}, {dimen[1]}, None)"
    my_env = Environment(dimen, None)

    assert my_env.__repr__ == EXPECTED_REPR
