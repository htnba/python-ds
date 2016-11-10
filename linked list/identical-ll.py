"""
Identical Linked Lists
Two Linked Lists are identical when they have same data and arrangement of data is also same. For example Linked lists a (1->2->3) and b(1->2->3) are identical. . Write a function to check if the given two linked lists are identical.
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
	def identical_ll(head1, head2):
		while(head1 and head2):
			if(head1.data != head2.data):
				return False
			else:
				head1 = head1.next
				head2 = head2.next
		if(head1 is not None or head2 is not None):
			return False
		return True

	@staticmethod
	def identical_ll_recur(head1, head2):
		if head1 is None and head2 is None:
			return True
		elif head1.data != head2.data:
			return False
		return LinkedList.identical_ll_recur(head1.next, head2.next)

if __name__ == "__main__":
	ll = LinkedList()
	h = Node(1)
	g = Node(2)
	f = Node(3)
	e = Node(4)
	ll.push(e)
	ll.push(f)
	ll.push(g)
	ll.push(h)

	print "==ll=="
	ll.print_ll(ll.head) # 7 nodes

	ll1 = LinkedList()
	ll1.push(Node(4))
	ll1.push(Node(3))
	ll1.push(Node(2))
	# ll1.push(Node(1))

	print "==ll1=="
	ll1.print_ll(ll1.head)  # 6nodes

	print LinkedList.identical_ll_recur(ll.head, ll1.head)