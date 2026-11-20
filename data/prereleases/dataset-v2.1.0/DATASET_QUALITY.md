# Validation and Test Quality: v2.1.0

Model: `models.d/newsagency_radiostation_modernbert_v2.1.0/best`

This report was generated only after verifying that evaluation predictions cover exactly the current validation and test document IDs.

Coverage levels: **adequate** = at least 20 gold mentions; **limited** = 10-19; **insufficient** = fewer than 10.

## Overall Quality

| Split | Documents | Gold mentions | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|
| train | 2,572 | 2,691 | - | - | - |
| validation | 527 | 587 | 0.957 | 0.877 | 0.916 |
| test | 490 | 634 | 0.938 | 0.839 | 0.886 |

## Entity Coverage

Entity coverage assesses whether labels in the test split have enough gold occurrences to support both training and evaluation. Validation does not contribute to coverage. Overall coverage is the weaker of train and test coverage.

| Overall coverage | Labels |
|---|---:|
| adequate | 5 |
| limited | 33 |
| insufficient | 11 |

| Entity label | Train occurrences | Train coverage | Test occurrences | Test coverage | Overall coverage |
|---|---:|---|---:|---|---|
| `org.ent.pressagency.afp` | 308 | adequate | 37 | adequate | **adequate** |
| `org.ent.pressagency.agence-radio` | 16 | limited | 10 | limited | **limited** |
| `org.ent.pressagency.akp` | 8 | insufficient | 14 | limited | **insufficient** |
| `org.ent.pressagency.ansa` | 22 | adequate | 10 | limited | **limited** |
| `org.ent.pressagency.ap` | 98 | adequate | 17 | limited | **limited** |
| `org.ent.pressagency.apa` | 30 | adequate | 10 | limited | **limited** |
| `org.ent.pressagency.ata` | 25 | adequate | 4 | insufficient | **insufficient** |
| `org.ent.pressagency.ats-sda` | 275 | adequate | 37 | adequate | **adequate** |
| `org.ent.pressagency.belga` | 29 | adequate | 10 | limited | **limited** |
| `org.ent.pressagency.cip` | 10 | limited | 3 | insufficient | **insufficient** |
| `org.ent.pressagency.ctk` | 26 | adequate | 10 | limited | **limited** |
| `org.ent.pressagency.ddp-dapd` | 19 | limited | 10 | limited | **limited** |
| `org.ent.pressagency.dnb` | 29 | adequate | 10 | limited | **limited** |
| `org.ent.pressagency.domei` | 28 | adequate | 10 | limited | **limited** |
| `org.ent.pressagency.dpa` | 76 | adequate | 12 | limited | **limited** |
| `org.ent.pressagency.europapress` | 20 | adequate | 11 | limited | **limited** |
| `org.ent.pressagency.extel` | 31 | adequate | 9 | insufficient | **insufficient** |
| `org.ent.pressagency.havas` | 342 | adequate | 50 | adequate | **adequate** |
| `org.ent.pressagency.keystone` | 13 | limited | 11 | limited | **limited** |
| `org.ent.pressagency.kipa` | 34 | adequate | 11 | limited | **limited** |
| `org.ent.pressagency.kyodo` | 20 | adequate | 10 | limited | **limited** |
| `org.ent.pressagency.palach-press` | 10 | limited | 3 | insufficient | **insufficient** |
| `org.ent.pressagency.reuters` | 332 | adequate | 54 | adequate | **adequate** |
| `org.ent.pressagency.spk-smp` | 44 | adequate | 10 | limited | **limited** |
| `org.ent.pressagency.st-petersburg-telegraph-agency` | 8 | insufficient | 2 | insufficient | **insufficient** |
| `org.ent.pressagency.stefani` | 23 | adequate | 10 | limited | **limited** |
| `org.ent.pressagency.tanjug` | 28 | adequate | 10 | limited | **limited** |
| `org.ent.pressagency.tass` | 39 | adequate | 15 | limited | **limited** |
| `org.ent.pressagency.telegraphen-union` | 17 | limited | 9 | insufficient | **insufficient** |
| `org.ent.pressagency.up-upi` | 124 | adequate | 25 | adequate | **adequate** |
| `org.ent.pressagency.wolff` | 69 | adequate | 14 | limited | **limited** |
| `org.ent.pressagency.xinhua` | 27 | adequate | 10 | limited | **limited** |
| `org.ent.radiostation.bbc` | 52 | adequate | 14 | limited | **limited** |
| `org.ent.radiostation.china-radio-international` | 10 | limited | 3 | insufficient | **insufficient** |
| `org.ent.radiostation.deutsche-welle` | 13 | limited | 9 | insufficient | **insufficient** |
| `org.ent.radiostation.deutschlandfunk` | 16 | limited | 10 | limited | **limited** |
| `org.ent.radiostation.kol-yisrael` | 21 | adequate | 2 | insufficient | **insufficient** |
| `org.ent.radiostation.polskie-radio` | 29 | adequate | 10 | limited | **limited** |
| `org.ent.radiostation.radio-bucharest` | 52 | adequate | 10 | limited | **limited** |
| `org.ent.radiostation.radio-free-europe` | 58 | adequate | 15 | limited | **limited** |
| `org.ent.radiostation.radio-liberty` | 17 | limited | 9 | insufficient | **insufficient** |
| `org.ent.radiostation.radio-moscow` | 38 | adequate | 10 | limited | **limited** |
| `org.ent.radiostation.radio-paris` | 30 | adequate | 10 | limited | **limited** |
| `org.ent.radiostation.radio-prague` | 30 | adequate | 11 | limited | **limited** |
| `org.ent.radiostation.rfi` | 19 | limited | 10 | limited | **limited** |
| `org.ent.radiostation.rtl` | 35 | adequate | 11 | limited | **limited** |
| `org.ent.radiostation.rts` | 21 | adequate | 10 | limited | **limited** |
| `org.ent.radiostation.vatican-radio` | 29 | adequate | 10 | limited | **limited** |
| `org.ent.radiostation.voice-of-america` | 41 | adequate | 12 | limited | **limited** |

## Test Entity Prediction Outcomes

This summarizes every test gold entity plus unmatched extra predictions. The detailed TSV is intended for filtering, sorting, and manual inspection.

Detailed TSV: `reports.d/test-entity-predictions.tsv`

| Outcome | Instances |
|---|---:|
| correct | 532 |
| wrong_label | 8 |
| span_mismatch | 12 |
| wrong_label_and_span | 2 |
| complex_overlap | 1 |
| missed | 79 |
| extra | 11 |

## Test Prediction Outcomes by Gold Label

| Entity label | Gold rows | Correct | Wrong label | Span mismatch | Wrong label + span | Complex overlap | Missed |
|---|---:|---:|---:|---:|---:|---:|---:|
| `org.ent.pressagency.afp` | 37 | 37 | 0 | 0 | 0 | 0 | 0 |
| `org.ent.pressagency.agence-radio` | 10 | 9 | 0 | 0 | 0 | 0 | 1 |
| `org.ent.pressagency.akp` | 14 | 11 | 3 | 0 | 0 | 0 | 0 |
| `org.ent.pressagency.ansa` | 10 | 8 | 1 | 0 | 0 | 0 | 1 |
| `org.ent.pressagency.ap` | 17 | 15 | 0 | 0 | 0 | 0 | 2 |
| `org.ent.pressagency.apa` | 10 | 10 | 0 | 0 | 0 | 0 | 0 |
| `org.ent.pressagency.ata` | 4 | 3 | 0 | 0 | 0 | 0 | 1 |
| `org.ent.pressagency.ats-sda` | 37 | 35 | 0 | 0 | 0 | 0 | 2 |
| `org.ent.pressagency.belga` | 10 | 9 | 0 | 0 | 0 | 0 | 1 |
| `org.ent.pressagency.cip` | 3 | 3 | 0 | 0 | 0 | 0 | 0 |
| `org.ent.pressagency.ctk` | 10 | 10 | 0 | 0 | 0 | 0 | 0 |
| `org.ent.pressagency.ddp-dapd` | 10 | 9 | 0 | 0 | 0 | 0 | 1 |
| `org.ent.pressagency.dnb` | 10 | 8 | 0 | 0 | 0 | 0 | 2 |
| `org.ent.pressagency.domei` | 10 | 10 | 0 | 0 | 0 | 0 | 0 |
| `org.ent.pressagency.dpa` | 12 | 12 | 0 | 0 | 0 | 0 | 0 |
| `org.ent.pressagency.europapress` | 11 | 9 | 0 | 0 | 0 | 0 | 2 |
| `org.ent.pressagency.extel` | 9 | 6 | 0 | 0 | 0 | 0 | 3 |
| `org.ent.pressagency.havas` | 50 | 49 | 0 | 0 | 0 | 0 | 1 |
| `org.ent.pressagency.keystone` | 11 | 6 | 0 | 0 | 0 | 0 | 5 |
| `org.ent.pressagency.kipa` | 11 | 6 | 0 | 0 | 0 | 0 | 5 |
| `org.ent.pressagency.kyodo` | 10 | 9 | 0 | 0 | 0 | 0 | 1 |
| `org.ent.pressagency.palach-press` | 3 | 3 | 0 | 0 | 0 | 0 | 0 |
| `org.ent.pressagency.reuters` | 54 | 45 | 2 | 0 | 0 | 0 | 7 |
| `org.ent.pressagency.spk-smp` | 10 | 8 | 0 | 1 | 0 | 0 | 1 |
| `org.ent.pressagency.st-petersburg-telegraph-agency` | 2 | 0 | 1 | 0 | 1 | 0 | 0 |
| `org.ent.pressagency.stefani` | 10 | 10 | 0 | 0 | 0 | 0 | 0 |
| `org.ent.pressagency.tanjug` | 10 | 10 | 0 | 0 | 0 | 0 | 0 |
| `org.ent.pressagency.tass` | 15 | 13 | 1 | 0 | 0 | 0 | 1 |
| `org.ent.pressagency.telegraphen-union` | 9 | 6 | 0 | 1 | 0 | 0 | 2 |
| `org.ent.pressagency.up-upi` | 25 | 19 | 0 | 2 | 0 | 0 | 4 |
| `org.ent.pressagency.wolff` | 14 | 9 | 0 | 0 | 0 | 0 | 5 |
| `org.ent.pressagency.xinhua` | 10 | 8 | 0 | 1 | 0 | 0 | 1 |
| `org.ent.radiostation.bbc` | 14 | 7 | 0 | 1 | 0 | 0 | 6 |
| `org.ent.radiostation.china-radio-international` | 3 | 2 | 0 | 0 | 0 | 0 | 1 |
| `org.ent.radiostation.deutsche-welle` | 9 | 9 | 0 | 0 | 0 | 0 | 0 |
| `org.ent.radiostation.deutschlandfunk` | 10 | 7 | 0 | 0 | 0 | 0 | 3 |
| `org.ent.radiostation.kol-yisrael` | 2 | 0 | 0 | 1 | 0 | 0 | 1 |
| `org.ent.radiostation.polskie-radio` | 10 | 7 | 0 | 0 | 0 | 0 | 3 |
| `org.ent.radiostation.radio-bucharest` | 10 | 10 | 0 | 0 | 0 | 0 | 0 |
| `org.ent.radiostation.radio-free-europe` | 15 | 14 | 0 | 0 | 0 | 0 | 1 |
| `org.ent.radiostation.radio-liberty` | 9 | 8 | 0 | 1 | 0 | 0 | 0 |
| `org.ent.radiostation.radio-moscow` | 10 | 9 | 0 | 0 | 0 | 0 | 1 |
| `org.ent.radiostation.radio-paris` | 10 | 7 | 0 | 1 | 0 | 0 | 2 |
| `org.ent.radiostation.radio-prague` | 11 | 9 | 0 | 1 | 0 | 0 | 1 |
| `org.ent.radiostation.rfi` | 10 | 5 | 0 | 0 | 0 | 0 | 5 |
| `org.ent.radiostation.rtl` | 11 | 8 | 0 | 0 | 0 | 0 | 3 |
| `org.ent.radiostation.rts` | 10 | 8 | 0 | 0 | 0 | 1 | 1 |
| `org.ent.radiostation.vatican-radio` | 10 | 8 | 0 | 1 | 1 | 0 | 0 |
| `org.ent.radiostation.voice-of-america` | 12 | 9 | 0 | 1 | 0 | 0 | 2 |

## Quality by Entity

| Entity label | Train gold | Val gold | Val F1 | Test gold | Test precision | Test recall | Test F1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `org.ent.pressagency.afp` | 308 | 42 | 0.976 | 37 | 1.000 | 1.000 | 1.000 |
| `org.ent.pressagency.agence-radio` | 16 | 10 | 0.947 | 10 | 0.900 | 0.900 | 0.900 |
| `org.ent.pressagency.akp` | 8 | 10 | 1.000 | 14 | 0.917 | 0.786 | 0.846 |
| `org.ent.pressagency.ansa` | 22 | 9 | 0.875 | 10 | 1.000 | 0.800 | 0.889 |
| `org.ent.pressagency.ap` | 98 | 16 | 0.897 | 17 | 1.000 | 0.882 | 0.938 |
| `org.ent.pressagency.apa` | 30 | 9 | 0.778 | 10 | 1.000 | 1.000 | 1.000 |
| `org.ent.pressagency.ata` | 25 | 2 | 0.667 | 4 | 1.000 | 0.750 | 0.857 |
| `org.ent.pressagency.ats-sda` | 275 | 42 | 0.988 | 37 | 0.921 | 0.946 | 0.933 |
| `org.ent.pressagency.belga` | 29 | 11 | 0.952 | 10 | 1.000 | 0.900 | 0.947 |
| `org.ent.pressagency.cip` | 10 | 0 | 0.000 | 3 | 1.000 | 1.000 | 1.000 |
| `org.ent.pressagency.ctk` | 26 | 11 | 0.800 | 10 | 1.000 | 1.000 | 1.000 |
| `org.ent.pressagency.ddp-dapd` | 19 | 6 | 1.000 | 10 | 1.000 | 0.900 | 0.947 |
| `org.ent.pressagency.dnb` | 29 | 12 | 0.857 | 10 | 1.000 | 0.800 | 0.889 |
| `org.ent.pressagency.domei` | 28 | 10 | 1.000 | 10 | 1.000 | 1.000 | 1.000 |
| `org.ent.pressagency.dpa` | 76 | 12 | 0.960 | 12 | 1.000 | 1.000 | 1.000 |
| `org.ent.pressagency.europapress` | 20 | 10 | 1.000 | 11 | 1.000 | 0.818 | 0.900 |
| `org.ent.pressagency.extel` | 31 | 6 | 0.667 | 9 | 0.857 | 0.667 | 0.750 |
| `org.ent.pressagency.havas` | 342 | 33 | 1.000 | 50 | 0.961 | 0.980 | 0.970 |
| `org.ent.pressagency.keystone` | 13 | 13 | 0.762 | 11 | 1.000 | 0.545 | 0.706 |
| `org.ent.pressagency.kipa` | 34 | 11 | 0.857 | 11 | 1.000 | 0.545 | 0.706 |
| `org.ent.pressagency.kyodo` | 20 | 9 | 1.000 | 10 | 1.000 | 0.900 | 0.947 |
| `org.ent.pressagency.palach-press` | 10 | 1 | 1.000 | 3 | 1.000 | 1.000 | 1.000 |
| `org.ent.pressagency.reuters` | 332 | 50 | 0.909 | 54 | 1.000 | 0.833 | 0.909 |
| `org.ent.pressagency.spk-smp` | 44 | 12 | 0.917 | 10 | 0.667 | 0.800 | 0.727 |
| `org.ent.pressagency.st-petersburg-telegraph-agency` | 8 | 2 | 1.000 | 2 | 0.000 | 0.000 | 0.000 |
| `org.ent.pressagency.stefani` | 23 | 9 | 1.000 | 10 | 0.909 | 1.000 | 0.952 |
| `org.ent.pressagency.tanjug` | 28 | 10 | 1.000 | 10 | 1.000 | 1.000 | 1.000 |
| `org.ent.pressagency.tass` | 39 | 13 | 0.800 | 15 | 0.929 | 0.867 | 0.897 |
| `org.ent.pressagency.telegraphen-union` | 17 | 12 | 0.833 | 9 | 0.857 | 0.667 | 0.750 |
| `org.ent.pressagency.up-upi` | 124 | 15 | 0.968 | 25 | 0.864 | 0.760 | 0.809 |
| `org.ent.pressagency.wolff` | 69 | 12 | 0.857 | 14 | 0.900 | 0.643 | 0.750 |
| `org.ent.pressagency.xinhua` | 27 | 11 | 1.000 | 10 | 0.800 | 0.800 | 0.800 |
| `org.ent.radiostation.bbc` | 52 | 17 | 0.741 | 14 | 0.778 | 0.500 | 0.609 |
| `org.ent.radiostation.china-radio-international` | 10 | 0 | 0.000 | 3 | 1.000 | 0.667 | 0.800 |
| `org.ent.radiostation.deutsche-welle` | 13 | 10 | 0.952 | 9 | 1.000 | 1.000 | 1.000 |
| `org.ent.radiostation.deutschlandfunk` | 16 | 10 | 0.889 | 10 | 1.000 | 0.700 | 0.824 |
| `org.ent.radiostation.kol-yisrael` | 21 | 0 | 0.000 | 2 | 0.000 | 0.000 | 0.000 |
| `org.ent.radiostation.polskie-radio` | 29 | 11 | 0.737 | 10 | 1.000 | 0.700 | 0.824 |
| `org.ent.radiostation.radio-bucharest` | 52 | 6 | 0.923 | 10 | 1.000 | 1.000 | 1.000 |
| `org.ent.radiostation.radio-free-europe` | 58 | 11 | 0.900 | 15 | 1.000 | 0.933 | 0.966 |
| `org.ent.radiostation.radio-liberty` | 17 | 11 | 0.952 | 9 | 0.800 | 0.889 | 0.842 |
| `org.ent.radiostation.radio-moscow` | 38 | 10 | 1.000 | 10 | 1.000 | 0.900 | 0.947 |
| `org.ent.radiostation.radio-paris` | 30 | 10 | 0.947 | 10 | 0.875 | 0.700 | 0.778 |
| `org.ent.radiostation.radio-prague` | 30 | 8 | 0.800 | 11 | 0.900 | 0.818 | 0.857 |
| `org.ent.radiostation.rfi` | 19 | 11 | 0.842 | 10 | 0.714 | 0.500 | 0.588 |
| `org.ent.radiostation.rtl` | 35 | 12 | 0.857 | 11 | 1.000 | 0.727 | 0.842 |
| `org.ent.radiostation.rts` | 21 | 7 | 0.769 | 10 | 0.727 | 0.800 | 0.762 |
| `org.ent.radiostation.vatican-radio` | 29 | 10 | 0.947 | 10 | 0.889 | 0.800 | 0.842 |
| `org.ent.radiostation.voice-of-america` | 41 | 12 | 0.870 | 12 | 0.900 | 0.750 | 0.818 |
