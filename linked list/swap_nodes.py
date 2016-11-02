"""
Swap nodes in a linked list without swapping data
Given a linked list and two keys in it, swap nodes for two given keys. Nodes should be swapped by changing links. Swapping data of nodes may be expensive in many situations when data contains many fields. 

It may be assumed that all keys in linked list are distinct.

Examples:

Input:  10->15->12->13->20->14,  x = 12, y = 20
Output: 10->15->20->13->12->14

Input:  10->15->12->13->20->14,  x = 10, y = 20
Output: 20->15->12->13->10->14

Input:  10->15->12->13->20->14,  x = 12, y = 13
Output: 10->15->13->12->20->14
"""


class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None

	def print_list(self):
		node = self.head
		while(node):
			print node.data
			node = node.next
	
	def push(self, node):
		node.next = self.head
		self.head = node

	def swap_nodes_normal_case(self, key1, key2):
		# find the nodes, their next and prev
		prev1 = None
		prev2 = None
		temp = self.head
		while(temp.next):
			if (temp.next.data == key1):
				prev1 = temp
			if (temp.next.data == key2):
				prev2 = temp
			if prev1 is not None and prev2 is not None:
				break
			temp = temp.next
		
		node1 = prev1.next
		node2 = prev2.next

		if node1 and node2:

			next1 = prev1.next.next
			next2 = prev2.next.next

			prev1.next = node2
			node2.next = next1

			node1.next = next2
			prev2.next = node1

	def swap_nodes_generic(self, key1, key2):
		# if both the nodes are the same then do nothing
		# find the position of both the nodes
		if key1 == key2:
			return

		pos1 = self.head
		prev1 = None
		prev2 = None
		while(pos1 and pos1.data!=key1):
			prev1 = pos1
			pos1 = pos1.next

		pos2 = self.head
		while(pos2 and pos2.data!=key2):
			prev2 = pos2
			pos2 = pos2.next
		
		if not (pos1 and pos2):
			return

		# print prev1.data, pos1.data, prev2.data, pos2.data

		# if one of them is the head
		if prev1 is None:
			# pos1 is head
			temp = pos1.next
			pos1.next = pos2.next
			pos2.next = temp
			prev2.next = pos1

		if prev2 is None:
			# pos2 is head
			temp = pos2.next
			pos2.next = pos1.next
			pos1.next = temp
			prev1.next = pos2

		# if none of them is the head


		else:
			prev1.next = pos2
			prev2.next = pos1
			temp = pos1.next
			pos1.next = pos2.next
			pos2.next = temp


if __name__ == "__main__":
	ll = LinkedList()
	n0 = Node(1)
	n1 = Node(2)
	n2 = Node(3)
	n3 = Node(4)
	n4 = Node(5)
	n5 = Node(6)
	
	ll.push(n0)
	ll.push(n1)
	ll.push(n2)
	ll.push(n3)
	ll.push(n4)
	ll.push(n5)

	print "==orig list=="
	ll.print_list()

	print "==swapping nodes normal case=="
	ll.swap_nodes_normal_case(2, 4)
	ll.print_list()

	print "==swapping nodes=="
	ll.swap_nodes_generic(1, 6)
	ll.print_list()