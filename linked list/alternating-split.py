"""
Alternating split of a given Singly Linked List
Write a function AlternatingSplit() that takes one list and divides up its nodes to make two smaller lists a and b. The sublists should be made from alternating elements in the original list. So if the original list is 0->1->0->1->0->1 then one sublist should be 0->0->0 and the other should be 1->1->1. 
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

	def del_alt_nodes(self):
		current = self.head
		del_node = current.next
		while (current and del_node):
			current.next = del_node.next
			del del_node
			current = current.next
			if current:
				del_node = current.next
			else:
				del_node = None

	def alt_spilt(self):
		t1 = self.head
		t2 = self.head.next
		while (t1 and t2):
			print self.head.data, self.head.next.data
			t1.next = t2.next
			if t2.next is not None:
				t2.next = t2.next.next
			t1 = t1.next
			t2 = t2.next
		return (self.head, self.head.next)


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

	print "==ll=="
	ll.print_ll(ll.head) # 7 nodes


	(h1, h2) = ll.alt_spilt()

	print "==alt_spilt 1=="	
	LinkedList.print_ll(h1)

	print "==alt_spilt 2=="	
	LinkedList.print_ll(h2)