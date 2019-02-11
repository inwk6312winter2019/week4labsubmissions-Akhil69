import copy

class point:
	"""Point class"""

class rectangle:
	"""Rectangle class"""

	def test_point(self,box):
	        p = point()
       		p.x = box.corner.x + box.width/2
        	p.y = box.corner.y + box.height/2
        	return p

	def print_point(self,p):
	        print('(%g,%g)'%(p.x,p.y))

	def rec(self,box,dx,dy):
		box.width += dx
		box.height += dy

rect=rectangle()
rect.width=100.0
rect.height=200.0
rect.corner=point()
rect.corner.x=0.0
rect.corner.y=0.0
box2=copy.deepcopy(rect)

center=rect.test_point(rect)
rect.print_point(center)
rect.rec(rect,70,120)
print(rect.width,rect.height)
box2.rec(box2,90,140)
print(box2.width,box2.height)


