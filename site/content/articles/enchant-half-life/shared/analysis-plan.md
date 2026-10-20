# Plan: what does "Spearman 0.74 for human half-life" measure?

Fixed 2026-10-20, before fitting any model.

## Question
Iambic's Enchant white paper (2024-10-29) claims a Spearman of 0.74 for human PK half-life on the Obach dataset (previous best 0.58, linked to the
TDC "Half_Life_Obach" benchmark; top TDC leaderboard score 0.576 on 2026-05-28) and "meaningful predictive power" when trained on under 1% of
the data (5 drugs). Split, test size, seeds and baselines are not disclosed. Using the same public data, what can be said about (a) how precisely
a Spearman of this size is determined, (b) how much the split design changes a plain baseline, (c) what simple methods reach with 5 training
drugs, and (d) whether the half-life ranking is driven by volume of distribution or by clearance?

## Data (public, TDC via Harvard Dataverse; downloaded 2026-10-20 with permission)
- half_life_obach.tab: 667 drugs, half-life (h). vdss_lombardo.tab: 1,130 drugs, Vss (L/kg).
- Parent compound key = first block of the InChIKey (stereoisomers and salts merged). Largest fragment kept for descriptors.
- Analysis set for (b)-(d): duplicates of a parent key merged by the median of log10 half-life.

## Analyses (seed 20261020)
1. Precision: Bonett-Wright 95% intervals for Spearman 0.74 and 0.58 at n = 133 (a 20% test set of 667) and n = 667. Simulation (Gaussian copula,
   10,000 replicates) of the paired difference between a 0.74 model and a 0.58 model on the same test set for assumed inter-model rank
   correlations 0.5, 0.7 and 0.9: width of the 95% interval and the fraction of replicates in which the better model is ahead.
2. Split design: two plain baselines (kNN on Morgan fingerprints, k = 5, Tanimoto-weighted; random forest on RDKit descriptors, 300 trees) under
   random 80/20 and scaffold 80/20 splits (TDC-style scaffold grouping, my implementation, not TDC's code), 5 seeds each. Test Spearman, and the
   distribution of each test compound's nearest-training-neighbour Tanimoto similarity.
3. Training size: the same two baselines trained on 5, 10, 20, 50, 100, 200 and all training drugs, 30 random draws each, tested on the same
   scaffold test sets. Also zero-training rules: Spearman of log half-life with single descriptors and with a crude ionisation class
   (SMARTS-based acid/base/zwitterion/neutral, no pKa).
4. Decomposition: for drugs in both files, log10(t1/2) = log10(Vss) - log10(CL) + constant when CL is back-calculated as ln2 x Vss / t1/2 (assumes
   Vz ~ Vss; no human CL data are in these files). Variance shares of log Vss and log CL, and how well the random forest predicts each component.

## Not done / limits
No Enchant predictions are available, so nothing here measures Enchant. Baselines are plain scikit-learn models, not state-of-the-art. No wet-lab
or clinical data. The Obach set is itself a literature compilation with heterogeneous studies.

## Addendum after review (2026-10-20)
- The first scaffold split did not follow TDC's big-group rule (largest group could enter the test set); replaced, and the re-split study raised from 5 to 30 seeds.
  First version archived in v0-flawed-split/.
- Added after review: evaluation on TDC's fixed test set (admet_group.zip, train_val.csv and test.csv for Half_Life_Obach, downloaded with permission);
  Zou intervals; a prior-sign non-negative regression as a 5-drug baseline; rule values on the fixed test set; variance/covariance of the identity.
- Dropped: the Gaussian-copula simulation (a power calculation) and the combined V+CL half-life prediction (circular).
- Eight single-descriptor rules were tried; all are reported.
