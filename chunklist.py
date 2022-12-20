


class ChunkList:

    _data = [[]]
    _length = 0

    def __init__(self, chunk_size=10000):
        self._chunk_size = chunk_size

    def __len__(self):
        return self._length

    def __str__(self):
        return str(self._data)

    def insert(self, insert_index, item):
        assert insert_index <= self._length

        chunk_start = 0
        chunks_index = 0
        chunks_length = len(self._data[0])
        while chunks_length < insert_index:
            chunk_start = chunks_length
            chunks_index += 1
            chunks_length += len(self._data[chunks_index])

        self._data[chunks_index].insert(insert_index-chunk_start, item)

        if len(self._data[chunks_index]) > self._chunk_size:
            mid_point = self._chunk_size // 2
            new_chunk = self._data[chunks_index][mid_point:]
            self._data.insert(chunks_index+1, new_chunk)
            del self._data[chunks_index][mid_point:]

        self._length += 1

    def append(self, item):
        self.insert(self._length, item)

    def pop(self, pop_index):
        assert pop_index <= self._length

        chunk_start = 0
        chunks_index = 0
        chunks_length = len(self._data[0])
        while chunks_length <= pop_index:
            chunk_start = chunks_length
            chunks_index += 1
            chunks_length += len(self._data[chunks_index])

        self._length -= 1
        popped = self._data[chunks_index].pop(pop_index-chunk_start)
        if len(self._data[chunks_index]) == 0:
            del self._data[chunks_index]
        return popped

