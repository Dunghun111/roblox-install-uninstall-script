import os
import sys
import time

BROWSER = sys.argv
if len(BROWSER) > 2:
    print('You can\'t run 2 browser at the same time')
if len(BROWSER) <= 0:
    print('''Support browser:
Brave
Chromium
Google Chrome''')
else:
    print('Starting...')
    time.sleep(1)
    os.system(f'python3 ~/launcher_dir/runRoblox.py {BROWSER[1]}')
