class Node:
    def __init__(self, name, next=None):
        self.name = name
        self.next = next

    def __str__(self):
        return str(self.name)


# 制作一个简单链表 #1->#2->#3->#4->#5
def create_simple() -> Node:
    node_list = [Node(i) for i in range(1, 6)]
    for i in range(0, 4):
        node_list[i].next = node_list[i + 1]
    return node_list[0]


# 制作一个指定数组链表
def create_complex(array: list) -> Node:
    node_list = [Node(i) for i in array]
    for i in range(0, len(array) - 1):
        node_list[i].next = node_list[i + 1]
    return node_list[0]


# 遍历一个链表输出到列表并打印输出
def print_linked_list(node):
    array = []
    node_temp = node
    while True:
        if not node_temp:
            break
        array.append(node_temp.name)
        node_temp = node_temp.next
    # print(array)
    return array


# 链表奇数在前
def extract_odd(node_root: Node) -> Node:
    array = []
    node = node_root
    while True:
        if not node:
            break
        array.append(node.name)
        node = node.next
    array_odd = [x for x in array if x % 2 == 1]
    array_even = [x for x in array if x % 2 == 0]
    array_odd.extend(array_even)
    node = create_complex(array_odd)
    return node


# 检查链表是否循环
def check_if_loop(node_root) -> bool:
    symbol = False
    array = []
    node = node_root
    while True:
        if not node:
            break
        if node.name in array:
            symbol = True
            break
        array.append(node.name)
        node = node.next
    return symbol


# 在循环开始时停止
def stop_at_loop(node_root) -> Node:
    symbol = False
    array = []
    node = node_root
    while True:
        if not node:
            break
        if node.name in array:
            symbol = True
            break
        array.append(node.name)
        node = node.next
    return node if symbol else None


if __name__ == '__main__':
    node_root = create_simple()
    node_odd_first = extract_odd(node_root)
    print(f"奇数在前的列表：{print_linked_list(node_odd_first)}")
    loop_list = create_complex([1, 2, 3, 1, 2, 3])
    symbol = check_if_loop(loop_list)
    print(f"创建循环链表：{print_linked_list(loop_list)},检测是否循环：{symbol}")
    node = stop_at_loop(loop_list)
    print(f"创建循环链表：{print_linked_list(loop_list)},循环截断之后的链表为：{print_linked_list(node)}")
