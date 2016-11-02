"""
Write a recursive function to print reverse of a Linked List
Given a linked list, print reverse of it using a recursive function. For example, if the given linked list is 1->2->3->4, then output should be 4->3->2->1.

Note that the question is only about printing the reverse
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

	def print_rev(self, head):
		if head is None:
			return
		self.print_rev(head.next)
		print head.data


if __name__ == "__main__":
	ll = LinkedList()
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	f = Node('f')
	g = Node('g')
	h = Node('h')
	ll.push(a)
	ll.push(b)
	ll.push(c)
	ll.push(d)
	ll.push(e)

	ll1 = LinkedList()
	ll1.push(f)
	ll1.push(g)
	ll1.push(h)
	f.next = c

	ll.print_ll(ll.head)
	print "==print reverse=="
	print ll.print_rev(ll.head)
