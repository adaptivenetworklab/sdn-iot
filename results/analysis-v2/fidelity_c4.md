# Fidelitas generator (C4)

## Marginal dan ACF

| perbandingan                  | slice   |   KS D |   W1 (Mbps) |   |dACF| rata2 lag 1-10 |   |dACF| maks lag 1-10 |
|:------------------------------|:--------|-------:|------------:|------------------------:|-----------------------:|
| batas: riil-train vs riil-val | p1      |  0.222 |       0.802 |                   0.140 |                  0.221 |
| batas: riil-train vs riil-val | p2      |  0.222 |       0.803 |                   0.138 |                  0.222 |
| batas: riil-train vs riil-val | p4      |  0.229 |       0.803 |                   0.146 |                  0.209 |
| sintetis vs riil-train        | p1      |  0.352 |       0.366 |                   0.160 |                  0.196 |
| sintetis vs riil-train        | p2      |  0.347 |       0.372 |                   0.123 |                  0.194 |
| sintetis vs riil-train        | p4      |  0.362 |       0.365 |                   0.130 |                  0.169 |

## Discriminator

| perbandingan                  | slice                |   AUC discriminator (5-fold) |   AUC sd antar fold |   jumlah jendela |
|:------------------------------|:---------------------|-----------------------------:|--------------------:|-----------------:|
| batas: riil-train vs riil-val | semua (jendela 50x3) |                        0.836 |               0.252 |          719.000 |
| sintetis vs riil-train        | semua (jendela 50x3) |                        0.534 |               0.327 |         1128.000 |

## Deskriptif

| data                     | slice   |   baris |   mean |    sd |   min |    p5 |   p50 |   p95 |   max |
|:-------------------------|:--------|--------:|-------:|------:|------:|------:|------:|------:|------:|
| riil-train (real_only)   | p1      |     613 |  3.554 | 0.962 | 0.310 | 3.116 | 3.308 | 6.818 | 7.752 |
| riil-train (real_only)   | p2      |     613 |  3.554 | 0.961 | 0.297 | 3.113 | 3.306 | 6.819 | 8.113 |
| riil-train (real_only)   | p4      |     613 |  4.274 | 0.976 | 0.339 | 3.708 | 4.042 | 7.599 | 8.573 |
| sintetis (aug_subsample) | p1      |     613 |  3.411 | 0.323 | 2.442 | 2.897 | 3.389 | 3.969 | 4.653 |
| sintetis (aug_subsample) | p2      |     613 |  3.420 | 0.334 | 2.423 | 2.907 | 3.381 | 4.001 | 4.378 |
| sintetis (aug_subsample) | p4      |     613 |  4.143 | 0.333 | 3.309 | 3.632 | 4.127 | 4.692 | 5.103 |
| riil-val                 | p1      |     204 |  4.355 | 1.700 | 3.075 | 3.131 | 3.323 | 7.253 | 7.649 |
| riil-val                 | p2      |     204 |  4.356 | 1.707 | 3.081 | 3.137 | 3.323 | 7.338 | 7.814 |
| riil-val                 | p4      |     204 |  5.076 | 1.710 | 3.665 | 3.706 | 4.056 | 8.023 | 8.574 |
