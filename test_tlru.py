import unittest
from time import sleep

from tlru import DoublyLinkedList, Node, TimeAwareLeastRecentlyUsed


class TestDoublyLinkedList(unittest.TestCase):

    def test_instantiate(self):
        """ It should instantiate without exceptions"""
        try:
            DoublyLinkedList()
        except Exception as e:
            self.fail(e)

    def test_initial_nodes(self):
        """ It should create and wire head and tails correctly"""
        __list = DoublyLinkedList()
        head = __list._DoublyLinkedList__head
        tail = __list._DoublyLinkedList__tail

        self.assertEqual(head.next, tail)
        self.assertEqual(tail.prev, head)

    def test_push_node(self):
        """ It should push a new element"""
        __list = DoublyLinkedList()
        node = Node(1)
        __list.push_node(node)

        self.assertEqual(__list._DoublyLinkedList__head.next.data, 1)
        self.assertEqual(__list._DoublyLinkedList__tail.prev.data, 1)

    def test_remove_node(self):
        """ It should remove node"""
        __list = DoublyLinkedList()
        node = Node(1)
        __list.push_node(node)
        __list.remove_node(node)

        self.assertEqual(__list._DoublyLinkedList__head.next, __list._DoublyLinkedList__tail)
        self.assertEqual(__list._DoublyLinkedList__tail.prev, __list._DoublyLinkedList__head)

    def test_remove_first(self):
        """ It should remove first node """
        __list = DoublyLinkedList()
        node_1 = Node(1)
        node_2 = Node(2)

        __list.push_node(node_1)
        __list.push_node(node_2)
        removed_node = __list.remove_first()

        self.assertEqual(removed_node, node_1)
        self.assertEqual(__list._DoublyLinkedList__head.next, node_2)

    def test_iterator(self):
        # TODO
        pass

    def test_str(self):
        # TODO
        pass


class TestTimeAwareLeastRecentlyUsed(unittest.TestCase):
    def test_instantiate(self):
        """ It should instantiate without exceptions"""
        try:
            TimeAwareLeastRecentlyUsed(time_to_expire=100, max_size=3)
        except Exception as e:
            self.fail(e)

    def test_instantiate_without_params(self):
        """ It should fail without time_to_expire and/or max_size params"""
        with self.assertRaises(TypeError):
            TimeAwareLeastRecentlyUsed()

    def test_put(self):
        """ It should put new key value correctly"""
        tlru = TimeAwareLeastRecentlyUsed(time_to_expire=100, max_size=3)
        tlru.put(1, 'one')

        self.assertEqual(tlru._TimeAwareLeastRecentlyUsed__key_to_node_map[1].data.value, 'one')
        self.assertEqual(tlru._TimeAwareLeastRecentlyUsed__doubly_linked_list._DoublyLinkedList__head.next.data.value,
                         'one')

    def test_get(self):
        """ It should get value using the corresponding key correctly"""
        tlru = TimeAwareLeastRecentlyUsed(time_to_expire=100, max_size=3)
        tlru.put(1, 'one')

        value = tlru.get(1)
        self.assertEqual(value, 'one')

    def test_max_size(self):
        """ Internal doubled list and dict must not exceed the given max_size"""
        # TODO insert more elements than the max_size and verify the dict and list len
        pass

    def test_lru(self):
        """ It should follow least recently used algorithm"""
        tlru = TimeAwareLeastRecentlyUsed(time_to_expire=100, max_size=3)

        tlru.put(1, 'one')
        tlru.put(2, 'two')
        tlru.put(3, 'three')
        tlru.put(4, 'four')
        self.assertEqual(tlru._TimeAwareLeastRecentlyUsed__doubly_linked_list._DoublyLinkedList__head.next.data.value,
                         'two')
        self.assertEqual(tlru._TimeAwareLeastRecentlyUsed__doubly_linked_list._DoublyLinkedList__tail.prev.data.value,
                         'four')

    def test_tlru(self):
        """ It should follow time aware least recently used algorithm"""
        tlru = TimeAwareLeastRecentlyUsed(time_to_expire=0.2, max_size=3)

        tlru.put(1, 'one')
        tlru.put(2, 'two')
        tlru.put(3, 'three')

        self.assertEqual(tlru.get(1), 'one')

        sleep(0.2)
        self.assertIsNone(tlru.get(1))

    def test_str(self):
        # TODO
        pass