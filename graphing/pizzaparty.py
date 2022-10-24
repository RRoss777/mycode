#!/usr/bin/env python3

"""Alta3 Research | RRoss 
- Creating a pie chart"""

import matplotlib.pyplot as plt
import numpy as np

def main ():

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Cheese', 'Spinach', 'Onions', 'Bacon'
    sizes = [60, 30, 5, 5]
    explode = (0, 0, 0.2, 0)  # only "explode" the 3nd slice (i.e. 'Onions')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.savefig("/home/student/mycode/pizzaparty.png")
    plt.savefig("/home/student/static/pizzaparty.png")

main()
