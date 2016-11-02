"""
Given only a pointer/reference to a node to be deleted in a singly linked list, how do you delete it?
A simple solution is to traverse the linked list until you find the node you want to delete. But this solution requires pointer to the head node which contradicts the problem statement.
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

	def del_node(self, node):
		temp = node.next
		node.next = node.next.next
		node.data = temp.data
		del temp


if __name__ == "__main__":
	ll = LinkedList()
	ll.push(Node(5))
	ll.push(Node(4))
	del_n = Node(2)
	ll.push(del_n)
	ll.push(Node(1))
	ll.print_ll(ll.head)

	print "==delete LL node=="
	ll.del_node(del_n)
	ll.print_ll(ll.head)
