import psutil 
import time



dsk = psutil.disk_usage('/')
print(dsk)
print(dsk.total)
print(dsk.used)
print(dsk.free)
print(dsk.percent)
btr1 = psutil.sensors_battery()
print(f"{str(btr1.percent)}%")

        
