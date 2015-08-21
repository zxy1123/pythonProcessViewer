class Vertex:
	def __init__(self,name,type="S",pre=None,next=None,weight=-1):
		self.name=name
		self.type=type
		self.pre=pre
		self.next=next
		self.heart=(0,0)
		self.weight=weight
	def is_name(self,name):
		if self.name==name:
			return True
		return False
	def __eq__(self,o):
		if o==None:
			return False
		if(self.name==o.name):
			return True
		return False
	def __hash__(self):
		return hash(self.name)
	def __str__(self):
		return "name:{0} type:{1} pre:{2} next:{3} weight:{4},heart:{5}".format(self.name,self.type,self.pre,self.next,self.weight,self.heart)