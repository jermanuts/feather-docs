---
title: Seed scheme
nav_title: Seed scheme
category: faq
---

Feather uses the [monero-seed](https://github.com/tevador/monero-seed) library written by Tevador, for 14 word mnemonic seeds.

The discussion that lead to its creation can be found [here](https://github.com/monero-project/monero/issues/6639).

Feather can restore wallets from both 14 word and 25 word seeds.

This seed scheme has a number of advantages over Monero core's seed scheme:

- The wallet creation date is embedded in the mnemonic seed. This way you no longer have to worry about restoring your wallet from the correct restore height.
- It uses BIP-39 wordlists. These wordlists container shorter and more common words than Monero's lists.
- 14 word seeds are quicker to write down and memorize.

### Supported languages

|Language| 14-word (BIP-39) | 25-word (Monero)|
|--------|------------------|-----------------|
|English |✔|✔|
|Japanese|✔|✔|
|Korean|✔|✖|
|Spanish|✔|✔|
|Chinese (simplified)|✔|✔|
|Chinese (traditional)|✔|✖|
|French|✔|✔|
|Italian|✔|✔|
|Czech|✔|✖|
|Portugese|✔|✖|
|Dutch|✖|✔|
|Esperanto|✖|✔|
|German|✖|✔|

**Note**: as of 1.0.0 only English is supported for 14 word seeds.

All BIP-39 wordlists can be found [here](https://github.com/bitcoin/bips/blob/master/bip-0039/bip-0039-wordlists.md).

### Convert 14-word seed into 25-word seed

Go to **Wallet → Seed**, enter your password, and check **Show 25 word seed**. Make sure to also note the restore height to make restoring the wallet faster.

### Convert 25-word seed into 14-word seed

This is not possible. The 14-word seed scheme uses a [KDF](https://en.wikipedia.org/wiki/Key_derivation_function) to derive the actual spendkey, this operation is non-reversible.

### Second seed word is always "poet", is this a bug?

No. In addition to the private spend key, Tevador's seed scheme also encodes the restore date, cryptocurrency type, and reserves a few bits for future use. The second word is static because some of the reserved bits remain the same for each seed generation.
