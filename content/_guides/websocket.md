---
title: Websocket
nav_title: Websocket
category: faq
---

The websocket server is a service hosted by the Feather developers that provides Feather Wallet clients with data from third party services.

It is used by the wallet to obtain pricing information, CCS & Reddit feeds, a curated list of remote nodes, the latest version of Feather Wallet and more. For more details view the table below.

The websocket server is only used to fetch information. The wallet does not send information about its state or the transactions you send to the websocket server. It is not used for any telemetry or crash reports. The wallet does not send an unique client id.

The websocket server is only accessible via a v3 onion service, as such the wallet always uses Tor to connect to it. This way your IP Address is not leaked to the websocket server.

This architecture was chosen for the simple reason that connecting to a single hidden service leaks significantly less metadata to third parties than connecting to  multiple clearnet services over Tor. 

When Feather starts it requests all available data. Clients cannot be fingerprinted based on their configuration. The server pushes updates when they become available.

The Feather developers can infer no information about any client, apart from:

- The total number of active connections to the websocket server.
- The time at which a client connects or disconnects
- Whether or not a client has previously connected

None of the above is actively tracked or recorded on the server.

The websocket server cannot make the client show arbitrary messages.

As of `1.0.0` it is not possible to disable the websocket connection. We recognize that users with exceptionally high treat models want to minimize their attack surface as much as possible. To accomodate this, we will allow compiling Feather without websocket support as well as add an option to disable it in the settings in a future release.


The following data is provided by the websocket server:

|key                        |description|
|---------------------------|---------|
|blockheights               |Current mainnet and stagenet blockheights. Used to speed up initial synchronization of newly created wallets.|
|nodes                      |A curated list of high-performance nodes run by trusted members of the community. Includes status information such as their current blockheight.|
|crypto_rates               |Crypto exchange rates. Obtained from CoinGecko. |
|fiat_rates                 |Fiat exchange rates |
|reddit                     |Latest Reddit posts in /r/Monero. Displayed on the Home screen.|
|ccs                        |Proposals in the Community Crowdfunding System that require funding. Displayed on the Home screen.|
|txFiatHistory              |Historical fiat prices|
|updates                    |Latest Feather version |
|xmrig                      |Latest xmrig downloads |
|localmonero_countries      |List of countries supported by LocalMonero|
|localmonero_currencies     |List of currencies supported by LocalMonero|
|localmonero_payment_methods|List of payment methods supported by LocalMonero|

