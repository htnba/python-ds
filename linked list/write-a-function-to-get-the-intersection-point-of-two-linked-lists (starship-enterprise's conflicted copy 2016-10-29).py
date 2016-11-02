"""
Write a function to get the intersection point of two Linked Lists.
There are two singly linked lists in a system. By some programming error the end node of one of the linked list got linked into the second list, forming a inverted Y shaped list. Write a program to get the point where two linked list merge. 
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

	def get_intersection_pt(self, head1, head2):
		temp = head1
		while(temp.next):
			temp = temp.next
		# we are at the last node in the first list
		temp.next = head1

		# the first list is now circular

		# now detect and find the intersection node
		slow = head2
		fast = head2.next
		while(fast and fast.next and slow.data!=fast.data):
			fast = fast.next.next
			slow = slow.next
		if fast is None:
			# there is no loop
			return None


		# slow and fast have met at last!

		# find the intersection point now
		slow = head2
		fast = fast.next
		prev = None
		while(slow.data!=fast.data):
			slow = slow.next
			prev = fast
			fast = fast.next
		
		# # slow and fast have met again. Too many times man.

		temp.next = None
		return slow


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
	print "==get intersection pt LL=="
	print ll.get_intersection_pt(ll.head, ll1.head).data
