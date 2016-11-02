"""
Merge two sorted linked lists
Write a SortedMerge() function that takes two lists, each of which is sorted in increasing order, and merges the two together into one list which is in increasing order. SortedMerge() should return the new list. The new list should be made by splicing
together the nodes of the first two lists.
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

	def merge(self, head1, head2):
		dummy_head = None
		last_node = None
		while(head1 and head2):
			if(head2 and head1 and head2.data < head1.data):
				while (head1 and head2 and head2.data<head1.data):
					if dummy_head is None:
						dummy_head = head2
						last_node = head2
					else:
						last_node.next = head2
						last_node = last_node.next
					head2 = head2.next

			if(head2 and head1 and head1.data < head2.data):
				while (head1 and head2 and head1.data<head2.data):
					if dummy_head is None:
						dummy_head = head1
						last_node = head1
					else:
						last_node.next = head1
						last_node = last_node.next
					head1 = head1.next

		if(head1 is None and head2 is not None):
			while(head2):
				last_node.next = head2
				last_node = head2
				head2 = head2.next

		if(head2 is None and head1 is not None):
			while(head1):
				last_node.next = head1
				last_node = head1
				head1 = head1.next
		return dummy_head

	def merge_recursive(self, head1, head2):
		if head1 is None:
			return head2
		elif head2 is None:
			return head1

		#  otherwise do what?
		new_head = None

		if(head1.data < head2.data):
			new_head = head1
			new_head.next = self.merge_recursive(head1.next, head2)
		else:
			new_head = head2
			new_head.next = self.merge_recursive(head1, head2.next)
		return new_head

		

if __name__ == "__main__":
	ll = LinkedList()
	ll.push(Node(5))
	ll.push(Node(4))
	ll.push(Node(2))
	ll.push(Node(1))
	ll.print_ll(ll.head)

	ll2 = LinkedList()
	ll2.push(Node(10))
	ll2.push(Node(8))
	ll2.push(Node(3))

	print "==merge LLs recursive=="
	new_head = ll.merge_recursive(ll.head, ll2.head)
	ll.print_ll(new_head)
