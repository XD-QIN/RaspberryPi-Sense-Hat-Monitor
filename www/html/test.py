from sense_emu import SenseHat
from time import sleep
import pygal
temp = []
sense = SenseHat()
##sense.clear()
weather= pygal.Line()
i =0;
while True:
    sleep(0.1)
    myfile = open('weather.txt','a')
    temp.append(sense.get_temperature())
    if (i>10):
        temp.pop(1)
##    weather.render_to_file('/home/pi/osoyoo-robot/cam_robot/robot/temp_history.svg')
    weather= pygal.Line()
    weather.add('temp',temp)
    weather.render()    
    weather.render_to_file('temp_history.svg')
    myfile.write(str(sense.temp))
    myfile.write('\n')
    myfile.close()
    i=i+1
##weather.add('temp',temp)
##weather.render()    
##weather.render_to_file('temp_history.svg')


# store the temperature in the database
def log_temperature(temp):

    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    curs.execute("INSERT INTO temps values(datetime('now'), (?))", (temp,))

    # commit the changes
    conn.commit()

    conn.close()

