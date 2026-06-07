# Debian dots ;3


## Architecture Overview

requirements:

* **Base Layer:** Debian
* **Window Manager:** Qtile
* **Shell Environment:** Zsh
* **Terminal Emulator:** Alacritty
* **X11 Compositor:** Picom
* **File Management:** Ranger
* **Application Launcher:** dmenu
* **Typography:** Iosevka Nerd Font

---

## Prerequisites and Dependency Installation

to install, you need to grab the dependancies first:

```bash
doas apt update && doas apt install -y \
  xinit xserver-xorg xserver-xorg-core xauth xclip xinput \
  qtile picom rofi xwallpaper scrot notification-daemon \
  alacritty zsh zsh-autosuggestions zsh-syntax-highlighting \
  ranger neovim htop fastfetch tree \
  pipewire pipewire-pulse wireplumber pavucontrol \
  chromium firefox-esr wpasupplicant curl wget \
  doas opendoas build-essential git nsxiv w3m-img
```
once installed, just copy this repo and paste the folders into .config, and **.zshrc** into *~*.

then, run these commands to make sure *zsh* and the *font* is present or wtv:

```bash
fc-cache -fv
chsh -s $(which zsh)
```
