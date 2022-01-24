# roblox-intall-uninstall-script
  - install and uninstall roblox
  - Instruction:
  - 	Download Roblox Launcher from Roblox
  - 	Commands (change [path to roblox] to path to robloxplayerlauncher e.g: ~/Donwnloads/RobloxPlayerLauncher.exe):
        
        git clone https://github.com/Dunghun111/roblox-install-uninstall-script ~/roblox-install-uninstall-script
        cp [path to roblox]/RobloxPlayerLauncher.exe ~/roblox-install-uninstall-script
        cd ~/roblox-install-uninstall-script
        python3 install-and-uninstall.py
        
# Credit
  - roblox-player-launcher: https://github.com/PJBeans/Roblox-Linux-Launcher made by PJBeans and his contributor

# Note:
  - 	For people can't launch install-and-uninstall.py try change in installFramework:

			    os.system('git clone https://github.com/Dunghun111/Roblox-Linux-Launcher.git ~/launcher_dir')

	- To:
					os.system('git clone https://github.com/PJBeans/Roblox-Linux-Launcher ~/launcher_dir')
