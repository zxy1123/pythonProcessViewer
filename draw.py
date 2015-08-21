import turtle
import math
class Shape:
	def __init__(self,t,name=""):
		self.t=t
		self.anchors=[]
		self.heart=None
		self.start=None
		self.name=name
	def move(self,x=0,y=0,heading=0):
		self.t.setheading(heading)
		self.t.penup()
		self.t.goto(x,y)
		self.t.pendown()
		self.setpos()
	def setpos(self,start=None):
		pass
	def heart2start(self,heart):
		pass
	def near_shape(self,other):
		min=-1
		ret =[]
		for sourceanchor in self.anchors:
			for targetanchor in other.anchors:
				x = sourceanchor[0] - targetanchor[0]
				y = sourceanchor[1] - targetanchor[1]
				dis = x**2 + y**2
				if min<0 or min > dis:
					min = dis
					ret=[Point(sourceanchor[0],sourceanchor[1]),Point(targetanchor[0],targetanchor[1])]
		return ret
	def draw_label(self):
		t=self.t
		self.move(self.start[0],self.start[1]+40)
		t.write(self.name)
				
				
class Square(Shape):
	def setpos(self,start=None):
		if start != None:
			pos=start
		pos=self.t.pos()
		self.heart=(pos[0]+20,pos[0]+20);
		self.start=pos
	def heart2start(self,heart):
		return (heart[0]-20,heart[1]-20)
	def draw(self):
		self.setpos()
		self.anchors=[]
		for i in [90,90,90,90]:
			self.t.forward(40)
			self.t.left(i)
			pos=self.t.pos()
			angle=self.t.heading()-90
			anchor=(pos[0]-20*math.cos(math.radians(angle)),pos[1]-20*math.sin(math.radians(angle)))
			self.anchors.append(anchor)
		self.draw_label()

		
class Diamond(Shape):
	def heart2start(self,heart):
		return (heart[0]-20,heart[1]-20) 
	def setpos(self,start=None):
		if start != None:
			pos=start
		pos=self.t.pos()
		self.heart=(pos[0]+20,pos[0]+20)
		self.start=pos
	def draw(self):
		self.setpos()
		self.t.penup()
		self.t.sety(self.t.ycor()+20)
		self.t.pendown()
		self.anchors=[]
		for i in [-45,90,90,90,90]:
			self.t.left(i)
			self.t.forward(40)
			pos=self.t.pos()
			self.anchors.append(pos)
		self.draw_label()
class Line(Shape):
	def __init__(self,t,name=""):
		self.t=t
		self.name=name
		self.start=None
	def move(self,x=0,y=0,heading=0):
		self.t.setheading(heading)
		self.t.penup()
		self.t.goto(x,y)
		self.t.pendown()
	def draw_arrow(self):
		pass
	def setpos(self,start=None):
		if start != None:
			pos=start
		pos=self.t.pos()
		self.start=pos
	def draw(self,start,end,heading=0):
		self.move(start.x,start.y,heading)
		self.t.goto(end.x,end.y)
		self.start=(start.x,start.y)
		self.draw_arrow(start,end)
		self.draw_label(start,end)
	def draw_label(self,start,end):
		t=self.t
		self.move((start.x+end.x)//2,(start.y+end.y)//2)
		t.write(self.name)
class LineWithArrow(Line):
	def draw_arrow(self,start,end):
		t=self.t
		x=end.x-start.x 
		y=end.y-start.y
		de=math.degrees(math.atan(math.fabs(y/x)))
		if x>0 and y<0:
			de = 360-de
		if x<0 and y>0:
			de = 180-de
		if x<0 and y<0:
			de =180+de
		t.seth(de)
		heading = t.heading()
		pos = t.pos()
		array=[30,-30]
		for i in array:
			t.left(i)
			t.backward(10)
			self.move(pos[0],pos[1],heading)
class Point():
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def __str__(self):
		return "{0} {1}".format(self.x,self.y)
if __name__=="__main__":
	tu = turtle.Turtle();
	tu.speed(0)
	tu.hideturtle()
	s = Square(tu,"test")
	t = Square(tu,"test")
	
	s.draw()
	for i in range(36):
		i*=10
		r=math.radians(i)
		t.move(200*math.cos(r),200*math.sin(r));
		t.draw()
		ret=s.near_shape(t)
		l = LineWithArrow(tu,"tststs")
		l.draw(ret[0],ret[1])
	t.move()
	wn=turtle.Screen();
	def quit():
		wn.bye()
	wn.onkey(quit,"q")
	wn.listen()
	wn.mainloop()