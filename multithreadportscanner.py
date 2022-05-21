# Websites used to find information for syntax and how to use multithreading 
# https://www.tutorialspoint.com/python/python_multithreading.htm#:~:text=The%20threading%20module%20provided%20with,force%20threads%20to%20run%20synchronously.
# I read through the site to find the benefits of using multithreading
# regular port scanner has to wait for the server response to move onto the next port with multi threading we can specific how many
# processes can be active at once each scanning a port finding if its open then moving onto the next port 
# benefit for this is that when scanning for open ports one by one would take for ever waiting for response from server 
import pyfiglet # This is the module for my pretty banner
import socket # to resolve IP address to names
import threading # This is used to create the multithread to be able to scan more than one port at a time
from queue import Queue # used to create the queue for the ports to be scanned


print_lock = threading.Lock() # locks the current thread while scanning the port once done the thread releases and moves onto the next one


ascii_banner = pyfiglet.figlet_format("PORT SCANNER") # my pretty banner 
print(ascii_banner) # prints my pretty banner


print("Put in a remote or local host to port scan I.E. localhost or www.website.com") # Asks for the user input and stores it in a variable
target = str(input()) # target variable is created 



def portscan(port): # first function created to create the port scanner 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET specifies the ipv4 addressing 
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port',port,'Wow its open!') # checks the ports to see if they are opens and if True it will print that it is open
        con.close()
    except: # this error exception is in place if trying to connect to a port that requires elevated permissions and will pass it and move on
        pass


def threader(): # creates the multithread so it can pull a port out of the queue and process it to see if it is open 
    while True:
        worker = q.get() # gets the port from the queue
        portscan(worker)
        q.task_done()
q = Queue() # Creates the queue

for x in range(1000): # This is how many many threads or ports that will be in the queue at one time 
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1,65535): # the number of ports to be scanned this number can be changed
    q.put(worker)
q.join()
