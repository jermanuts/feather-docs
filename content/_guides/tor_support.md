---
title: Tor support
nav_title: Tor support
category: faq
---

Feather works with Tor out of the box. You don't have to manually install Tor to use it.

Feather releases are bundled with a Tor binary. If the presence of a local Tor daemon on the default port (9050) is not detected, Feather will place the bundled Tor binary in the [config folder](paths) and run it on port 19450.

If you are unable to connect to the Tor network on your machine, some wallet functionality will not work. For instance, Feather will be unable to obtain fiat prices, crowdfunding proposals, Reddit posts and other data from the [websocket](websocket) server.

Feather can be configured to handle network traffic in three different ways:

- Route all traffic over Tor, except traffic to node
- Route all traffic over Tor, except wallet synchronization (**default**)
- Route all traffic over Tor

You have the option to select the desired mode when Feather is started for the first time **before** any network connections are made. You can also change the mode in the **Tor settings** dialog (click the Tor icon in the status bar).

By default, Feather routes all network traffic over Tor, except for wallet synchronization. Synchronization requires a lot of data transfer and is therefore very slow over Tor. A remote node does not learn much about your wallet during synchronization (for more information see [Nodes](nodes)). We believe this is a reasonable privacy / convenience trade-off.

On Tails, Whonix, or when Feather is started with `torsocks`, all traffic is routed through Tor regardless of application configuration. Traffic to a [local node](local-node) is never routed over Tor.

