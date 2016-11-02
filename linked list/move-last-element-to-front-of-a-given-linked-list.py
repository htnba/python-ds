"""
move-last-element-to-front-of-a-given-linked-list
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

	def last_to_first(self):
		head = self.head
		prev = None
		while head.next is not None:
			prev = head
			head = head.next
		prev.next = None
		head.next = self.head
		self.head = head

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

	# ll1 = LinkedList()
	# ll1.push(f)
	# ll1.push(g)
	# ll1.push(h)
	# f.next = c

	ll.print_ll(ll.head)
	print "==move last to first LL=="
	print ll.last_to_first()
	ll.print_ll(ll.head)
