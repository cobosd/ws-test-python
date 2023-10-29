import subprocess

proc = subprocess.Popen(['~/dump1090/dump1090'], stdout=subprocess.PIPE)
while True:
    line = proc.stdout.readline()
    if not line:
        break
    print(line.strip())
