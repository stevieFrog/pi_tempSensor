import Adafruit_DHT
import datetime
import time

while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
        from datetime import datetime
        timeIsNow = datetime.now()
        timeIsNow_st = timeIsNow.strftime("%d/%m/%Y %H:%M:%S")
        todaysDate = timeIsNow.strftime("%Y%m%d")
        exactTimeNow = timeIsNow.strftime("%H:%M:%S")
        fileNameWithDate = "Results" + todaysDate + ".txt"
        timeToWait = 300

        if humidity is not None and temperature is not None:
                humidity = round(humidity, 2)
                temperature = round(temperature, 2)
                textOutput = 'Temp = {0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature, humidity) + " @ " + timeIsNow_st
                writeOutput = timeIsNow_st + "," + todaysDate + "," + exactTimeNow + "," + '{0:0.1f},{1:0.1f}'.format(temperature, humidity)
        else:
                textOutput = 'Cannot connect to the sensor!' + " @ " + timeIsNow_st

        with open(fileNameWithDate, 'a') as f:
                f.write(writeOutput + '\n')

        print textOutput
        time.sleep(timeToWait)
