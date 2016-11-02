"""
Write a program function to detect loop in a linked list
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

	def print_ll(self, head):
		while(head):
			print head.data
			head = head.next

	def detect_loop(self):
		slow_ptr = self.head
		fast_ptr = self.head.next
		while(fast_ptr and fast_ptr.next and fast_ptr.data!=slow_ptr.data):
			fast_ptr = fast_ptr.next.next
			slow_ptr = slow_ptr.next
		print "fast_ptr.data", fast_ptr.data
		print "slow_ptr.data", slow_ptr.data
		if fast_ptr.data == slow_ptr.data:
			return True
		else:
			return False

if __name__ == "__main__":
	ll = LinkedList()
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)
	n5 = Node(5)
	n1.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n2
	ll.head = n1

	# ll.print_ll(ll.head)

	print "==detect loop=="
	print ll.detect_loop()
	# new_head = ll.reverse_iter()
	# ll.print_ll(new_head)