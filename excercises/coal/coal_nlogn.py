class SegmentTree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size <<= 1
        self.tree = [0] * (2 * self.size)
    
    def update(self, i, val):
        i += self.size
        self.tree[i] = val
        i //= 2
        while i > 0:
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])
            i //= 2
    
    def query(self, transport, idx=1, left=0, right=None):
        if right is None:
            right = self.size
        if self.tree[idx] < transport:
            return -1
        if right - left == 1:
            return left
        mid = (left + right) // 2
        res = self.query(transport, 2*idx, left, mid)
        if res == -1:
            res = self.query(transport, 2*idx+1, mid, right)
        return res


def coal(A, T):
    n = len(A)
    wolne = []
    tree = SegmentTree(n)

    last = 0
    for i, transport in enumerate(A):
        if len(wolne) == 0:
            # pierwszy magazyn
            wolne.append(T - transport)
            tree.update(0, wolne[0])
            last = 0
            continue
        
        idx = tree.query(transport)
        if idx == -1 or idx >= len(wolne):
            # nowy magazyn
            wolne.append(T - transport)
            tree.update(len(wolne)-1, wolne[-1])
            last = len(wolne)-1
        else:
            wolne[idx] -= transport
            tree.update(idx, wolne[idx])
            last = idx

    return last


from egz2atesty import runtests
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
