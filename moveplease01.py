#!usr/bin/env python3

"""A simple script to move two files into ceph_storage/
Alta3 Research | ryanne.ross@tlgcohort.com"""


#std library imports
import shutil #shell utilities will be used to move files
import os #provides access to low level operations


os.chdir('/home/student/mycode/')

shutil.move('raynor.obj', 'ceph_storage/')

xname = input('What is the new name for kerrigan.obj? ')

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

