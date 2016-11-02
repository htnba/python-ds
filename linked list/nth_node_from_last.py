"""
Find nth node from the end of a Linked List
Given a Linked List and a number n, write a function that returns the value at the nth node from end of the Linked List.
"""

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, node):
		node.next = self.head
		self.head = node

	def print_ll(self):
		head = self.head
		while(head):
			print head.data
			head = head.next

	def find_nth_from_last(self, n):
		dumb = self.head
		nth_from_last = self.head
		count = 0
		while(dumb):
			count += 1
			if count>n:
				nth_from_last = nth_from_last.next
			dumb = dumb.next
		if count<n:
			print "N exceeds len"
			return None
		return nth_from_last.data

if __name__ == "__main__":
	ll = LinkedList()
	ll.push(Node(1))
	ll.push(Node(2))
	ll.push(Node(3))
	ll.push(Node(4))
	ll.push(Node(5))
	ll.push(Node(6))
	ll.push(Node(7))
	ll.push(Node(8))
	ll.push(Node(9))
	ll.push(Node(10))
	ll.push(Node(11))
	# ll.push(Node(12))
	ll.print_ll()

	print "==nth from last=="
	print ll.find_nth_from_last(11)