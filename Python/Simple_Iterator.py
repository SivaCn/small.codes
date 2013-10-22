# Simple Iterator


class MyIter(object):
    def __init__(self, val):
        self.val = val

    def __iter__(self):
        return self

    def next(self):
        if self.val >= 5:
            raise StopIteration
        self.val += 1
        return self.val

print list(MyIter(0))
