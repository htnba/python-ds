"""
intersection-of-two-sorted-linked-lists
"""
import copy

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

	def intersection_iter(self, head1, head2):
		new_head = None
		tail = None
		while (head1 and head2):
			print head1.data, head2.data
			if head1.data < head2.data:
				head1 = head1.next
			elif head2.data < head1.data:
				head2 = head2.next
			elif head1.data == head2.data:
				node = copy.copy(head1)
				if new_head is None:
					new_head = node
					tail = node
				else:
					tail.next = node
					tail = node
				head1 = head1.next
				head2 = head2.next
		return new_head

	def intersection_recur(self, head1, head2):
		if head1 is None or head2 is None:
			return None

		new_head = None
		if head1.data<head2.data:
			# advance the first list
			self.intersection_recur(head1.next, head2)
		if head2.data<head1.data:
			# advance the second list
			self.intersection_recur(head1, head2.next)
		if head1.data == head2.data:
			# make a new node and do things to it.
			# advance both the lists
			new_head = copy.copy(head1)
			new_head.next = self.intersection_recur(head1.next, head2.next)
		return new_head



if __name__ == "__main__":
	ll = LinkedList()
	h = Node(1)
	g = Node(2)
	f = Node(3)
	e = Node(4)
	d = Node(5)
	c = Node(6)
	b = Node(7)
	a = Node(8)
	ll.push(a)
	ll.push(b)
	ll.push(c)
	ll.push(d)
	ll.push(e)
	ll.push(g)
	ll.push(h)

	ll.print_ll(ll.head)

	ll1 = LinkedList()
	ll1.push(b)
	ll1.push(c)
	ll1.push(d)
	ll1.push(f)
	ll1.push(g)
	ll1.push(h)

	print "=="
	ll1.print_ll(ll1.head)


	print "==intersection LL=="
	new_head = ll.intersection_recur(ll.head, ll1.head)
	LinkedList.print_ll(new_head)