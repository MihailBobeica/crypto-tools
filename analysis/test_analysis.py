#!/usr/bin/env python3


import unittest

from beautifier import display_blocks


class TestDisplayBlocksFunction(unittest.TestCase):

	def test_stream_type(self):
		int_stream = [0] * 16
		with self.assertRaises(TypeError):
			display_blocks(int_stream)

		not_hex_stream = "gg" * 16
		with self.assertRaises(ValueError):
			display_blocks(not_hex_stream)


if __name__ == '__main__':
	unittest.main()
