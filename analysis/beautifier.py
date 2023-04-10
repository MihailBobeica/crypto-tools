#!/usr/bin/env python3


from binascii import hexlify, unhexlify

from colorama import Fore, Back


def _warning(message):
	print(f"{Fore.YELLOW}WARNING: {message}{Fore.RESET}")


def _print_property(name, value):
	print(f"{Fore.CYAN}{name}{Fore.RESET}\t{value}")


def display_blocks(stream, block_size=16):
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
	blocks = length // block_size
	_print_property("blocks", blocks)



def main():
	a = "-" + "ab" * 16 + "bc" * 15
	display_blocks(a)
	b = "ab" * 16 + "bc" * 16
	display_blocks(b)


if __name__ == '__main__':
	main()
