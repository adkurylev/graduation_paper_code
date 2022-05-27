import subprocess
import os
import datetime
from time import sleep

input_files = sorted(os.listdir("./input"), key=lambda name: -int(name.split('_')[0]))
processed_blocks_numbers = list(map(lambda x: x.split('_')[0], os.listdir("./output")))

path = '../'

count = 0

for f in input_files:
    if f.split('_')[0] in processed_blocks_numbers:
        print(f"{f} already processed")
        # os.remove('./input/'+f)
        continue

    with open("./Info files/log.txt", "a+") as log:
        logstr = f"File {f} started at {datetime.datetime.now().strftime('%H:%M:%S')}"
        log.write(logstr + "\n")
        print(logstr)
        
    subprocess.call(['gnome-terminal', '--', f'{path}a.out', f'input/{f}', f'output/{f.split("_")[0] + "_output.txt"}', '10'])
    count += 1

    if count > 20:
        count = 0
        sleep(240)

print("Everything was processed")