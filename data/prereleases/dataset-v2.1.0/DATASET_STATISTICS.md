# Dataset Statistics: v2.1.0

This report is generated from the released train, validation, and test JSONL files.

## Overview

| Split | Documents | With mentions | Tokens | Mentions | Newspapers | Date range |
|---|---:|---:|---:|---:|---:|---|
| train | 2,572 | 1,696 | 915,897 | 2,691 | 139 | 1840-01-04 to 2000-12-19 |
| validation | 527 | 401 | 126,313 | 587 | 55 | 1841-09-28 to 2000-12-23 |
| test | 490 | 385 | 111,962 | 634 | 49 | 1840-06-16 to 2000-10-26 |
| **Total** | **3,589** | **2,482** | **1,154,172** | **3,912** | - | - |

## Split Integrity

No document IDs occur in more than one split.

## Documents by Language

| Value | Train | Validation | Test | Total |
|---|---:|---:|---:|---:|
| `de` | 812 | 169 | 156 | 1,137 |
| `en` | 129 | 33 | 24 | 186 |
| `fr` | 1,268 | 278 | 269 | 1,815 |
| `it` | 9 | 1 | 2 | 12 |
| `lb` | 31 | 4 | 9 | 44 |
| `unknown` | 323 | 42 | 30 | 395 |

## Mentions by Entity Family

| Value | Train | Validation | Test | Total |
|---|---:|---:|---:|---:|
| `press agency` | 2,180 | 431 | 468 | 3,079 |
| `radio station` | 511 | 156 | 166 | 833 |

## Mentions by Entity Label

| Value | Train | Validation | Test | Total |
|---|---:|---:|---:|---:|
| `org.ent.pressagency.afp` | 308 | 42 | 37 | 387 |
| `org.ent.pressagency.agence-radio` | 16 | 10 | 10 | 36 |
| `org.ent.pressagency.akp` | 8 | 10 | 14 | 32 |
| `org.ent.pressagency.ansa` | 22 | 9 | 10 | 41 |
| `org.ent.pressagency.ap` | 98 | 16 | 17 | 131 |
| `org.ent.pressagency.apa` | 30 | 9 | 10 | 49 |
| `org.ent.pressagency.ata` | 25 | 2 | 4 | 31 |
| `org.ent.pressagency.ats-sda` | 275 | 42 | 37 | 354 |
| `org.ent.pressagency.belga` | 29 | 11 | 10 | 50 |
| `org.ent.pressagency.cip` | 10 | 0 | 3 | 13 |
| `org.ent.pressagency.ctk` | 26 | 11 | 10 | 47 |
| `org.ent.pressagency.ddp-dapd` | 19 | 6 | 10 | 35 |
| `org.ent.pressagency.dnb` | 29 | 12 | 10 | 51 |
| `org.ent.pressagency.domei` | 28 | 10 | 10 | 48 |
| `org.ent.pressagency.dpa` | 76 | 12 | 12 | 100 |
| `org.ent.pressagency.europapress` | 20 | 10 | 11 | 41 |
| `org.ent.pressagency.extel` | 31 | 6 | 9 | 46 |
| `org.ent.pressagency.havas` | 342 | 33 | 50 | 425 |
| `org.ent.pressagency.keystone` | 13 | 13 | 11 | 37 |
| `org.ent.pressagency.kipa` | 34 | 11 | 11 | 56 |
| `org.ent.pressagency.kyodo` | 20 | 9 | 10 | 39 |
| `org.ent.pressagency.palach-press` | 10 | 1 | 3 | 14 |
| `org.ent.pressagency.reuters` | 332 | 50 | 54 | 436 |
| `org.ent.pressagency.spk-smp` | 44 | 12 | 10 | 66 |
| `org.ent.pressagency.st-petersburg-telegraph-agency` | 8 | 2 | 2 | 12 |
| `org.ent.pressagency.stefani` | 23 | 9 | 10 | 42 |
| `org.ent.pressagency.tanjug` | 28 | 10 | 10 | 48 |
| `org.ent.pressagency.tass` | 39 | 13 | 15 | 67 |
| `org.ent.pressagency.telegraphen-union` | 17 | 12 | 9 | 38 |
| `org.ent.pressagency.up-upi` | 124 | 15 | 25 | 164 |
| `org.ent.pressagency.wolff` | 69 | 12 | 14 | 95 |
| `org.ent.pressagency.xinhua` | 27 | 11 | 10 | 48 |
| `org.ent.radiostation.bbc` | 52 | 17 | 14 | 83 |
| `org.ent.radiostation.china-radio-international` | 10 | 0 | 3 | 13 |
| `org.ent.radiostation.deutsche-welle` | 13 | 10 | 9 | 32 |
| `org.ent.radiostation.deutschlandfunk` | 16 | 10 | 10 | 36 |
| `org.ent.radiostation.kol-yisrael` | 21 | 0 | 2 | 23 |
| `org.ent.radiostation.polskie-radio` | 29 | 11 | 10 | 50 |
| `org.ent.radiostation.radio-bucharest` | 52 | 6 | 10 | 68 |
| `org.ent.radiostation.radio-free-europe` | 58 | 11 | 15 | 84 |
| `org.ent.radiostation.radio-liberty` | 17 | 11 | 9 | 37 |
| `org.ent.radiostation.radio-moscow` | 38 | 10 | 10 | 58 |
| `org.ent.radiostation.radio-paris` | 30 | 10 | 10 | 50 |
| `org.ent.radiostation.radio-prague` | 30 | 8 | 11 | 49 |
| `org.ent.radiostation.rfi` | 19 | 11 | 10 | 40 |
| `org.ent.radiostation.rtl` | 35 | 12 | 11 | 58 |
| `org.ent.radiostation.rts` | 21 | 7 | 10 | 38 |
| `org.ent.radiostation.vatican-radio` | 29 | 10 | 10 | 49 |
| `org.ent.radiostation.voice-of-america` | 41 | 12 | 12 | 65 |
