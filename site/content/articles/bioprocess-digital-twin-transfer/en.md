Cells that grow well in a small bioreactor need not behave the same way in a larger vessel. Even with the same cell line, oxygen delivery and mixing times change. An AI model that predicts culture data needs to account for the equipment too.

On October 21, 2026, Ark founder Yossi Quint described a manufacturing digital twin that embeds learned biology within physical equations. The blog also reports a case with yield 43% above a historical best. This is a company-reported result ([1](#ref-1)). Without a verified comparison and underlying data, that number is not an independently established control-system effect.

This article does not attempt to reproduce the 43%. Instead, a calculation using only oxygen balance asks **how models that agree in one vessel can diverge after an equipment condition changes**. It is not a reconstruction of a plant, but it makes one limitation of physics-based extrapolation concrete.

## Scope and sources

Sources were checked on October 30, 2026. I read Ark's technical blog and the public abstract of the 1992 hybrid-model paper by Psichogios and Ungar, which combines known balances with a neural network in a fed-batch model ([2](#ref-2)). I did not reanalyze that paper's experimental data.

I also consulted the public abstract of Rackauckas et al.'s universal differential equations framework, in which unknown components of scientific models can be learned ([3](#ref-3)). Ark's model weights, training data and customer manufacturing data were unavailable. The calculation below does not train a neural network. It examines what cannot be identified from one operating condition before deciding which component to learn.

## Where the learned component sits matters

For dissolved oxygen concentration \(C\), a minimal balance is

\[
\frac{dC}{dt}=k_La(C^*-C)-q(C).
\]

Here \(C^*\) is the saturation concentration in equilibrium with the gas phase, \(k_La\) is the volumetric mass-transfer coefficient, and \(q(C)\) is oxygen consumption per unit culture volume. The first term supplies oxygen to the liquid; the second removes it.

If biomass is represented separately, consumption can be written as \(q(C)=q_O(C)X\). Here biomass \(X\) is fixed and absorbed into the consumption term. Growth, death, substrate consumption and product accumulation are omitted.

Replacing an unknown \(q\) with a neural network \(q_\theta\) makes the equipment parameter \(k_La\) an explicit place to change the model when moving between vessels. That makes the intervention easier to interpret than with a predictor that directly returns oxygen concentration. It does not guarantee that the data distinguish among different possible \(q_\theta\) functions satisfying the same balance.

If training contains only conditions where oxygen remains near one level, it may identify consumption around that level. It does not establish whether consumption remains constant or falls when oxygen becomes scarce. Increasing model capacity does not automatically provide those missing observations.

## Methods

The single calibration condition is \(C^*=0.20\ \mathrm{mmol/L}\), \(k_La=50\ \mathrm{h}^{-1}\), and steady concentration \(C=0.18\ \mathrm{mmol/L}\). At steady state, \(dC/dt=0\), giving

\[
q(0.18)=50(0.20-0.18)=1.00\ \mathrm{mmol/(L\cdot h)}.
\]

All values are assumed for illustration, not taken from Ark.

Construct two consumption functions passing through that point:

\[
q(C)=q_{\max}\frac{C}{K+C},\qquad
q_{\max}=1.00\frac{K+0.18}{0.18}.
\]

Model A uses \(K=0.02\ \mathrm{mmol/L}\); model B uses 0.22 mmol/L. Their \(q_{\max}\) values are 1.111 and 2.222 mmol/(L·h), respectively. Both exactly reproduce the calibration concentration and uptake. These coefficients were constructed, not estimated from data.

Represent an equipment change by lowering \(k_La\) from 50 to \(8\ \mathrm{h}^{-1}\), hold everything else fixed, and solve the positive root of

\[
k_La(C^*-C)=q(C).
\]

The direction is illustrative. It does not imply that every larger vessel has this coefficient. Vessel size alone does not determine mass transfer; agitation, gas supply and fluid properties also matter.

## Results

Table 1. Synthetic steady oxygen uptake at calibration and after the change.

| Model | \(k_La\) (h⁻¹) | Dissolved oxygen (mmol/L) | Uptake (mmol/(L·h)) | Fraction of calibration uptake |
| --- | ---: | ---: | ---: | ---: |
| A | 50 | 0.1800 | 1.0000 | 1.000 |
| B | 50 | 0.1800 | 1.0000 | 1.000 |
| A | 8 | 0.0871 | 0.9035 | 0.904 |
| B | 8 | 0.1083 | 0.7333 | 0.733 |

![Two oxygen-consumption functions passing through one calibration point and their steady uptake across mass-transfer coefficients.](shared/bioprocess-digital-twin-transfer/figures/oxygen-transfer.png)

Figure 1. Sharing a balance and calibration point does not identify the consumption curve at lower oxygen concentrations. The dotted constant-rate extrapolation fixes uptake at its calibration value; it is not an actual AI model's output.

The two models are indistinguishable at calibration but predict about 90% and 73% of calibration uptake after the change. Model B retains a higher dissolved oxygen concentration because its consumption falls more sharply as oxygen declines, not because its equipment supplies more oxygen. Interpreting higher dissolved oxygen as better cell performance would reverse the explanation.

This difference is not caused by the presence or absence of a neural network. **Sharing the physical balance does not identify predictions in a new condition if the biological response curve remains unidentified.**

Across 101 \(k_La\) values from 0.1 to 100 h⁻¹, I checked that roots lie between zero and \(C^*\) and that transfer equals consumption. Calibration reproduction was also verified. These checks concern the specified model, not its fit to manufacturing data.

## What must transfer with a learned model

If flexible biological consumption and equipment transfer are estimated together from the same concentration record, it can be difficult to tell which component absorbs which error. Learning weak supply as strong cellular consumption carries that error into a new vessel.

Independent information about equipment coefficients and coverage of the receiving process's concentration range serve different purposes. The former helps separate balance terms; the latter reduces extrapolation of the consumption curve. Counting culture runs alone does not reveal which information was added.

The well-mixed model also erases local hypoxia and exposure history. Two vessels with the same average concentration may expose cells to different cycles between oxygen-rich and oxygen-poor regions. Predicting the average does not establish transportability of a cellular state that responds to those histories.

For digital-twin control, the response to an operation matters in addition to prediction error. Predicting one operating condition and supporting decisions about gas supply or feeding are different validation targets. Comparisons with historical yield records also need to account for cell line, product, culture duration, quality, measurements and human interventions.

## Limitations and conclusion

The calculation assumes fixed biomass, perfect mixing, constant saturation concentration and steady state. It predicts neither product concentration nor quality and does not convert uptake differences into yield differences. Temperature, carbon dioxide, pH, shear, metabolic switching and controller delay are omitted. No data establish which consumption curve is closer to real cells.

The calculation nevertheless clarifies a requirement for transfer. Embedding a learned model in physical equations creates a place to separate equipment from biology. Whether data support that separation remains an empirical question. **Moving from prediction in one vessel to use in another requires identifying the biological response when operating conditions change.**

## Data and code availability

The [code and results archive](shared/bioprocess-digital-twin-transfer/bioprocess-digital-twin-transfer.zip) contains assumed constants, root calculations, output CSV, the figure and environment information. Run `python analysis.py` to reproduce it. Inputs are entirely synthetic. The archive contains no company data, proprietary models or source-paper figures.

## References

1. <span id="ref-1"></span>Quint Y. [The Day After AI Drug Discovery](https://www.ark-biotech.com/insights/the-day-after-ai-drug-discovery) [Internet]. Ark Biotech; 2026 Oct 21 [cited 2026 Oct 30].
2. <span id="ref-2"></span>Psichogios DC, Ungar LH. A hybrid neural network-first principles approach to process modeling. AIChE Journal. 1992;38(10):1499–1511. [doi:10.1002/aic.690381003](https://doi.org/10.1002/aic.690381003). Public abstract consulted.
3. <span id="ref-3"></span>Rackauckas C, Ma Y, Martensen J, Warner C, Zubov K, Supekar R, et al. Universal Differential Equations for Scientific Machine Learning [Preprint]. arXiv; 2020. Version 4, revised 2021 Nov 2. [doi:10.48550/arXiv.2001.04385](https://doi.org/10.48550/arXiv.2001.04385). Public abstract consulted.
