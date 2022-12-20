
import unittest
import itertools
from pprint import pprint

from chunklist import ChunkList

class TestChunkList(unittest.TestCase):
    def test_insert(self):
        expected = []
        cl = ChunkList(chunk_size=10)
        for i in range(20):
            cl.insert(0, i)
            expected.insert(0, i)

        for i in range(20, 40):
            cl.append(i)
            expected.append(i)

        for i in range(10):
            popped = cl.pop(13)
            popped_expected = expected.pop(13)

        flat_list = list(itertools.chain(*cl._data))
        self.assertEqual(flat_list, expected)


if __name__ == '__main__':
    unittest.main()
