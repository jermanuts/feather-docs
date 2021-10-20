---
title: Network Traffic
nav_title: Network Traffic
category: faq
---

This section provides an overview of the ways Feather can make network connections.


| To / Feature                 | Description                                                | Always over Tor | Handled by |
|------------------------------|------------------------------------------------------------|-----------------|------------|
| [Node](nodes)                | Synchronization, transaction construction                  | Optional<sup>[0]</sup>        | epee       |
| [Websocket](websocket)       | Fiat price, Reddit, CCS, current blockheight               | Yes             | Qt         |
| [Built-in updater](updater)  | Contacts featherwallet.org if a new update is available. Depends on websocket.    | Yes             | Qt         |
| [Local Monero](exchanges)    | Contacts LocalMonero's v3 address only if a search is initiated in the Local Monero tab.| Yes | Qt |
| [Mining](mining-setup)       | Connection to mining pool, only if pool mining.            | Optional<sup>[1]</sup> | Qt |

(0) = configurable when Feather starts for the first time and in Tor settings, see [Tor support](tor-support) for more information.  
(1) = configurable in the mining settings, see [Setup mining](mining-setup) for more information.  
