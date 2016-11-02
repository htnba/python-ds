class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None

	def print_list(self):
		node = self.head
		while(node):
			print node.data
			node = node.next
	
	def push(self, node):
		node.next = self.head
		self.head = node

	def append(self, new_node):
		node = self.head
		while(node.next):
			# stops at the last node, when node.next becomes null
			node = node.next
		node.next = new_node

	def insert_after(self, data, new_node):
		temp_node = ll.head
		while(temp_node.data != data and temp_node):
			temp_node = temp_node.next
		temp = temp_node.next
		temp_node.next = new_node
		new_node.next = temp

	def delete(self, key):
		"""
			delete first occourance of key in the LinkedList
		"""
		prev_node = self.head
		while(prev_node.next and prev_node.next.data != key):
			prev_node = prev_node.next
		# in the end we are at the node having key or last node
		del_node = prev_node.next
		next_node = prev_node.next.next
		prev_node.next = next_node
		del del_node

	def delete_given_pos(self, pos):
		if pos == 0:
			del_node = self.head
			self.head = self.head.next
			del del_node
			return
		prev = self.head
		# dont understand
		# for i in xrange(0, pos):
			# temp = temp.next
		count = 0
		while(count<pos-1):
			prev = prev.next
			count +=1

		del_node = prev.next
		prev.next = prev.next.next
		del del_node

		# self.delete(temp.data)

if __name__ == "__main__":
	ll = LinkedList()
	n0 = Node(1)
	n1 = Node(2)
	n2 = Node(3)
	
	ll.head = n0
	n0.next = n1
	n1.next = n2
	ll.print_list()
	print "==="

	ll.push(Node(4))
	
	print "==="
	
	ll.print_list()
	
	print "==="
	
	ll.append(Node(5))
	ll.print_list()

	print "==="

	ll.insert_after(3, Node(20))
	ll.print_list()

	print "===deleting==="

	ll.delete(20)
	ll.print_list()

	print "===deleting end==="


	print "===deleting given pos==="

	ll.delete_given_pos(3)
	ll.print_list()

	print "===deleting given pos==="