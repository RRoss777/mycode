#!/usr/bin/env python3
"""Alta3 Research | RRoss
   List - making selections from complex lists"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)
    
    #display second item in list 1
    print(list1[1])

    #create a second list
    list2 = ["juniper"]

    #extend list1 by list2
    list1.extend(list2)

    #display list1, now containing juniper
    print(list1)

    #create list3
    list3 =["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    #use append operation to append list1 by list3
    list1.append(list3)

    #display the new complext list1
    print(list1)

    #display item 5 (list of IP addresses) in list1
    print(list1[4])

    #display the first item in the list of IP addresses
    print(list1[4][0])

main()

