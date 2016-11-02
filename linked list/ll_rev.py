"""
Write a function to reverse a linked list
Given pointer to the head node of a linked list, the task is to reverse the linked list.
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

	def reverse(self, head):
		if head.next is None:
			return head
		head_rev = self.reverse(head.next)
		head.next.next = head
		head.next = None
		return head_rev

	def reverse_iter(self):
		prev = None
		current = self.head
		next = current.next

		while(current and current.next):
			current.next = prev
			prev = current
			current = next
			next = current.next
		current.next = prev
		prev = current
		return prev
	

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
	ll.push(Node(12))
	ll.print_ll(ll.head)

	print "==reverse=="
	new_head = ll.reverse_iter()
	ll.print_ll(new_head)