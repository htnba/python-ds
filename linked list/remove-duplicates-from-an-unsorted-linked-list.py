"""
Remove duplicates from an unsorted linked list
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
		while head is not None:
			print head.data
			head = head.next

	def remove_dups(self):
		head = self.head
		prev = None
		visited_dict = {}
		while head is not None:
			if visited_dict.get(head.data, None) is not None:
				prev.next=head.next
				temp = head.next
				del head
				head = temp
			else:
				visited_dict[head.data] = True
				prev = head
				head = head.next

if __name__ == "__main__":
	ll = LinkedList()
	a = Node('a')
	a1 = Node('a')
	b = Node('b')
	b1 = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	f = Node('f')
	g = Node('g')
	h = Node('h')
	ll.push(a)
	ll.push(b)
	ll.push(c)
	ll.push(a1)
	ll.push(d)
	ll.push(e)
	ll.push(b1)

	# print ll.head.next.next.next.next.next.next.data
	ll.print_ll(ll.head)
	print "==remove duplicates LL=="
	ll.remove_dups()
	ll.print_ll(ll.head)
	# print ll.head.data
