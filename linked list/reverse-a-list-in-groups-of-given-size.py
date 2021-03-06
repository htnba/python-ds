"""
Reverse a Linked List in groups of given size
Given a linked list, write a function to reverse every k nodes (where k is an input to the function). 
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
	def reverse(head):
		if head is None or head.next is None:
			return head
		# 1-2-3-4-5  1 2-3-4-5; 1 5-4-3-2 new head is 5 suppose; new_head.next is the current node and current node.
		# next is None
		temp = head.next
		new_head = LinkedList.reverse(head.next)
		head.next = None
		temp.next = head
		return new_head


	@staticmethod
	def rev_groups(head, size):
		# reverse the first group of k elements
		# then call recursively maybe
		if size<1:
			print "Not done dude!"
			return head
		if head is None or head.next is None:
			return head

		counter = 1
		tail = head
		while(counter<size and tail.next):
			tail = tail.next
			counter += 1
		# print "counter", counter
		# print "tail", tail.data
		temp = tail.next
		tail.next = None
		new_head = LinkedList.reverse(head)
		# print "nh", new_head.data
		# print "ll", LinkedList.print_ll(new_head)
		# nh3-2-1  temp4-5-6-7
		# print "h", head.data
		head.next = LinkedList.rev_groups(temp, size)
		return new_head

		# 1-2-3-4-5-6-7 size is 3
		# counter 1, head @ 2
		# counter 2, head @3
		# counter 3, head @4 not done
		# pass


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

	print "==rev=="
	ll.print_ll(LinkedList.rev_groups(ll.head, 3))
	# ll.print_ll(LinkedList.reverse(ll.head))
