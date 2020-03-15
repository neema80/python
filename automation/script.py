import subprocess
# to import useful modules using operating system
# this command is repeating python example.py 5 times
for i in range (5):
    subprocess.check_call(['python','example.py'])