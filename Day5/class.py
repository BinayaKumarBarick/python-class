class Item:
    def _init_(self,name,type,size,others):
        self.name=name
        self.type=type
        self.others=others
        self.calculate_size()

    def calculate_size(self):
        self.size=len(self.name)+len(self.type)

item ={
        "name":"laptop", "type":"electronics","others":{"brand":"xyz","color":"silver"}
      }
print(item.name,item.type,item.others)


class storage:
    def _init_(self,host,port,protocol,container):
        self.host=host
        self.port=port
        self.protocol=protocol
        self.container=[]

    def add_element(self,item):
         self.container.append(item)

    def calculate_size(self):
         return sum(item.size for item in self.container)
