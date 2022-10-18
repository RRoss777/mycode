#!/usr/bin/env python3

"""Alta3 Research | RRoss
Pushing files around using shutil and os fromthe standard library"""


#import additional code to complete task
import shutil
import os

def main():
#move into working directory
    os.chdir("/home/student/mycode/")

#copy the file A to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#copy the entire directoryA to directory B
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
