#!/usr/bin/env python3


from binascii import hexlify, unhexlify

from colorama import Fore, Back


def _warning(message):
	print(f"{Fore.YELLOW}WARNING: {message}{Fore.RESET}")


def display_blocks(stream, block_size=16):
	if isinstance(stream, str):
		# check if it's an hexadecimal string
		stream = stream.strip()
		int(stream, 16)  # short way to check if the stream is hexadecimal
		if stream[0] == "-":
			_warning("There is a negative sign in front of the hex stream.")
		stream = stream.replace("0x", "").replace("0X", "").replace("-", "")
	elif isinstance(stream, bytes):
		pass
	elif isinstance(stream, bytearray):
		pass
	else:
		raise TypeError


def main():
	pass


if __name__ == '__main__':
	main()
