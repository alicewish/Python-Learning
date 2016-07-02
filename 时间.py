import datetime, time

starttime = datetime.datetime.now()
time.sleep(1)
endtime = datetime.datetime.now()
print((endtime - starttime).days)

