---
title: Feature comparison
nav_title: Feature comparison
category: faq
---

Feature comparison between Monero desktop wallets.

| Feature                                                                                     | Feather                  | CLI             | GUI             |
|---------------------------------------------------------------------------------------------|--------------------------|-----------------|-----------------|
| **► The Basics**                                                                            |
| [Subaddress accounts](switch-subaddress-account)                                            | ✔                        | ✔               | ✔               |
| [Contacts](add-contact)                                                                     | ✔                        | ✔               | ✔               |
| Dark mode                                                                                   | ✔                        | ✔               | ✔               |
| [View-only wallet](create-view-only-wallet)                                                 | ✔                        | ✔               | ✔               |
| Language localisation                                                                       | ✖*                       | ✔               | ✔               |
| Wallet implementation                                                                       | `wallet2` <sup>[0]</sup> | `wallet2`       | `wallet2`       |
| **► Seed & Keys**                                                                           |
| Export secret keys                                                                          | ✔                        | ✔               | ✔               |
| [Seed scheme](seed-scheme)                                                                  | Polyseed <sup>[1]</sup>  | 25              | 25              |
| Supported seed languages                                                                    | 10 <sup>[2]</sup>        | 12              | 12              |
| **► Privacy & Security**                                                                    |
| [Built-in Tor](tor-support)                                                                 | ✔                        | ✖               | ✖               |
| Socks5 proxy support                                                                        | ✔<sup>[3]</sup>          | ✔<sup>[3]</sup> | ✔<sup>[3]</sup> |
| Address re-use mitigation                                                                   | ✔                        | ✔               | ✖               |
| [Encrypted wallet files](wallet-files)                                                      | ✔                        | ✔               | ✔               |
| [Reproducible builds](building-from-source)                                                 | ✔                        | ✔               | ✔<sup>[4]</sup> |
| [Bootstrappable builds](https://github.com/feather-wallet/feather/tree/master/contrib/guix) | ✔                        | ✖               | ✖               |
| Hide balance                                                                                | ✔                        | ✖               | ✔               |
| Output blackballing                                                                         | ✖                        | ✔               | ✔               |
| Lock on inactivity                                                                          | ✔                        | ✔               | ✔               |
| Lock on minimize                                                                            | ✔                        | ✖               | ✖               |
| **► Proofs / Messages**                                                                     |
| [Sign/verify message](sign-verify-message)                                                  | ✔                        | ✔               | ✔               |
| [Verify transaction proof](verify-tx-proof)                                                 | ✔                        | ✔               | ✔               |
| [Formatted transaction proofs](formatted-tx-proofs)                                         | ✔                        | ✖               | ✖               |
| [Create SpendProof](prove-tx-authorship)                                                    | ✔                        | ✔               | ✔               |
| [Create OutProof](prove-payment)                                                            | ✔                        | ✔               | ✔               |
| Create InProof                                                                              | ✔                        | ✔               | ✖               |
| Create ReserveProof                                                                         | ✖*                       | ✔               | ✖               |
| **► Coin Control**                                                                          |
| Freeze/Thaw                                                                                 | ✔                        | ✔               | ✖               |
| [Sweep single](sweep-output)                                                                | ✔                        | ✔               | ✖               |
| Sweep multi (selected)                                                                      | ✔                        | ✖               | ✖               |
| Sweep all                                                                                   | ✔                        | ✔               | ✖               |
| Output splitting                                                                            | ✔                        | ✔               | ✖               |
| Manual input selection                                                                      | ✔                        | ✖               | ✖               |
| Coin labeling                                                                               | ✔                        | ✖               | ✖               |
| **► Transactions**                                                                          |
| [Multi-destination transactions](pay-to-many)                                               | ✔                        | ✔               | ✔               |
| [Transaction pusher](push-tx)                                                               | ✔                        | ✖               | ✖               |
| [Manual transaction import](missing-tx)                                                     | ✔                        | ✔               | ✔               |
| [Transaction rebroadcasting](failed-tx)                                                     | ✔                        | ✖               | ✖               |
| Multibroadcasting                                                                           | ✔                        | ✖               | ✖               |
| [Offline transaction signing](offline-tx-signing)                                           | ✔                        | ✔               | ✔               |
| ... using animated QR codes                                                                 | ✔                        | ✖               | ✖               |
| Transaction unlock time                                                                     | ✖†                       | ✔               | ✖               |
| Automatic network fee adjustment                                                            | ✔                        | ✔               | ✔               |
| Manual fee-tier selection                                                                   | ✔                        | ✔               | ✔               |
| Multisig                                                                                    | ✖*                       | ✔               | ✖               |
| **► Mining**                                                                                |
| Solo mining                                                                                 | ✔<sup>[6]</sup>          | ✔               | ✔               |
| [Pool mining](mining-setup)                                                                 | ✔<sup>[6]</sup>          | ✖               | ✖               |
| P2Pool                                                                                      | ✖*                       | ✖               | ✔               |
| **► Hardware wallets**                                                                      |
| Ledger Nano S/S+/X                                                                          | ✔                        | ✔               | ✔               |
| Trezor Model T/Safe 3                                                                       | ✔                        | ✔               | ✔               |
| **► Fiat**                                                                                  |
| Crypto/fiat calculator                                                                      | ✔                        | ✖               | ✖               |
| Historical fiat prices                                                                      | ✔                        | ✖               | ✖               |
| Fiat balance display                                                                        | ✔                        | ✖               | ✔               |
| **► Misc**                                                                                  |
| Built-in updater                                                                            | ✔                        | ✖               | ✔               |
| Wallet autosave                                                                             | ✔                        | ✖               | ✔               |
| [Webcam QR code scanner](webcam-qr-scanner)                                                 | ✔                        | ✖               | ✔<sup>[7]</sup> |
| [Export history as CSV](export-tx-history)                                                  | ✔                        | ✔               | ✔               |
| Auto-open passwordless wallets                                                              | ✔                        | ✖               | ✖               |
| Copy-pasteable support template                                                             | ✔                        | ✖               | ✖               |
| Open multiple wallets in single instance                                                    | ✔                        | ✖               | ✖               |
| Extra entropy from dice rolls                                                               | ✔                        | ✖               | ✖               |
| Mass address export                                                                         | ✖*                       | ✖               | ✖               |
| Atomic swaps                                                                                | ✖*                       | ✖               | ✖               |
| Adjustable subaddress lookahead                                                             | ✔                        | ✔               | ✔<sup>[8]</sup> |
| Local node manager                                                                          | ✖                        | ✖               | ✔               |
| Merchant mode                                                                               | ✖†                       | ✖               | ✔               |

**\*** = not yet  
**†** = no plans to support  
(0) = with modifications (see the feature branches for [feather/monero](https://github.com/feather-wallet/monero))  
(1) = Feather also supports restoring 14 and 25 word seeds.  
(2) = Polyseed uses BIP-39 wordlists, for Monero see [here](https://github.com/monero-project/monero/tree/master/src/mnemonics). As of 1.0.0 only English is supported for Polyseed.  
(3) = authentication not supported  
(4) = except macOS  
(6) = with 𝐗𝐌𝐑𝐢𝐠  
(7) = except Linux release  
(8) = only for hardware wallets  

Missing something? [Let us know](report-an-issue).
