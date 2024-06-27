import heapq


prefixes_dict = {}
sequence = input("Enter letter sequence: ")
pq = []
tree_pq = []
letter_occurrences = {}


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def join(s1, s2):
    return s1[0] + s2[0], str.join("", sorted(s1[1] + s2[1]))


def array_to_binary_tree(array):
    if not array:
        return None

    root = Node(array[len(array) - 1])
    queue = [root]
    front = 0
    index = len(array) - 2

    while index >= 0:
        node = queue[front]
        front += 1
        if len(node.value) == 1:
            continue

        node.right = Node(array[index])
        queue.append(node.right)
        index -= 1

        if index < 0:
            break

        node.left = Node(array[index])
        queue.append(node.left)
        index -= 1

    return root


def generate_prefixes(root: Node, curr_prefix=""):
    if not root:
        return None
    if len(root.value) == 1:
        prefixes_dict[root.value] = curr_prefix
        return None
    if root.left:
        generate_prefixes(root.left, curr_prefix + "0")
    if root.right:
        generate_prefixes(root.right, curr_prefix + "1")


if __name__ == "__main__":
    for letter in sequence:
        letter_occurrences[letter] = letter_occurrences.get(letter, 0) + 1

    for letter in letter_occurrences:
        heapq.heappush(pq, (letter_occurrences[letter], letter))

    nodes = []
    while len(pq) > 1:
        s1 = heapq.heappop(pq)
        s2 = heapq.heappop(pq)
        s_new = join(s1, s2)

        nodes.append(s1[1])
        nodes.append(s2[1])

        heapq.heappush(pq, s_new)

        heapq.heappush(tree_pq, s1)
        heapq.heappush(tree_pq, s2)
        heapq.heappush(tree_pq, s_new)

    nodes.append(heapq.heappop(pq)[1])

    root = array_to_binary_tree(nodes)
    generate_prefixes(root)

    print(prefixes_dict)

encoded_sequence = str.join("", [prefixes_dict[letter] for letter in sequence])
print("Encoded sequence: " + encoded_sequence)
