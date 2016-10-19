class StackError(Exception):
    pass

class MyStack(object):
    
    def __init__(self, sequence=None, max_size=-1):
        self.stack = list(sequence) if sequence else list()
        self.MAX_LIMIT = max_size if max_size > 0 and max_size != -1 else None 

    def push(self, item):
        if self.MAX_LIMIT and len(self.stack) >= self.MAX_LIMIT:
            raise StackError('Stack is Full')
        self.stack.append(item)

    def push_many(self, sequence):
        if self.MAX_LIMIT:
            if len(self.stack) + len(sequence) >= self.MAX_LIMIT:
                raise StackError('Sequence cannot be fit in Stack, will overflow, Maximum limit is {}.'.format(self.MAX_LIMIT))
        [self.push(item) for item in sequence]

    def pop(self):
        if self.stack:
            return self.stack.pop()
        raise StackError('Stack is Empty')

    def pop_many(self, count):
        if len(self.stack[-count:]) >= count:
            return [self.stack.pop() for _ in xrange(count)]
        raise StackError('Stack does not have sufficient items to pop')

    def top(self):
        if self.stack:
            return self.stack[-1]
        raise StackError('Stack is Empty')

    def as_tuple(self):
        return tuple(self.stack)

    def as_dict(self):
        return {key: value for key, value in enumerate(self.stack)}

    def clear(self):
        self.stack = list()

    def resize(self, limit_by):
        self.MAX_LIMIT = limit_by
    
a = MyStack()
b = MyStack([1,2,3])

#a.top()
print b.stack
print b.top()
print b.pop()
print b.stack
print b.top()
#print b.pop_many(2)
b.push(20000)
print b.stack
b.push_many([4,6,7,8,8])
print b.stack
print b.as_dict()
print b.as_tuple()
b.clear()
print b.stack
b.push_many([4,6,7,8,8])
print b.stack
