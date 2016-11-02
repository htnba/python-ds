"""
Find the middle of a given linked list in C and Java
Given a singly linked list, find middle of the linked list. For example, if given linked list is 1->2->3->4->5 then output should be 3.

If there are even nodes, then there would be two middle nodes, we need to print second middle element. For example, if given linked list is 1->2->3->4->5->6 then output should be 4.
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

	def get_middle(self):
		slow = self.head
		fast = self.head
		if self.head is None:
			return None

		while(fast is not None and fast.next is not None):
			fast = fast.next.next
			slow = slow.next

		return slow

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

	print "==middle element=="
	print ll.get_middle().data
