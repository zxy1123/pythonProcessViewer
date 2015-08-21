from xmlparser import get_graph
import bfs
import draw
import turtle
import sys
class Context:
	def __init__(self):
		self.max_wide=0
		self.max_height=0
		self.data={}
	def __str__(self):
		return "{0} {1} {2}".format(self.max_wide,self.max_height,self.data)
def get_adj_list(adj_list):
	ret = {}
	for k in adj_list:
		ret[k]=[]
		for v in adj_list[k]:
			ret[k].append(v[0])
	return ret
def get_weight(adj_list):
	start=None
	for k in adj_list:
		if k.is_name("startNode"):
			start=k
			break
	group=bfs.search(adj_list,start)
	for gen in group:
		for k in gen:
			k.weight=gen.get(k)
def create_context(list):
	c = Context()
	max_wide=0
	for v in list:
		list = c.data.get(v.weight,None)
		if list==None:
			c.data[v.weight]=[]
			list=c.data[v.weight]
		list.append(v)
	for k in c.data:
		l = len(c.data[k])
		if l > max_wide:
			max_wide=l
	c.max_wide=max_wide
	c.max_height=len(c.data.keys())
	return c	
def pos(p,n,scale=10):
	mid = n+1
	return ((p*2-mid)*scale)//2
def mainloop():
	wn=turtle.Screen();
	def quit():
		wn.bye()
	wn.onkey(quit,"q")
	wn.listen()
	wn.mainloop()
def main(wide_dis,height_dis,path):
	turtle.screensize(1000,1700)
	tu = turtle.Turtle()
	tu.hideturtle()
	tu.speed(0)
	adj_list_edge=get_graph(path)
	adj_list=get_adj_list(adj_list_edge)
	get_weight(adj_list)
	list=sorted(adj_list,key=lambda v:v.weight)
	c=create_context(list)
	height= c.max_height
	for k in c.data:
		i=1
		wide=len(c.data[k])
		for v in c.data[k]:
			v.heart=(pos(i,wide,wide_dis),pos(height-k-1,height,height_dis))
			i+=1
	pair={}
	for v in list:
		s=None
		if v.type=="exclude":
			s=draw.Diamond(tu,v.name)
			pair[v]=s
		else:
			s=draw.Square(tu,v.name)
			pair[v]=s
		start=s.heart2start(v.heart)
		s.move(start[0],start[1])
		s.draw()
	for v in adj_list_edge:
		list=adj_list_edge[v]
		for iter in list:
			s=pair[v]
			e=pair[iter[0]]
			dis=s.near_shape(e)
			l = draw.LineWithArrow(tu,iter[1])
			l.draw(dis[0],dis[1])
			l.move()
	mainloop()
if __name__=='__main__':
	path=sys.argv[1]
	main(300,100,path)