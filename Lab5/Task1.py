from math import sqrt
class test:

	def distance(self,i,j):
		dx=i
		dy=j
		print(i.x,j.x)
		dx=i.x-j.x
		dy=i.y-j.y
		print(dx,dy)
		res=sqrt(dx**2+dy**2)
		print(res)

pt1=test()
pt2=test()
pt1.x=5
pt2.x=4
pt1.y=6
pt2.y=4

pt1.distance(pt1,pt2)
