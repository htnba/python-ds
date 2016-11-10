"""
Merge Sort for Linked Lists
Merge sort is often preferred for sorting a linked list. The slow random-access performance of a linked list makes some other algorithms (such as quicksort) perform poorly, and others (such as heapsort) completely impossible.
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
	def partition(head):
		if head is None:
			return (None, None)
		if head.next is None:
			return (None, head)
		slow = head
		fast = head.next
		prev = None
		while (fast and fast.next):
			fast = fast.next.next
			prev = slow
			slow = slow.next
		if fast is None:
			prev.next = None
			return (head, slow)
		elif fast is not None:
			temp = slow.next
			slow.next = None
			return (head, temp)

	@staticmethod
	def merge_recur(head1, head2):
		if head1 is None:
			return head2
		# is it necessary to use elif here?? test it
		elif head2 is None:
			return head1
		res = None
		if(head1.data<=head2.data):
			res = head1
			res.next = LinkedList.merge_recur(head1.next, head2)
		if(head2.data<head1.data):
			res = head2
			res.next = LinkedList.merge_recur(head1, head2.next)
		return res


	@staticmethod
	def merge_sort(head):
		if head is None or head.next is None:
			return head
		# divide the list into two parts
		# call merge sort on them
		# merge them
		head1, head2 = LinkedList.partition(head)
		head1 = LinkedList.merge_sort(head1)
		head2 = LinkedList.merge_sort(head2)
		return LinkedList.merge_recur(head1, head2)

if __name__ == "__main__":
	ll = LinkedList()
	h = Node(124)
	g = Node(332)
	f = Node(3)
	e = Node(21)
	i = Node(52)
	ll.push(e)
	ll.push(f)
	ll.push(g)
	ll.push(h)
	ll.push(i)

	print "==ll=="
	ll.print_ll(ll.head) # 7 nodes

	print "==sorted ll=="
	new_head = LinkedList.merge_sort(ll.head)
	ll.print_ll(new_head)

	# ll1 = LinkedList()
	# ll1.push(Node(4))
	# ll1.push(Node(3))
	# ll1.push(Node(2))
	# ll1.push(Node(1))

	# print "==ll1=="
	# ll1.print_ll(ll1.head)  # 6nodes

	# print "==partition=="
	# h1, h2 = ll.partition(ll.head)


	# print "==1"
	# ll.print_ll(h1)
	# print "==2"
	# ll.print_ll(h2)
