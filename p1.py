from datetime import *
d1 = datetime(2017, 9, 5, 6, 50, 30)
period = timedelta(days=10, hours=12, minutes=30, seconds=10)
print('New date and time = ', d1+period)
Output
New date and time =  2017-09-15 19:20:40
