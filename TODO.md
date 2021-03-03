#SoySauce a Arch Linux Distro
##TODO:
###Calamares:
###ArchISO:
###Configuration:
- [ ] System Information : Image, OS name, etc, (neofetch data)
- [ ] OpenBox config/daemon
- [ ] compton daemon
- [ ] polybar run with vm https://wiki.archlinux.org/index.php/Polybar#Running_with_WM
- [ ] lxdm daemon
- [ ] plymouth hooks
###Desktop Environment:
- [x] Window Mangaer: OpenBox
- [x] Display Server: Xorg
- [x] Compositor: Compton?
- [x] Status Bar: Polybar
- [ ] Menus: Rofi?
- [x] Program Menu: DMenu
- [x] Login Manger: LXDM?
- [x] Boot Screen: Plymouth
- [x] File Explorer: Dolphin
- [x] Terminal Emulator:Termite?
- [x] System Monitor:Gnome
- [x] Torrent: Transmission
- [x] Editor: Notepadqq
- [x] Drive Manager: Gparted
- [x] Qt Theme: Kvantum Manager
- [x] GTK Theme: LXappearance
- [x] System Theme: Pywall
- [x] Wallpaper: Nitrogen?
- [x] Lightweight Browser: Qutebrowser?
- [x] Notifications: Dunst
- [ ] Installer: Calamares
###Packages:
####Networking/Bluetooth:
iproute2
networkmanager: https://wiki.archlinux.org/index.php/NetworkManager#Front-ends
network-manager-applet: network manager front end
bluez: bluetooth
bluez-utills: bluetooth
####CLI Tools:
nano
vim
ranger: file manager
####Power Management:
tlp: https://wiki.archlinux.org/index.php/TLP
####Sound:
alsa is built into kernel modules https://wiki.archlinux.org/index.php/Advanced_Linux_Sound_Architecture#Installation
alsa-utils
alsa-firmware #certain sound cards
sof-firmware #laptop sound open firmware
alsa-ucm-conf #laptop sound open firmware
pulseaudio #GUI https://wiki.archlinux.org/index.php/PulseAudio#Installation
pulseaudio-alsa
pulseaudio-bluetooth
pulseaudio-equalizer
lib32-libpulse #32-bit multilib support (wine/steam)
lib32-alsa-plugins #32-bit multilib support (wine/steam)

####Drive Management:
####Boot:
brub: https://wiki.archlinux.org/index.php/GRUB
plymouth (AUR): https://wiki.archlinux.org/index.php/Plymouth#Installation
XDG Autostart?