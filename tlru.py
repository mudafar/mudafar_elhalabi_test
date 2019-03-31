from time import time


class Node:
    def __init__(self, node_data=None, next_node=None, prev_node=None):
        self.next = next_node
        self.prev = prev_node
        self.data = node_data


class DataWithTimestamp:
    def __init__(self, key, value, time_to_expire=None):
        self.key = key
        self.value = value
        self.timestamp = time()
        self.__time_to_expire = time_to_expire

    def is_expired(self):
        try:
            return self.timestamp + self.__time_to_expire < time()
        except:
            return False

    def __str__(self):
        return str(self.value)


class DoublyLinkedList:
    def __init__(self):
        self.__head = Node()
        self.__tail = Node()
        self.__head.next = self.__tail
        self.__tail.prev = self.__head

    def push_node(self, node: Node):
        prev_node = self.__tail.prev
        prev_node.next = node
        node.prev = prev_node
        self.__tail.prev = node
        node.next = self.__tail

    @staticmethod
    def remove_node(node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def move_to_the_end(self, node: Node):
        self.remove_node(node)
        self.push_node(node)

    def remove_first(self):
        first_node = self.__head.next
        if first_node != self.__tail:
            self.remove_node(first_node)

            return first_node
        return None

    def __iter__(self):
        current = self.__head.next
        while current is not None and current != self.__tail:
            yield current
            current = current.next

    def __str__(self):
        list_str = 'head -> '
        for node in self:
            list_str += f'{node.data} -> '
        list_str += 'tail'

        return list_str


class TimeAwareLeastRecentlyUsed:
    """A time aware least recently used cache class.


    """

    def __init__(self, time_to_expire: float, max_size: int):
        """
        :param time_to_expire: time in seconds before an entry will expire.
        :param max_size: maximum size of the cache.

        :return: TimeAwareLeastRecentlyUsed instance.
        """
        self.__key_to_node_map = dict()
        self.__doubly_linked_list = DoublyLinkedList()
        self.__max_size = max_size
        self.__time_to_expire = time_to_expire

    def __mark_as_last_used(self, node):
        self.__doubly_linked_list.move_to_the_end(node)

    def __clean_any_expired_entries(self):
        for node in self.__doubly_linked_list:
            if node.data.is_expired():
                self.__doubly_linked_list.remove_node(node)
                del self.__key_to_node_map[node.data.key]

    def put(self, key, value):
        """
        Put/Insert a new value in the cache

        :param key: entry key
        :param value: value to be saved
        :return: None
        """

        self.__clean_any_expired_entries()

        # if entry already exist in the cache.
        if key in self.__key_to_node_map:
            # Update node data, this includes its timestamp
            node = self.__key_to_node_map[key]
            node.data = DataWithTimestamp(key, value, self.__time_to_expire)
            self.__mark_as_last_used(node)
        else:
            # No entry, create a new node and link it to the list and insert ot using the given key to the map.
            node = Node(DataWithTimestamp(key, value, self.__time_to_expire))
            self.__doubly_linked_list.push_node(node)
            self.__key_to_node_map[key] = node

            # If new map size exceed the max_size remove the least recently used entry
            if len(self.__key_to_node_map) > self.__max_size:
                removed_node = self.__doubly_linked_list.remove_first()
                if removed_node:
                    del self.__key_to_node_map[removed_node.data.key]

    def get(self, key):
        """
        Get a value from the cache if exist, else return None

        :param key: entry key
        :return: Value related with the given key else None.
        """
        self.__clean_any_expired_entries()

        if key in self.__key_to_node_map:
            node = self.__key_to_node_map[key]
            self.__mark_as_last_used(node)

            return node.data.value

        return None

    def __str__(self):
        return str(self.__doubly_linked_list)
