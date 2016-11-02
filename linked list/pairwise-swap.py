"""
Pairwise swap elements of a given linked list
Given a singly linked list, write a function to swap elements pairwise. For example, if the linked list is 1->2->3->4->5 then the function should change it to 2->1->4->3->5, and if the linked list is 1->2->3->4->5->6 then the function should change it to 2->1->4->3->6->5. 
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


	def pairwise_swap(self):
		prev = None
		current = self.head
		next = self.head.next
		while(current and next):
			# temp = next
			current.next = next.next
			next.next = current
			if prev is not None:
				prev.next = next
				print "prev, current, next", prev.data, current.data, next.data
			else:
				self.head = next
				print "prev, current, next", prev, current.data, next.data
				pass
			prev = current
			if prev.next:
				current = prev.next
			else:
				current = None
			if current and current.next:
				next = current.next
			else:
				next = None

	def pairwise_swap_recur(self, head):
		if head is None or head.next is None:
			return head
		temp = head.next # g
		new_head = head.next.next # f
		head.next.next = head # g-> h
		# print temp, temp.next
		head.next = self.pairwise_swap_recur(new_head) # h-> whatever returned
		return temp # return g??. no. return f

if __name__ == "__main__":
	ll = LinkedList()
	a = Node('a')
	# a1 = Node('a')
	b = Node('b')
	# b1 = Node('b')
	c = Node('c')
	# c1 = Node('c')
	d = Node('d')
	e = Node('e')
	f = Node('f')
	g = Node('g')
	h = Node('h')
	ll.push(a)
	# ll.push(a1)
	ll.push(b)
	# ll.push(b1)
	# ll.push(c)
	# ll.push(c1)
	ll.push(d)
	ll.push(e)
	ll.push(f)
	ll.push(g)
	ll.push(h)

	ll.print_ll(ll.head)
	print "==pairwise_swap_iter=="
	ll.pairwise_swap()
	# ll.head = ll.pairwise_swap_recur(ll.head)
	ll.print_ll(ll.head)