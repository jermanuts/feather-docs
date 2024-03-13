---
title: Wallet cache viewer
nav_title: Wallet cache viewer
category: advanced
---

This feature is intended for developers and Monero users curious to learn more about the internal datastructure of `wallet2`.

**Caution**: This dialog can display sensitive information.

To access the wallet cache viewer go to **Wallet → Advanced → Wallet cache debug**.

### Overview:

|datastructure|description|
|-------------|-----------|
|m_blockchain|List of blockhashes. |
|m_transfers| Outputs we have received. Shown in the Coins tab. |
|m_key_images| Key image cache. Map: key image → m_transfers index. Sorted by index for readability. |
|m_pub_keys | Pub key cache. Map: pub key → m_transfers index. Sorted by index for readability. |
|m_address_book| Contacts. Shown in the Send tab. |
|m_unconfirmed_payments| Unconfirmed incoming transactions. |
|m_payments| Confirmed incoming transactions. |
|m_unconfirmed_txs | Unconfirmed outgoing transactions. |
|m_confirmed_txs | Confirmed outgoing transactions. |
|m_tx_keys | Map: txid → tx key. |
|m_additional_tx_keys | List of additional tx keys for each outgoing tx |
|m_tx_notes | Transaction descriptions |
|m_scanned_pool_txs | List of mempool transactions we have already scanned. |
|m_subaddresses| Map: address key → \<major index\>,\<minor index\> |
|m_subaddress_labels| Map: \<major index\>,\<minor index\> → label |
|m_account_tags| Account labels. Map: \<account index\> → label |
|m_attributes| Custom wallet attributes. Map: str → str |

Datastructures not displayed in the viewer:

`m_account_public_address`, `m_ring_history_saved`, `m_last_block_reward`, `m_tx_device`, `m_device_last_key_image_sync`, `m_cold_key_images`, `m_rpc_client_secret_key`.

### Feather wallet attributes:

- `feather.seed`: backup copy of the wallet's [Polyseed](seed-scheme)
- `feather.seedoffset`: seed offset passphrase
- `feather.hiddenaddresses`: comma delimited list of hidden subaddresses.
- `feather.𝐗𝐌𝐑𝐢𝐠_username`: receiving address in mining settings
- `feather.𝐗𝐌𝐑𝐢𝐠_password`: password for mining pool
- `feather.subaddress_account`: index of selected subaddress account
- `tx:<txid>`: hexstring of outgoing transaction
