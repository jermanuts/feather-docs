---
title: Installing Feather on Raspberry Pi
nav_title: Raspberry Pi
category: installation
weight: 200
---

Installation will only take a few minutes to complete. 

The estimated storage requirement is ~30 MB.

## Requirements

Before beginning the installation procedure, please check if your model is supported.

**Minimum system requirements**: ARMv7 or higher CPU, 512 MB (1 GB+ recommended) RAM, 2 or more cores recommeded.

| Model | Core Type | No. of Cores | RAM | Supported |
|-------|-----------|--------------|-----|-----------|
| 4 B   | Cortex-A72 (ARMv8)    | 4 | 1,2,4,8 GB | ✔️* |
| 3 B+  | Cortex-A53 (ARMv8)    | 4 | 1 GB, 2 GB | ✔️ |
| 3 A+  | Cortex-A53 (ARMv8)    | 4 | 512 MB | ✔️* |
| 3     | Cortex-A53 (ARMv8)    | 4 | 1 GB | ✔️* |
| 2     | Cortex-A7 (ARMv7)     | 4 | 1 GB | ✔️* |
| B+    | ARM1176JZF-S (ARMv6)  | 1 | 512 MB | ❌ |
| B     | ARM1176JZF-S (ARMv6)  | 1 | 256 MB | ❌ |
| Zero 2 W | Cortex-A53 (ARMv8) | 4 | 512 MB  | ✔️* |
| Zero (W,WH) | BCM2835 (ARMv6) | 1 | 512 MB  | ❌ |

\* = not tested ([let us know](report-an-issue)!)

## Downloading Feather

Download the latest AppImage for Raspberry Pi from [featherwallet.org/download](https://featherwallet.org/download). 

## Starting Feather

Right click on the AppImage **→ Properties → Permissions**. Set "Execute" to "Anyone", close the window.

Again, right click on the AppImage **→ Open With → Accessories → Terminal**.

To start Feather, right click on the AppImage **→ Open**. Then click **Execute** if prompted.

Having trouble getting Feather to start? Please [contact](report-an-issue) the developers.
