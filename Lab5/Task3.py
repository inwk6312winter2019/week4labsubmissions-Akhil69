class Test:
	"""this class shows time"""

	

time=Test()
time.hour=9
time.minute=35
time.second=25
def print_time(t):
	print('the time is:','%.2d:%.2d:%.2d'%(t.hour,t.minute,t.second))

print_time(time)
