'''
I made this during pentesting djinn from Vulnhub
29 June 2020 - 22:18 hrs PKT GMT +0500hrs

Updated for Udacity Project
11 April 2021 - 22:18 hrs PKT GMT +0500hrs
'''
from itertools import permutations
import socket,time,sys

items = '1356','6784','3409' # the port combinations you want to try out === change this as per your requirement

datalist = permutations(items)

remote_ip = '192.168.10.14' #remote IP address === change this as per your requirement
remote_port = 22 #remote port that should be checked after trying the combinations === change this as per your requirement

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
        print("I think the port is open now ^___^ ") 
        sys.exit()

    except Exception as e: 
        print ("We got an error = " + str(e))
    
    


