import os


def install_dependencies_and_add_i386_architecture():
    os.system('wget -O - https://dl.winehq.org/wine-builds/winehq.key | sudo apt-key add -')
    os.system('sudo dpkg --add-architecture i386')
    os.system('sudo apt-add-repository "deb https://dl.winehq.org/wine-builds/ubuntu/ focal main"')
    os.system('sudo apt update')
    os.system('sudo apt-get install winehq-staging git -y')


def roblox_install():
    os.system('git clone https://github.com/Dunghun111/Roblox-Linux-Launcher.git ~/launcher_dir')
    os.system('wine RobloxPlayerLauncher.exe')
    os.system('sudo cp ~/roblox-install-uninstall-script/runRoblox.py /usr/bin/Roblox')
    os.system('sudo cp ~/roblox-install-uninstall-script/runRoblox.py /usr/bin/roblox')

