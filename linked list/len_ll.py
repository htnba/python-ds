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

	def len_iter(self):
		count = 0 
		temp = self.head
		while(temp):
			temp = temp.next
			count += 1
		return count

	def len_recur(self, node, count_cur):
		if node is None:
			return count_cur
		return self.len_recur(node.next, count_cur+1)

	def search_iter(self, key):
		temp = self.head
		while (temp):
			if(temp.data == key):
				return True
			temp = temp.next
		if temp is None:
			return False

	def search_recur(self, node, key):
		if node is None:
			return False
		if node.data==key:
			return True
		return self.search_recur(node.next, key)
	
if __name__ == "__main__":
	ll = LinkedList()
	n0 = Node(1)
	n1 = Node(2)
	n2 = Node(3)
	n3 = Node(4)
	n4 = Node(5)
	n5 = Node(6)
	
	ll.push(n0)
	ll.push(n1)
	ll.push(n2)
	ll.push(n3)
	ll.push(n4)
	ll.push(n5)

	print "==orig list=="
	ll.print_list()

	print "==len list=="
	print ll.len_iter()

	print "==len list recur=="
	print ll.len_recur(ll.head, 0)

	print "==len list search iter=="
	print ll.search_iter(40)

	print "==len list search recur=="
	print ll.search_recur(ll.head, 4)