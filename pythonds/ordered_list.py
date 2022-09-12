from tkinter import CURRENT


class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def __str__(self):
        return str(self.data)


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def get_size(self):
        total = 0
        current = self.head
        while current:
            total += 1
            current = current.next
        return total

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f'Appended {item}.')

    def remove(self, item):
        item_found = False
        if self.head is None:
            raise Exception(f'Cannot remove {item} because the list is empty!')
        if self.head.get_data() == item:
            self.head = self.head.get_next()
            item_found = True
        else:
            prev = self.head
            current = self.head.next
            while current:
                if current.get_data() == item:
                    prev.next = current.next
                    item_found = True
                    break
                prev = current
                current = current.next
        if not item_found:
            raise Exception('Item not found in list!')
        print(f'Removed {item}.')

    def search(self, item):
        idx = 0
        item_found = False
        current = self.head
        while current:
            if current.get_data() == item:
                item_found = True
                break
            current = current.next
            idx += 1
        if item_found:
            print(f'{item} found at index {idx}.')
            return idx
        print(f'{item} was not found in the list.')
        return -1

    def insert(self, pos, item):
        new_node = Node(item)
        if pos == 0:
            new_node.set_next(self.head)
            self.head = new_node
        elif pos == self.get_size():
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            idx = 1
            prev = self.head
            current = self.head.next
            while current:
                if idx == pos:
                    prev.next = new_node
                    new_node.next = current
                    break
                idx += 1
                prev = current
                current = current.next
        print(f'Inserted {item} at index {pos}.')

    def pop(self, mute_output=False):
        popped_item = None
        if self.get_size() == 1:
            popped_item = self.head
            self.head = None
        else:
            prev = self.head
            current = self.head.next
            while current.next:
                prev = current
                current = current.next
            popped_item = current
            prev.next = None
        if not mute_output:
            print(f'Popped {popped_item}.')
        return popped_item

    
    def pop_at(self, pos):
        popped_item = None
        if pos == 0:
            popped_item = self.head
            self.head = self.head.next
        elif pos == self.get_size() - 1:
            popped_item = self.pop(mute_output=True)
        elif pos >= self.get_size():
            raise Exception('Cannot pop, provided index is greater than size of list!')
        else:
            idx = 1
            prev = self.head
            current = self.head.next
            while current:
                if idx == pos:
                    prev.next = current.next
                    popped_item = current
                    break
                idx += 1
                prev = current
                current = current.next
        print(f'Popped {popped_item} at index {pos}.')
        return popped_item
            

    def __str__(self):
        current = self.head
        list_of_nodes = []
        while current:
            list_of_nodes.append(current.get_data())
            current = current.next
        return ' -> '.join(map(lambda x: str(x), list_of_nodes))


ul = UnorderedList()
ul.append(0)
ul.append(1)
ul.append(3)
ul.append(5)
ul.append(7)
ul.append(9)
ul.append(11)
ul.append(13)
print(ul)
ul.remove(0)
ul.remove(13)
ul.remove(5)
print(ul)
ul.search(1)
ul.search(3)
ul.search(5)
ul.search(7)
ul.search(9)
ul.search(12)
ul.insert(0, 66)
ul.insert(3, 98)
ul.insert(7, 123)
print(ul)
print(ul.get_size())
ul.pop()
ul.pop()
print(ul)
ul.pop_at(0)
print(ul)
ul.pop_at(2)
print(ul)
ul.pop_at(3)
print(ul)