from assert_linked_list import assert_linked_list_values


class Node:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.next = None


def test_assert_linked_list_values() -> None:
    li = Node(0)
    li.next = Node(1)
    li.next.next = Node(2)
    li.next.next.next = Node(3)
    assert_linked_list_values(li, [0, 1, 2, 3])
