def prime_generator(n):
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i

class CycleIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.iterable) - 1:
            self.index = 0
        result = self.iterable[self.index]
        self.index += 1
        return result
