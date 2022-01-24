import os
import sys
import time

from installFramework import *
from uninstallFramework import *

dir_list = []
if os.getuid() == 0:
    print('Don\'t run in root!')
    sys.exit()

else:
    pass

os.system('mkdir ~/launcher_dir')


if len(os.listdir(os.path.expanduser('~/launcher_dir'))) == 0:
    print('''We are going to add i386 architecture, install wine and git.
If you already done 2 of these, this will do nothing!''')
    install_dependencies_and_add_i386_architecture()
    print('Now we\'ll install Roblox')
    roblox_install()
    os.system('python3 ~/launcher_dir/runRoblox.py')
    print('Done! Now type \'Roblox\' or \'roblox\' in your terminal to launcher roblox launcher.')
    print('''If you see this script is good, take a look at this script:
'https://github.com/PJBeans/Roblox-Linux-Launcher'
This help me to launch roblox on my GNU/Linux laptop.
This will auto close in 10 second''')
    time.sleep(10)

else:
    answer = input('Uninstall Roblox? (y/N): ')
    if answer.lower() == 'y':
        uninstall_roblox()

    answer = input('Uninstall dependencies? (y/N): ')
    if answer.lower() == 'y':
        uninstall_dependencies()

    answer = input('Remove 32-bit architecture? (y/N):')
    if answer.lower() == 'y':
        remove_i386_arch()
