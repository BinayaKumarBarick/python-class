class Item:
    def __init__(self, name, type, others):
        self.name = name
        self.type = type
        self.others = others 
        self.size=self.calculate_size()

    def calculate_size(self):
        self.size = len(self.name) + len(self.type)
        return self.size

class Storage:
    def __init__(self, host, port, protocol ):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.container = []

    def add_element(self, item):
        self.container.append(item)
        return item

    def calculate_size(self):
        return sum(item.size for item in self.container)
    
item1= Item("laptop","electronics",others={ "color":"silver","brand":"xyz"})
print(item1.size)
storage1=Storage("host1",22,"http")
print(storage1.host)
print(storage1.add_element(item1))
       


