#!/usr/bin/env python3

"""RRoss | Alta3 Research
   nesting an if-statement inside of a for loop"""

vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]

approved_vendors = ["cisco", "juniper", "big_ip"]

for x in vendors:
    print("\nThe vendor is " + x, end="")
print("\nOur loop has ended.")
