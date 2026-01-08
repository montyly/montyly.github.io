---
layout: default
title: Portfolio
permalink: /portfolio/
---

<style>
.nav-tabs {
  display: flex;
  margin-bottom: 1.5rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-family: inherit;
  font-size: 0.95em;
  overflow: hidden;
  width: fit-content;
}

.nav-tabs a {
  padding: 8px 16px;
  text-decoration: none;
  color: #0366d6;
  background: #f8f8f8;
  border-right: 1px solid #ccc;
  flex: 1;
  text-align: center;
}

.nav-tabs a:last-child {
  border-right: none;
}

.nav-tabs a.active {
  background: white;
  font-weight: bold;
}
</style>

<div class="nav-tabs">
  <a href="/">Home</a>
  <a href="/blog">Blog</a>
  <a href="/portfolio/" class="active">Portfolio</a>
  <a href="/about/">About</a>
</div>


---

*Former Trail of Bits Engineering Director – Author of Slither*


---

## 🧾 Audit Portfolio

The folllowing contains example of public security reviews I have participated in. 

### Defi


| Year | Protocol | Description | Report Link |
|------|----------|-------------|-------------|
| 2024 | Uniswap V4 | AMM | [Link](https://github.com/trailofbits/publications/blob/master/reviews/2024-07-uniswap-v4-core-securityreview.pdf) |
| 2024 | Balancer V3 | AMM | [Link](https://github.com/trailofbits/publications/blob/master/reviews/2024-12-balancer-v3-securityreview.pdf) |
| 2023 | BlueFin (Move/SUI) | Perpetual swap | [Link](https://bluefin.io/blog/doc/bluefin_sui_final_report.pdf) |
| 2023 | Mass.money | Tetris VM | [Link](https://github.com/trailofbits/publications/blob/master/reviews/2023-06-nestedfinance-tetrishyvm-securityreview.pdf) |
| 2023 | Mass.money | Account abstraction, vesting, on-chain DCA | [Link](https://github.com/trailofbits/publications/blob/master/reviews/2023-02-nestedfinance-smartcontracts-securityreview.pdf) |
| 2022 | Folksfinance (Algorand) | Lending protocol | [Link](https://github.com/trailofbits/publications/blob/master/reviews/2022-11-folksfinance-securityreview.pdf) |
| 2021 | Balancer V2 | AMM | [Link](https://github.com/trailofbits/publications/blob/master/reviews/2021-04-balancer-balancerv2-securityreview.pdf) |
| 2020 | Balancer core | AMM | [Link](https://github.com/trailofbits/publications/blob/master/reviews/BalancerCore.pdf) |
| 2020 | Curve dao | Governance for Stablecoin AMM | [Link](https://github.com/trailofbits/publications/blob/master/reviews/CurveDAO.pdf) |
| 2020 | Curve | Stablecoin AMM | [Link](https://github.com/trailofbits/publications/blob/master/reviews/curve-summary.pdf) |
| 2020 | StakerDAO (Algorand) | Vault | [Link](https://github.com/trailofbits/publications/blob/master/reviews/wALGO.pdf) |
| 2020 | Dexter (Tezos) | AMM on Tezos | [Link](https://github.com/trailofbits/publications/blob/master/reviews/dexter.pdf) |
| 2019 | Computable | Data marketplace protocol | [Link](https://github.com/trailofbits/publications/blob/master/reviews/computable.pdf) |
| 2019 | Flexa | Staking | [Link](https://github.com/trailofbits/publications/blob/master/reviews/Flexa.pdf) |
| 2018 | Basis | Stablecoin | [Link](https://github.com/trailofbits/publications/blob/master/reviews/basis.pdf) |
| 2018 | Gemini | Stablecoin | [Link](https://github.com/trailofbits/publications/blob/master/reviews/gemini-dollar.pdf) |
| 2018 | Origin | Marketplace protocol | [Link](https://github.com/trailofbits/publications/blob/master/reviews/origin.pdf) |
| 2018 | Parity | Multisig wallet | [Link](https://github.com/trailofbits/publications/blob/master/reviews/parity.pdf) |
| 2017 | Sai | Stablecoin | [Link](https://github.com/trailofbits/publications/blob/master/reviews/sai.pdf) |
| 2017 | Dapphub | Smart contract library | [Link](https://github.com/trailofbits/publications/blob/master/reviews/dapphub.pdf) |

### Blockchain Protocols

| Year | Name                     | Description                          | Report Link |
|------|--------------------------|--------------------------------------|-------------|
| 2024 | Offchain BoLD Fixes      | L2 rollup       | [Link](https://github.com/trailofbits/publications/blob/master/reviews/2024-12-offchain-boldfixes-securityreview.pdf) |
| 2022 | Offchain Nitro           | L2 rollup            | [Link](https://docs.arbitrum.io/assets/files/2022_03_14_trail_of_bits_security_audit_nitro_1_of_2-d777111730bd602222978f7d98713d40.pdf) |
| 2020 | Hermez                   | L2 rollup                            | [Link](https://github.com/trailofbits/publications/blob/master/reviews/hermez.pdf) |
| 2019 | Centrifuge               | Asset tokenization chain             | [Link](https://resources.cryptocompare.com/asset-management/687/1694187019179.pdf) |
| 2017 | RSKj                     | Bitcoin sidechain client             | [Link](https://github.com/trailofbits/publications/blob/master/reviews/RSKj.pdf) |

Non-public reviews include:
- Algorand (L1)
- Celo (L1)
- Chainlink (Oracle network)
- Matic / Polygon (L1/2)
- Status (Secure messaging + wallet)
- TBTC (Bitcoin bridge)

## 🐞 Vulnerabilities Disclosure

| Year | Project | Description | Link |
|------|---------|-------------|------|
| 2020 | Tezos |  Callback authorization bypass & Callback injection | [Post](https://forum.tezosagora.org/t/smart-contract-vulnerabilities-due-to-tezos-message-passing-architecture/2045) |
| 2020 | Aave | Selfdestruct through uninitialized proxy | [Blog](https://blog.trailofbits.com/2020/12/16/breaking-aave-upgradeability/) |
| 2020 | Vyper | Function collision | [Github](https://github.com/vyperlang/vyper/pull/1530), [Blog](https://blog.trailofbits.com/2019/10/24/watch-your-language-our-first-vyper-audit/) |
| 2020 | E&Y'gs Nightfall | Unused return value allows minting free tokens | N/A |
| 2020 | DOSNetwork | ABI encodePacked Collision | N/A |
| 2020 | EthKids | Msg.value reused | N/A |
| 2019 | Kleros | Array’s length overwrite allows arbitrary write | N/A |
| 2017 | Gitcoin | Lack of check on ERC20 return value | [Github](https://github.com/gitcoinco/smart_contracts/commit/d84c59e04c32a20a907950d6032a21cf423c1e10) |

### Non-Blockchain Disclosures

| Year | Project | CVE | Description | Link |
|------|---------|-----|-------------|------|
| 2016 | Giflib | CVE-2016-3177 | Use after free and double free | [Link](https://sourceforge.net/p/giflib/bugs/83) |
| 2015 | Jasper-JPEG-200 | CVE-2015-5221 | Use after Free | [Link](https://www.openwall.com/lists/oss-security/2015/08/20/4) |
| 2016 | Alsabat | N/A | Use after free | [Link](https://bugzilla.redhat.com/show_bug.cgi?id=1378419) |
| 2015 | Openjpeg | CVE-2015-8871 | Use after free | [Link](https://github.com/uclouvain/openjpeg/issues/563) |
| 2015 | Gnome-nettool | N/A | Use after free | [Link](https://bugzilla.gnome.org/show_bug.cgi?id=753184) |
| 2015 | Accel-ppp | N/A | Use after free | [Link](http://accel-ppp.org/forum/viewtopic.php?f=18&t=581) |