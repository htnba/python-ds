"""
Remove duplicates from a sorted linked list
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

	def remove_dups(self):
		head = self.head
		while head is not None and head.next is not None:
			if head.data == head.next.data:
				temp = head.next
				head.next = head.next.next
				del temp
			head = head.next


if __name__ == "__main__":
	ll = LinkedList()
	a = Node('a')
	a1 = Node('a')
	b = Node('b')
	b1 = Node('b')
	c = Node('c')
	c1 = Node('c')
	d = Node('d')
	e = Node('e')
	f = Node('f')
	g = Node('g')
	h = Node('h')
	ll.push(a)
	ll.push(a1)
	ll.push(b)
	ll.push(b1)
	ll.push(c)
	ll.push(c1)
	ll.push(d)
	ll.push(e)
	ll.push(f)
	ll.push(g)
	ll.push(h)

	ll.print_ll(ll.head)
	print "==remove duplicates LL=="
	ll.remove_dups()
	ll.print_ll(ll.head)