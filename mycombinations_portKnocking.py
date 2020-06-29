from itertools import permutations
import socket,time,sys

items = '1356','6784','3409'

datalist = permutations(items)

remote_ip = '192.168.10.14'
remote_port = 22

s = socket.socket()

for data in list(datalist):
    print ("Trying port knocking combination " + str(data))
    
    for loop1 in range (0,len(data)):
        print("Connecting to remote ip = "+ remote_ip + " remote port = " + str(data[loop1]))
        extracted_port = data[loop1]
        extracted_port = int(extracted_port)
        
        try:
            s.connect((remote_ip,extracted_port))
            time.sleep(0.5) #0.5 seconds of sleep
    
        except Exception as e: 
            print("\n")
            #print ("We got an error = " + str(e))
  

    try:
        s.connect((remote_ip,remote_port))
        print("I think its open now") 
        sys.exit()

    except Exception as e: 
        print ("We got an error = " + str(e))
    
    


