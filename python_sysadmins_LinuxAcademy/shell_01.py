#!/usr/bin/python

import subprocess
try:
    output = subprocess.check_output("ls", stderr=subprocess.STDOUT)
except OSError as err:
    print ("Caught OSError")
    output = err
except subprocess.CalledProcessError as err:
    print ("Caught subprocess.CalledProcessError")
    output = err

print (output)