"""
union-and-intersection-of-two-linked-lists
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

	@staticmethod
	def print_ll(head):
		while(head):
			print head.data
			head = head.next

	@staticmethod
	def union_and_intersection(head1, head2):
		# do merge sprt
		# then combine both the lists
		


if __name__ == "__main__":
	ll = LinkedList()
	h = Node(124)
	g = Node(332)
	f = Node(3)
	e = Node(21)
	i = Node(52)
	j = Node(1000)
	k = Node(2000)
	ll.push(e)
	ll.push(f)
	ll.push(g)
	ll.push(h)
	ll.push(i)
	ll.push(j)
	ll.push(k)
	print "==ll=="
	ll.print_ll(ll.head) # 7 nodes

	ll1 = LinkedList()
	h1 = Node(23124)
	g1 = Node(23332)
	f1 = Node(3)
	e1 = Node(21)
	i1 = Node(2352)
	j1 = Node(231000)
	k1 = Node(2000)
	ll1.push(e1)
	ll1.push(f1)
	ll1.push(g1)
	ll1.push(h1)
	ll1.push(i1)
	ll1.push(j1)
	ll1.push(k1)
	print "==ll=="
	ll.print_ll(ll1.head) # 7 nodes

	print "==rev=="
	ll.print_ll(LinkedList.union_and_intersection(ll.head, 2))
	# ll.print_ll(LinkedList.reverse(ll.head))
