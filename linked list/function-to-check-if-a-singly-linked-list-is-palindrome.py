"""
Function to check if a singly linked list is palindrome
Given a singly linked list of characters, write a function that returns true if the given list is palindrome, else false.
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

	def reverse(self, head):
		# recursive
		if head is None or head.next is None:
			return head
		new_head = self.reverse(head.next)
		head.next.next = head
		head.next = None
		return new_head

	def reverse_iter(self, head):
		prev = None
		current = head
		next = current.next
		while(current and current.next):
			temp = current.next
			current.next = prev
			prev = current
			current = temp
			next = current.next
		current.next = prev
		return current


	def mid(self):
		slow = self.head
		fast = self.head
		prev = None
		while(fast is not None and fast.next is not None):
			fast = fast.next.next
			prev = slow
			slow = slow.next
		if fast is None:
			return (prev, "even", prev)
		else:
			return (slow, "odd", prev)

	def check_equal(self, head1, head2):
		while (head1 and head2):
			if head1.data != head2.data:
				return False
			head1 = head1.next
			head2 = head2.next
		if head1 is not None and head2 is not None:
			return False
		return True

	def check_palin(self, head):
		# find middle element
		# reverse the ll after middle
		# check if the two lists are same
		# revert the list back
		# return True or False
		(mid_node, oe,  prev) = self.mid()
		# print "oe", oe
		# print "mndata ", mid_node.data
		if oe=="odd":
			temp = mid_node
			mid_node = mid_node.next
			sec_half_head = mid_node
			prev.next = None
		if oe=="even":
			sec_half_head = mid_node.next
			mid_node.next = None

		rev_sec_half = self.reverse_iter(sec_half_head)

		# check equality
		print self.check_equal(rev_sec_half, head)


		if oe=="odd":
			# temp has the middle node
			# reverse the second list again
			# temp.next is the head of that list
			# prev is the end of the first half, so prev.next=temp
			valid_sec_half = self.reverse_iter(rev_sec_half)
			temp.next = valid_sec_half
			prev.next = temp
		if oe=="even":
			valid_sec_half = self.reverse_iter(rev_sec_half)
			mid_node.next = valid_sec_half


if __name__ == "__main__":
	ll = LinkedList()
	ll.push(Node('a'))
	ll.push(Node('b'))
	ll.push(Node('c'))
	ll.push(Node('b'))
	ll.push(Node('a'))

	ll.print_ll(ll.head)
	print "==check palindrome LL=="
	ll.check_palin(ll.head)
	ll.print_ll(ll.head)
