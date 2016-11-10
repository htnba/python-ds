"""
reverse-alternate-k-nodes-in-a-singly-linked-list
"""
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
		if head is None or head.next is None:
			return head
		tail = head
		counter = 1
		while(counter<size and tail.next):
			counter += 1
			tail = tail.next
		# we are at 1-2-3-4-5-6-7-8-9 we are at 3.
		temp = tail.next
		tail.next = None
		new_head = LinkedList.reverse(head)
		# 3-2-1 4-5-6-7-8-9
		head.next = temp
		counter = 1
		tail = temp
		while (counter<size and tail.next):
			counter += 1
			tail = tail.next
		tail.next = LinkedList.rev_groups(tail.next, size)
		return new_head


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
	ll.print_ll(LinkedList.rev_groups(ll.head, 2))
	# ll.print_ll(LinkedList.reverse(ll.head))
