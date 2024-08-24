from typing import Sequence, Mapping, Any

def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access nested map with key path.
    Parameters
    ----------
    nested_map: Mapping
        A nested map
    path: Sequence
        a sequence of key representing a path to the value
    Example
    -------
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


nested_map = {"a": {"b": {"c": 1}}}
path = ["a", "b", "c"]
result = access_nested_map(nested_map, path)
print(f"Test Case 1: {result}")  # Expected output: 1

# Test Case 2: Path does not exist
nested_map = {"a": {"b": {"c": 1}}}
path = ["a", "b", "d"]
try:
	result = access_nested_map(nested_map, path)
except KeyError as e:
	print(f"Test Case 2: KeyError - {e}")  # Expected output: KeyError - 'd'


nested_map = {"a": {"b": {"c": 1}}}
path = ["a", "b", "c", "d"]
try:
	result = access_nested_map(nested_map, path)
except KeyError as e:
	print(f"Test Case 3: KeyError - {e}")  # Expected output: KeyError - 'd'

# Test Case 4: Empty path
nested_map = {"a": {"b": {"c": 1}}}
path = []
result = access_nested_map(nested_map, path)
print(f"Test Case 4: {result}")  # Expected output: {"a": {"b": {"c": 1}}}

