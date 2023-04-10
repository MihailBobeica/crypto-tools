#!/usr/bin/env python3


from binascii import hexlify, unhexlify
from math import ceil

from colorama import Fore, Back

from exception_analysis import ColsNotInRange


def _warning(message):
	print(f"{Fore.YELLOW}WARNING: {message}{Fore.RESET}")


def _print_property(name, value):
	print(f"{Fore.GREEN}{name}{Fore.RESET}\t{value}")


def display_blocks(stream, block_size=16, cols=2):
	print()
	print(f"{Back.MAGENTA}DISPLAY BLOCKS{Back.RESET}")
	if isinstance(stream, str):
		# check if it's an hexadecimal string
		stream = stream.strip().lower()
		int(stream, 16)  # short way to check if the stream is hexadecimal
		if stream[0] == "-":
			_warning("There is a negative sign in front of the hex stream.")
		stream = stream.replace("0x", "").replace("-", "")
	elif isinstance(stream, bytes):
		stream = hexlify(stream).decode()
	elif isinstance(stream, bytearray):
		stream = hexlify(stream).decode()
	else:
		raise TypeError
	hex_block_size = block_size * 2
	
	_print_property("size", block_size)
	length = len(stream) // 2
	_print_property("length", length)

	if t:=(length % block_size):
		_warning(f"Stream length is not divisible by the block size\n{length} % {block_size} = {t}")
	n = ceil(length / block_size)
	_print_property("blocks", n)

	blocks = [stream[i * hex_block_size: (i+1) * hex_block_size] for i in range(n)]

	match cols:
		case 1:
			for i, block in enumerate(blocks):
				if i % 2:
					print(f"{Fore.CYAN}{block}{Fore.RESET}", end="\t")
				else:
					print(block, end="\t")
				print()
		case 2:
			for i, block in enumerate(blocks):
				if ((i + 1) // 2) % 2:
					print(f"{Fore.CYAN}{block}{Fore.RESET}", end="\t")
				else:
					print(block, end="\t")
				if (i + 1) % 2 == 0:
					print()
		case 3:
			for i, block in enumerate(blocks):
				if i % 2:
					print(f"{Fore.CYAN}{block}{Fore.RESET}", end="\t")
				else:
					print(block, end="\t")
				if (i + 1) % 3 == 0:
					print()
		case _:
			raise ColsNotInRange()

	print()



def main():
	a = "-" + "ab" * 16 + "bc" * 15 + "ab" * 16 + "bc" * 15 + "ab" * 16 + "bc" * 15 + "12" * 64
	display_blocks(a, cols=1)
	b = "ab" * 16 + "bc" * 16
	display_blocks(b)
	c = "00" * 64
	display_blocks(c)


if __name__ == '__main__':
	main()
