class Item:
    def __init__(self, name,type,others):
        self.name = name
        self.type = type
        self.others = others
        self.size=self.calculate_size()

    def calculate_size(self):
        self.size= len(self.name) + len(self.type)
        return self.size

class Storage:
    def __init__(self, host, port, protocol,max_size):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.container = []
        self.max_size=max_size
        self.current_item_size=0

    def add_element(self, item):
        
        try:
            if not isinstance(self,Item):
                raise TypeError("invalid  object type")
        except TypeError:
            print("This is not a valid Item Object")

        try:
            if self.current_item_size+item.size>self.max_size:
                raise MemoryError
        except MemoryError:
            print("maximum storage size exceeds")
        finally:
            self.container.append(item)
            self.current_item_size+=item.size
            print(" new item added")
            return item      
        
    def calculate_size(self):
       
        self.size = sum([item.size for item in self.container])
        return self.size
      
 
item1 = Item("laptop","electronics", others={"color":"silver","brand":"xyz"}) 
print(item1.size)
storage1=Storage("bicky",22,"http",max_size=10)
storage1.add_element(item1)
item2 = Item("dog","animal", others={"color":"black","brand":"abc"})
storage1.add_element(item2)
print("max_size:",storage1.max_size)
print(storage1.calculate_size())


            
