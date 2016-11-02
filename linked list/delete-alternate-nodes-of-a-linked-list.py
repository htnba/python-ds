"""
Delete alternate nodes of a Linked List
Given a Singly Linked List, starting from the second node delete all alternate nodes of it. For example, if the given linked list is 1->2->3->4->5 then your function should convert it to 1->3->5, and if the given linked list is 1->2->3->4 then convert it to 1->3.
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

	ll1 = LinkedList()
	ll1.push(Node(91))
	ll1.push(Node(112))
	ll1.push(Node(1221))
	ll1.push(Node(3123))
	ll1.push(Node(343))
	ll1.push(Node(432))

	print "==ll1=="
	ll1.print_ll(ll1.head)  # 6nodes


	print "==intersection LL=="
	ll.del_alt_nodes()
	ll1.del_alt_nodes()

	print "==del LL1=="	
	LinkedList.print_ll(ll.head)
	print "==del LL2=="	
	LinkedList.print_ll(ll1.head)