---
title: Transaction Fee
nav_title: Transaction Fee
category: faq
---

Feather automatically adjusts the transaction fee based on the number of transactions in the [mempool](glossary). This behavior is identical to the “automatic” fee option in the GUI.

#### Can I manually adjust the transaction fee?

It is not currently possible to manually adjust the transaction fee in Feather.

Transaction fees are visible on the blockchain, therefore setting it manually can make your transaction stick out and harm your privacy. In the interest of transaction uniformity, we have decided to not add this feature at this time.

Besides, paying a higher than normal fee usually has no impact on the time it takes for your transaction to get confirmed. This is because Monero blocks are usually not full and thus there is no competition for block space. Transactions paying the minimum fee will almost always get included in 1 or 2 blocks.


#### My outgoing transaction still hasn't confirmed, what can I do?

First, make sure the transaction shows up in a block explorer. You can do this by entering the txid into [xmrchain.net](https://xmrchain.net).

If the transaction does not show up, try rebroadcasting the transaction by following the steps [here](failed-tx).

If the transaction shows up, all you can do is wait. Your transaction should be included in a block soon, unless an atypical network event is ongoing (e.g. spam attack, network upgrade, etc). Check any of the Monero community hangouts for more information.

#### Who receives the transaction fee?

The fee is paid to the miner that mines the block that includes the transaction. The Feather developers do not take a cut from the transaction fee.
