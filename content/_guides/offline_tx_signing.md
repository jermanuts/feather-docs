---
title: Offline transaction signing
nav_title: Offline transaction signing
category: advanced
---

Offline transaction signing is a method of signing transactions without exposing the private spend key to a computer that is connected to the internet. Conceptually, it is similar to how a hardware wallet functions, except the process is done manually.

Two devices are required: one device connected to the internet that hosts a view-only wallet ("the online device"), and a second [airgapped](https://en.wikipedia.org/wiki/Air_gap_%28networking%29) device that hosts a corresponding wallet containing the secret spendkey ("the offline device"). The offline device is typically a laptop or desktop computer stripped of any network interfaces that is used exclusively for the purpose of offline transaction signing.

The procurement and setup of the offline device is outside of the scope of this guide. However, we recommend installing a lightweight linux distribution with an [encrypted filesystem](https://wiki.archlinux.org/title/Dm-crypt/Encrypting_an_entire_system) on the offline device.

Transactions are constructed using the view-only wallet on the online device, then signed with the spendable wallet on the offline device and later broadcast to the network using the view-only wallet on the online device or via another means such as a [transaction pusher](https://xmrchain.net/rawtx).

Common ways to transfer files between computers are: USB flash drives, SD cards or QR Codes. In this guide we will assume files will be transferred between devices using files on a flash drive.

## Initial Setup

### Create a new offline wallet

On an offline device, [create a new wallet](create-wallet).

Go to **Wallet → View-Only**. Save the following information to a text file on your flash drive:

- Restore height
- Primary address
- Secret view key

Click **Copy** to copy all required information to your clipboard.

### Create a new view-only wallet

On the online device, follow the steps [here](create-view-only-wallet) to create a view-only wallet using the information saved in the previous step.

## Syncing the wallets

After the wallet has received a transaction it is necessary to sync the wallets.

You can check if syncing is needed by going to the **Coins** tab on the view-only wallet. If there are coins that show a crossed-out eye symbol, syncing is needed.

Follow the steps below to sync the wallets.

#### Export outputs

On the view-only wallet, go to **Wallet → Advanced → Export → Outputs**. Save the file on the flash drive.

#### Import outputs

Transfer the flash drive to the **offline** device.

On the offline wallet, go to **Wallet → Advanced → Import → Outputs**. Select the file saved in the previous step.

#### Export Key Images

On the offline wallet, go to **Wallet → Advanced → Export → Key Images**. Save the file on the flash drive.

#### Import Key Images

Transfer the flash drive to the **online** device.

On the view-only wallet, go to **Wallet → Advanced → Import → Key Images**. Select the file saved in the previous step.

Go to the **Coins** tab, and make sure all outputs have an eye symbol.


## Sending a transaction

### Construction

[Create a transaction](create-transaction) on the view-only wallet.

Click on **Export unsigned → Save to File**. Save the file to the flash drive.

### Signing

Unmount the flash drive and plug it into the offline machine.

Go to **Tools → Load unsigned transaction → From file**. Select the unsigned transaction created in the previous step.

Verify the details. Click **Sign**, save the signed transaction to the flash drive.

### Broadcasting

Unmount the flash drive and plug into the online device.

Go to **Tools → Broadcast transaction → From file**. Select the signed transaction created in the previous step.

Verify the transaction details. Click **Send** to broadcast the transaction.

After the transcation has received at least 1 confirmation, re-sync the wallets using the steps above.
