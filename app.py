import datetime
import hashlib
from binascii import unhexlify, hexlify


class Block:
	def __init__(self, prev_hash, transaction, amount):
		self.next = None
		self.__data = {
			"prev_hash": prev_hash,
			"transaction": transaction,
			"amount": amount,
			"hash": "",
			"time": datetime.datetime.now().time()
		}
		self.__data["hash"] = self.make_hash()

	def get_data(self):
		return self.__data

	def make_hash(self):
		test_hash = hexlify(hashlib.sha256(unhexlify(self.get_data()["prev_hash"])).digest()).decode("utf-8")
		while test_hash[:5] != "00000":
			test_hash = hexlify(hashlib.sha256(unhexlify(test_hash)).digest()).decode("utf-8")
		return test_hash

	def append(self, transaction, amount):
		n = self
		while n.next:
			n = n.next
		prev_hash = n.get_data()["hash"]
		end = Block(prev_hash, transaction, amount)
		n.next = end


def print_blocks(block):
	node = block
	print(node.get_data())
	while node.next:
		node = node.next
		print(node.get_data())

test_block = Block("0000007464674764764476476476476123", "Ivan", 100)
test_block.append("Boris", 1042)
test_block.append("Mary", 42)
print_blocks(test_block)