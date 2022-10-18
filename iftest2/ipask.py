#!/usr/bin/env python3

"""Alta3 Research | RRoss
Conditionals - strings test true"""
                                                     
ipchk = input("Apply an IP address:")
                               
# a string tests as True
if ipchk:
    print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk:
    print("Looks like the IP address was set:" + ipchk)
else:# if data is NOT provided
   print("You did not provide input.") # indented under else
