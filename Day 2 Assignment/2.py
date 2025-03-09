import pkg2 
import datetime

f = pkg2.File('.')
print(f.getMaxSize(2))
print(f.getLatestFiles(datetime.date(2025,3,8)))

