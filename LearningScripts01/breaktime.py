import webbrowser
import time
total_breaks = 3
break_count = 0
print("This program starts on "+time.ctime())
while (break_count<total_breaks):
        time.sleep(5)
        webbrowser.open("https://www.youtube.com/watch?v=zpf8hrbT2d0")
        break_count=break_count+1
