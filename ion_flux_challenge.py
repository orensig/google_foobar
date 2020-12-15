import random

class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        return


    def insert(self, data):
        # print(f"{data}\n")
        _current_element = data.pop()
        self.data = _current_element
        if len(data) == 0:
            return
        idx2dissect = int(len(data)/2)-1
        left_data = data[:idx2dissect+1]
        right_data = data[idx2dissect+1:]
        self.right = Node()
        self.right.insert(right_data)
        self.left = Node()
        self.left.insert(left_data)
        return


    def find_parent(self, _num):
        if self.left is None and self.right is None:
            return -1
        if self.left.data == _num or self.right.data == _num:
            return self.data
        left_ans = self.left.find_parent(_num)
        right_ans = self.right.find_parent(_num)
        if left_ans != -1:
            return left_ans
        return right_ans


    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)


    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def solution(h, q):
    if (not isinstance(h,int) or h < 1 or h > 30
            or not isinstance(q,list) or len(q) < 1 or len(set(q)) > 1000
            or min(set(q)) < 1 or max(set(q)) > ((2**h) - 1)):
        raise Exception("One of the parameters: h and q (or both) is malformed")
    ordered_list_h = list(range(1, 2**h))
    perfect_tree = Node()
    perfect_tree.insert(data=ordered_list_h)
    res = []
    for _item in q:
        res.append(perfect_tree.find_parent(_num=_item))
    return res


if __name__ == '__main__':
    h1 = 10
    # q1 = [1,4,16,15,20]
    q1 = [random.randrange(1,3) for i in range(2000)]
    print(len(set(q1)))
    sol = solution(h=h1,q=q1)
    print(sol)
