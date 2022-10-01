import unittest

import os

from dryades.bimfile.bimfile import BeforeImageFile

fnam = "mytest.txt"
test_str = "hello world!"


class BimFileTestCase(unittest.TestCase):
    def setUp(self):
        with open(fnam, "wb") as fd:
            fd.write(test_str.encode())

    def tearDown(self):
        os.remove(fnam)

    def test_defaults(self):
        fs = os.stat(fnam)
        self.assertEqual(fs.st_size, len(test_str))

    def test_rollback(self):
        fd = BeforeImageFile(fnam, "r+b").open()

        fd.seek(0)
        greet_str = "salut"
        fd.write(greet_str.encode())

        fd.seek(0)
        read_str = fd.read(len(greet_str)).decode()
        self.assertEqual(greet_str, read_str)

        fd.rollback()

        fd.seek(0)
        read_str = fd.read().decode()
        self.assertEqual(test_str, read_str)

        fd.close()

    def test_commit(self):
        fd = BeforeImageFile(fnam, "r+b").open()

        fd.seek(0)
        greet_str = "salut"
        fd.write(greet_str.encode())

        fd.comit()

        fd.seek(0)
        read_str = fd.read().decode()
        self.assertEqual(read_str, "salut world!")

        fd.close()
