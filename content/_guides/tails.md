---
title: Installing Feather on Tails
nav_title: Tails
category: installation
weight: 200
---

Installation will only take a few minutes to complete. 

The estimated storage requirement is ~30 MB.

## Configuring the persistent volume

Tails is an amnesic operating system. By default, files are not saved to your USB drive and are thus lost after the computer is restarted. Only files stored on the _persistent volume_ are kept across different working sessions.

We strongly recommend that you store Feather on the persistent volume. This way, you won't have to reinstall Feather and restore your wallets each time you start Tails.

You need to configure the persistent volume before you can use it. If you have already configured the persistent volume, skip ahead to the next section.

Go to **Applications → System Tools → Configure persistent volume**.

Enter a strong password to protect the persistent volume. Files on the persistent volume are encrypted with your password. 

Follow through the remaining screens. You do not need to enable any additional settings.

You must restart Tails before you can continue with the installation. When you get to the Tails greeter enter your password to unlock the persistent volume.

The persistent volume will show up in the File Browser as a folder named `Persistent`. You can quickly access it from the sidebar.

## Downloading Feather

Download the latest AppImage for Tails from [featherwallet.org/download](https://featherwallet.org/download). 

- Tip: Save the file to the default location. Tor Browser on Tails does not have access to other folders.

After the download is complete, move the AppImage to a folder within your persistent volume (Home → Persistent).

## Verifying the download (optional)

This section describes how to verify the AppImage file using PGP.

Download the release signing key from the [git repository](https://raw.githubusercontent.com/feather-wallet/feather/master/utils/pubkeys/featherwallet.asc).

To save the file from Tor Browser: right click **→ Save Page As.. → Save**.

In the file browser, right click on `featherwallet.asc` **→ Open with Import Key**. You will see a notification displaying that key was imported successfully.

In the menu bar go to **Applications → Utilities → Passwords and Keys**. 

In the column on the left select "GnuPG keys". Locate the key named "FeatherWallet" and double click it. Go the "Details" tab. Make sure the **fingerprint** matches:

```
8185 E158 A333 30C7 FD61 BC0D 1F76 E155 CEFB A71C
```

If the fingerprint does not match, do not continue the installation. Instead, [report](report-an-issue) this incident to the developers.

Go back to [featherwallet.org/download](https://featherwallet.org/download) and download the **signature** file for the Tails AppImage. After the download is complete, place the file in the same directory as the AppImage.

In the file browser, right click on the `.asc` file **→ Open with Verify Signature**. If the signature is valid, you will see a notication pop up containing the text "Valid but untrusted signature by FeatherWallet".

If the signature is invalid, do not continue with the installation. Instead, [report](report-an-issue) this incident to the developers immediately.

After verification is complete you can delete the `.asc` file.

## Starting Feather

Right click on the AppImage **→ Properties → Permissions**. Make sure "Allow executing file as program" is enabled. You will only have to do this once.

To start Feather simply double click on the AppImage. If the program doesn't start, try right click **→ Run**.

Having trouble getting Feather to start? Please [contact](report-an-issue) the developers.
