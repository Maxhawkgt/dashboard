import requests
import os

# Enter DS18B20 sensor names
sensorids = ["28-011921185ac2", "28-0119213b316f", "28-011921407f94"]

# Enter agent_host name for InfluxDB
hostname = 'pi2'

def read_temp_raw():
    f = open(device_file, "r")
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != "YES":
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find("t=")
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = (float(temp_string)*1.8+32000.0)/1000.0
        
        return temp_f
	
data =""
for sensor in range(len(sensorids)):
    device_file = "/sys/bus/w1/devices/"+ sensorids[sensor] +"/w1_slave"
    temperature = (read_temp())
    dtemp = "%.1f" % temperature
    result = (str(dtemp))
    print result

    data = sensorids[sensor] + ',agent_host=' + hostname + ',host=monitor treading=' + result
    p = requests.post('http://192.168.0.9:8086/write?db=rc_custom&precision=s', data.encode())

    print data

#CPU temperature
def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        temp = temp.replace("\'C","")
        return (temp.replace("temp=",""))

tempc = eval(measure_temp())
tempf = float(tempc)*1.8+32.0
print(tempc)
print(tempf)
data = 'cputemp,agent_host=' + hostname + ',host=monitor treading=' + str(tempf)
p = requests.post('http://192.168.0.9:8086/write?db=rc_custom&precision=s', data.encode())

print(data)
