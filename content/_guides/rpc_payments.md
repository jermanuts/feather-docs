---
title: RPC Payments
nav_title: RPC Payments
category: faq
---

Feather does not support [RPC Payments](https://github.com/monero-project/monero/commit/2899379791b7542e4eb920b5d9d58cf232806937). This feature will not be implemented.

#### Rationale

- RPC Pay requires RandomX mining code to be present in the program file, which frequently triggers false positives from anti-virus software.
- There is a large overlap between users that aren't able to run their own node (due to network, storage, battery, cpu limitations) and users that are unable to mine on their machine, making the use-case for this feature unclear. 
- Presently a large number of high performance node are freely available.
