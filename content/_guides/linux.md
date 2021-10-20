---
title: Installing Feather on Linux
nav_title: Linux
category: installation
weight: 100
---

Using **TailsOS?** See the instructions [here](tails) instead.

## AppImage

Download the latest AppImage for Linux from [featherwallet.org/download](https://featherwallet.org/download).

After the download is complete, **make sure to allow executing the file as a program**. You can often find this setting in the Properties → Permissions tab in your file explorer. Alternatively, run `chmod +x feather-x.x.x.AppImage` in a terminal.

You should now be able to run the AppImage by double clicking on the file in a file explorer. If that does not work, try right clicking on the file, and look for "Run" or "Open". Alternatively, you can start Feather by typing `./feather-x.x.x.AppImage` in a terminal.

Having trouble getting Feather to start? Please [contact](report-an-issue) the developers.

---

## Arch Linux

Feather is available on the [AUR](https://aur.archlinux.org/packages/monero-feather-git).

### Installation with yay

```bash
yay -S monero-feather-git
```

### Manually

```bash
git clone https://aur.archlinux.org/monero-feather-git.git
cd monero-feather-git
makepkg -si
```

--- 

Want to help package Feather for your distribution? Join us in `#feather` on OFTC.
