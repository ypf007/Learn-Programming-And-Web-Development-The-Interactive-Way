class Node:
    def __init__(self,initialdata):
        self.data = initialdata
        self.tail = None
    def changeTail(self,newtail):
        self.tail = newtail

class UnorderedList:
    def __init__(self):
        self.head = None
    def add(self,initialdata):
        tempnode = Node(initialdata)
        tempnode.changeTail(self.head)
        self.head = tempnode

list1 = UnorderedList()

list1.add({'Id': 0,'Role': 'Me', 'BMI': 21.1})
list1.add({'Id': 1,'Role': 'Wife', 'BMI':18.2})
list1.add({'Id': 2,'Role': 'Mom', 'BMI': 22.7})

# pythontutor's permanent link:
# http://pythontutor.com/visualize.html#code=class%20Node%3A%0A%20%20%20%20def%20__init__%28self,initialdata%29%3A%0A%20%20%20%20%20%20%20%20self.data%20%3D%20initialdata%0A%20%20%20%20%20%20%20%20self.tail%20%3D%20None%0A%20%20%20%20def%20changeTail%28self,newtail%29%3A%0A%20%20%20%20%20%20%20%20self.tail%20%3D%20newtail%0A%0Aclass%20UnorderedList%3A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20self.head%20%3D%20None%0A%20%20%20%20def%20add%28self,initialdata%29%3A%0A%20%20%20%20%20%20%20%20tempnode%20%3D%20Node%28initialdata%29%0A%20%20%20%20%20%20%20%20tempnode.changeTail%28self.head%29%0A%20%20%20%20%20%20%20%20self.head%20%3D%20tempnode%0A%0Alist1%20%3D%20UnorderedList%28%29%0A%0Alist1.add%28%7B'Id'%3A%200,'Role'%3A%20'Me',%20'BMI'%3A%2021.1%7D%29%0Alist1.add%28%7B'Id'%3A%201,'Role'%3A%20'Wife',%20'BMI'%3A18.2%7D%29%0Alist1.add%28%7B'Id'%3A%202,'Role'%3A%20'Mom',%20'BMI'%3A%2022.7%7D%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false