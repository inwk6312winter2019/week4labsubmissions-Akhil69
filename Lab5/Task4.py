class Test:
	"""this class shows time"""

t1=Test()
t2=Test()

t1.hour=10
t1.minute=55
t1.second=25

t2.hour=10
t2.minute=45
t2.second=30

def print_time(t):
	print('the time is:','%.2d:%.2d:%.2d'%(t.hour,t.minute,t.second))
 
def is_after(t1, t2):
    t1_total_seconds = (t1.hour * 3600) + (t1.minute * 60) + t1.second
    t2_total_seconds = (t2.hour * 3600) + (t2.minute * 60) + t2.second
    return t1_total_seconds > t2_total_seconds
     
print_time(t1)
print_time(t2)

print(is_after(t1,t2))
