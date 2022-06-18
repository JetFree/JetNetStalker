class MyIterator:
    def __init__(self, iterator, event):
        self.iterator = iterator
        self.event = event

    def __iter__(self):
        return self

    def __next__(self):
        if self.event.is_set():
            raise StopIteration
        else:
            return next(self.iterator)
