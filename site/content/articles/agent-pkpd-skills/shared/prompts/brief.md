You are acting as a pharmacometrician. Your working directory is {WORKDIR}. Work only inside it.

It contains `warfarin.csv`, a public single-oral-dose warfarin dataset (the `warfarin` data from the R package nlmixr2data). Columns: id, time (h), amt (mg; dose records), dv (observation), dvid ("cp" = plasma warfarin concentration in mg/L, "pca" = prothrombin complex activity in % of normal), evid (1 = dose, 0 = observation), wt (kg), age (years), sex.

Task:
1. Audit the data and decide how to handle any problems you find.
2. Build a population PK model.
3. Build a PK/PD model relating warfarin concentration to PCA.
4. Report parameter estimates with uncertainty, model diagnostics, model comparison and limitations.
5. Answer this question with an appropriate analysis: does using a subject's own PK measurements up to 24 h after the dose improve prediction of that subject's PCA after 24 h, compared with a population prediction?

Rules:
- Do not read, list or search any files outside {WORKDIR}. Other folders on this computer contain a reference analysis of the same data, and reading them would invalidate this exercise.
- Do not use web search or web fetch.
- Do not install packages. Available: R 4.5.3 at "C:/Program Files/R/R-4.5.3/bin/Rscript.exe" with nlmixr2est 7.1.0, nlmixr2 7.0.1, rxode2 5.1.8, ggplot2, vpc, xpose.nlmixr2; Python 3.12 with numpy 1.26, scipy, pandas, matplotlib.
- Keep any single computation under about 30 minutes.
{SKILL_LINE}
Deliverables in {WORKDIR}: `report.md` with sections (Data audit; PK model; PK/PD model; Parameter estimates; Diagnostics; Early-PK prediction question; Limitations), the scripts you ran (runnable top to bottom), and figures. Every number in the report must come from your executed code. Finish with a short summary of your main findings.
