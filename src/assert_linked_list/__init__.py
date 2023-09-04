from typing import Any


# TODO(cnpryer):
#   * Abstraction for linked list type/interface (Node)
#   * Assert vs just eval bool?
#   * `assert True`?
#   * If `assert` should I raise?
def assert_linked_list_values(root: Any, values: list[Any]) -> bool:
    """Assert that for each node's value in a linked list (starting at some `root`
    node) is equal to and of the same order for each value provided in `values`.
    """
    node = root
    for val in values:
        assert node, None
        assert node.val == val, f"node.val={node.val},val={val}"
        node = node.next
    assert True
