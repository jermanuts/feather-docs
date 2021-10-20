---
title: "Help: missing transaction"
nav_title: Missing transaction
category: troubleshooting
---

Use this guide if you are expecting an incoming transaction, but it hasn't shown up yet.

### Is your wallet up-to-date?

Some Monero protocol updates are backwards incompatible, old wallet versions stop working eventually. New wallet versions may also contain important bugfixes and security updates.

You can find your current Feather version in **Help → About**.

You can find the latest version of Feather on [featherwallet.org/download](https://featherwallet.org/download).

On most operating systems you can use the [built-in updater](updater) to update to the latest version. To upgrade manually, see the installation guide for your specific operating system at the top of these docs.

### Is your wallet synchronized?

The wallet needs to scan the blockchain to find your transactions. The statusbar will tell you how many blocks are still remaining. Wait for this process to complete.

The statusbar will show "Synchronized" when the wallet is synchronized.

For more information, see [Synchronization](synchronization).

### Does the transaction show up on a block explorer?

Go to a public block explorer (e.g. [xmrchain.net](https://xmrchain.net)) and search for the transaction. If it doesn't show up the transaction wasn't relayed properly, contact the sender to notify them of the issue.

If the transaction was sent using Feather, the sender may [rebroadcast](failed-tx) the transaction to resolve the issue.

### Manually import the transaction

If the transaction shows up on a block explorer, follow the steps to [manually import your transaction](import-transaction).
