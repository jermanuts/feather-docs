---
title: Obtaining the release signing key
nav_title: Release signing key
category: advanced
---

You may obtain the release signing key from:

- The git repository hosted on [GitHub](https://raw.githubusercontent.com/feather-wallet/feather/master/utils/pubkeys/featherwallet.asc)
- [keys.openpgp.org](https://keys.openpgp.org) (search for `dev@featherwallet.org`)
  - `gpg --keyserver hkps://keys.openpgp.org --search dev@featherwallet.org`
- Ubuntu's [SKS keyserver](https://keyserver.ubuntu.com/pks/lookup?search=dev%40featherwallet.org&fingerprint=on&op=index)
  - `gpg --keyserver hkps://keyserver.ubuntu.com --search dev@featherwallet.org`
- [featherwallet.org](https://featherwallet.org/files/featherwallet.asc)

After importing the key, verify that fingerprint matches: `8185E158A33330C7FD61BC0D1F76E155CEFBA71C`

We recommend that you cross-check the fingerprint shown above through the domains listed below. By cross-checking the integrity of the fingerprint across multiple domains you can be confident that you obtained the correct key.

- [Twitter profile](https://twitter.com/FeatherWallet)
- [Subreddit sidebar](https://old.reddit.com/r/FeatherWallet/)
- Through DNS (Linux): `drill -D key.featherwallet.net TXT`

If any of the resources listed above do not provide the expected fingerprint, please [report](report-an-issue) this to the developers immediately.