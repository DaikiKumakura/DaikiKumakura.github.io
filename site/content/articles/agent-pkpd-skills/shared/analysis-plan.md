# Plan: can an AI agent with a public skill library redo a warfarin PK/PD analysis?

Fixed 2026-10-18, before launching any agent run.

## Question
Given the public warfarin PK/PCA dataset and a fixed analysis brief, how close does an AI agent get to a
pharmacometrician's analysis (the published warfarin-pkpd note, 2026-10-04), with and without the
K-Dense Scientific Agent Skills `pkpd-modeling` skill (commit a1043ef, MIT)?

## Design
- Agent: Claude subagent (general-purpose, same model family as the author's assistant), fresh context.
- Arms: S = skill folder provided and agent told to read SKILL.md first; N = no skill. Two runs per arm (S1, S2, N1, N2).
- Each run in its own empty scratch directory containing only `warfarin.csv` (nlmixr2data 2.0.10 export, 515 rows)
  and, for S, `skills/pkpd-modeling/`. Agents are told not to read other files, not to use the web
  (the reference analysis is published), and not to install packages.
- Same brief for all runs (prompt saved in `prompts/`). Tools: R 4.5.3 with nlmixr2est 7.1.0 / rxode2 5.1.8; Python 3.12.
- n = 2 per arm: descriptive only; no claim that one arm is better.

## Scoring rubric (prespecified; reference = warfarin-pkpd results)
A. Data audit: (a1) 2 subjects without baseline PCA (IDs 1, 7); (a2) 4 zero concentrations; (a3) duplicate PK time keys (ID 9);
   (a4) apparent CL/F, V/F because F is unknown.
B. PK: (b1) one-compartment first-order absorption or a justified alternative; (b2) NLME estimation;
   (b3) typical CL/F within +/-20% of 0.134 L/h and V/F within +/-20% of 7.84 L; (b4) uncertainty reported.
C. PD: (c1) recognises the concentration-response delay; (c2) turnover/indirect-response or effect-compartment model;
   (c3) compared with a direct model; (c4) reports IC50/EC50 and the delay parameter (reference IC50 1.15 mg/L, kout 0.0515 1/h).
D. Early-PK question: (d1) subject-level held-out evaluation; (d2) only PK at or before 24 h used, PCA scored after 24 h;
   (d3) conclusion (reference: no consistent improvement; paired MSE difference +0.0015, -0.0012 to 0.0043).
E. Reporting: (e1) diagnostics (GOF/VPC/shrinkage); (e2) limitations incl. not INR, bleeding or dosing;
   (e3) errors found on inspection of code and report; (e4) scripts re-run by me without error.
Also recorded: wall time, tokens, tool calls, which skill parts were used.

The reference is one analyst's analysis, not ground truth; differences are described, not scored as wrong,
unless they are errors (wrong units, leakage, numbers not matching the agent's own output).

## Addendum after review (2026-10-19)
- Reference values in the figure changed to the allometric reference model (agents all used allometry).
- e4 (re-running agent scripts) was not done; instead report numbers were matched to output files and key code checked.
- Added after review: S2 lag misspecification check (check_lincmt_tlag.R); CV refit-movement check; subgroup of 13 subjects with early PK.
- Scoring was not blinded. The project-level CLAUDE.md (general analysis rules) was likely loaded in all four runs.
