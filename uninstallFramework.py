import os


def uninstall_roblox():
    os.system('sudo rm -rf ~/launcher_dir')
    os.system('sudo rm -rf ~/usr/bin/roblox ~/usr/bin/Roblox')
    os.system('sudo rm -rf ~/.wine/drive_c/users/$USER/AppData/Local/Roblox')
    os.system('sudo rm -rf ~/.wine/drive_c/users/$USER/AppData/LocalLow/rbxcsettings.rbx')


def uninstall_dependencies():
    os.system('sudo apt remove winehq-staging git')
    os.system('sudo rm -rf ~/.wine')


def remove_i386_arch():
    os.system('sudo dpkg --remove-architecture i386')
