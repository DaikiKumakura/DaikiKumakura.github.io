To make an antibody more resistant to heat, select a candidate with a higher melting temperature. That sounds straightforward. But if the temperature measures the wrong process, it can also point molecular engineering in the wrong direction.

Anthropic's October 27, 2026 account describes researchers and Claude questioning antibody measurement metrics in a collaboration with BigHat. Its explanation separates unfolding from aggregation ([1](#ref-1)). That distinction is more interesting here than a headline improvement factor.

This article separates equilibrium stability from irreversible loss during heating. In an explicitly synthetic calculation, the temperature at which half the initial molecules remain as native monomers changes with concentration and heating rate even though the equilibrium unfolding midpoint does not. Those two temperatures need separate names.

## Scope and sources

Sources were checked on October 30, 2026. I examined Anthropic's official account, the original nanobody study by Kunz et al., and NIST's abstract and bibliographic account of work by Lang and Cole. I could not retrieve the body of BigHat's linked technical report. This article neither reanalyzes its raw data nor independently tests Claude's antibody designs.

Kunz et al. measured fluorescence alongside turbidity and found concentration-dependent apparent unfolding. [Figure 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC5962586/#Fig1) and [Figure 4](https://pmc.ncbi.nlm.nih.gov/articles/PMC5962586/#Fig4) of their paper support separating a structural transition from aggregation-related measurements ([2](#ref-2)). Lang and Cole studied the importance of heating rate when comparing techniques. I checked NIST's abstract and record, rather than verifying every experimental condition in the full paper ([3](#ref-3)).

## Two processes behind one temperature

Let \(N\) denote native soluble molecules, \(U\) unfolded soluble molecules, and \(A\) material irreversibly lost from the soluble monomer pool. The distinction begins with

\[
N\rightleftharpoons U,\qquad U\longrightarrow A.
\]

Ignoring the second arrow imports an interpretation in which cooling restores the original state into a measurement where it may not.

For a reversible two-state equilibrium, the native-to-unfolded ratio can be related to a free-energy difference. If molecules are lost to aggregation during heating, however, time at temperature and concentration also matter. Persistence to a higher temperature does not uniquely identify a change in equilibrium free energy.

Fluorescence ratios, scattering, turbidity and the remaining soluble monomer fraction are different observables. Scattering also depends on particle properties such as size, so it cannot simply be converted into the fraction of molecules aggregated. Orthogonal measurements help distinguish explanations that one signal cannot separate.

## Methods

To isolate the distinction, I assumed rapid equilibrium between native and unfolded states within the remaining soluble pool. Its unfolded fraction is

\[
f_U(T)=\frac{1}{1+\exp[-(T-T_m)/s]},
\]

where \(T_m\) is the equilibrium midpoint in the absence of aggregation and \(s=2\ ^\circ\mathrm{C}\) controls the transition width. This illustrative logistic curve is not a thermodynamic fit to an antibody.

Normalize the initial amount of material to one and let \(a\) be the fraction irreversibly lost. Under heating at rate \(r=dT/dt\), I solved

\[
\frac{da}{dT}=\frac{k_{65}e^{(T-65)/5}}{r}
\frac{c}{c_0}\{f_U(T)(1-a)\}^2.
\]

Here \(k_{65}\), in \(\mathrm{min}^{-1}\), is an effective coefficient at the reference concentration; \(c/c_0\) is the initial concentration multiplier. Temperatures in the exponent are numerical values in °C; \((T-65)/5\) abbreviates \((T-65\ ^\circ\mathrm{C})/(5\ ^\circ\mathrm{C})\). The normalized phenomenological loss term represents a two-molecule process. Its order was assumed, not inferred from experimental data.

Starting with \(a=0\) at 25 °C, I heated the system to 85 °C. Synthetic candidate A has \(T_m=65\ ^\circ\mathrm{C}\) and \(k_{65}=0.003\ \mathrm{min}^{-1}\); B has 69 °C and 0.08 \(\mathrm{min}^{-1}\). B is therefore more resistant to equilibrium unfolding but loses unfolded molecules more rapidly.

The comparison endpoint is \(T_{50,N}\), where the native monomer fraction

\[
n(T)=(1-a(T))(1-f_U(T))
\]

reaches 0.5. **This is not a reconstruction of a differential scanning fluorimetry (DSF) fluorescence ratio or an instrument-reported melting temperature.** It is an explicitly defined quantity that does not require an assumed mapping to the experimental signal.

## Results

Table 1. Temperature at which half the initial material remains as native monomers in the synthetic calculation.

| Concentration multiplier | Heating rate (°C/min) | A: \(T_{50,N}\) (°C) | B: \(T_{50,N}\) (°C) |
| ---: | ---: | ---: | ---: |
| 1 | 0.5 | 64.99 | 68.67 |
| 1 | 2.0 | 65.00 | 68.90 |
| 5 | 0.5 | 64.96 | 68.04 |
| 5 | 2.0 | 64.99 | 68.61 |

Equilibrium midpoints remain 65 °C for A and 69 °C for B in every condition. Concentration is relative to a reference, not a measured value in mg/mL. Display precision describes numerical outputs, not experimental precision.

![Synthetic native monomer and irreversible loss curves for candidates A and B at two concentrations.](shared/claude-antibody-thermal-metrics/figures/thermal-aggregation.png)

Figure 1. Synthetic heating at 0.5 °C/min. Solid lines use the reference concentration; dashed lines use five times that concentration. These are not copied or redrawn BigHat experimental curves.

Although B's equilibrium midpoint is fixed at 69 °C, its \(T_{50,N}\) ranges from 68.04 to 68.90 °C. Slower heating leaves more time for loss, while higher concentration accelerates the assumed two-molecule process. The same changes have much smaller effects on A.

A and B do not reverse rank in these conditions. This is not evidence that changing a protocol must reverse rankings. It shows a condition-dependent displacement of the observed half-loss temperature for a molecule whose equilibrium midpoint remains unchanged.

I checked that native, unfolded and irreversibly lost fractions sum to one and that the loss fraction remains between zero and one. Relaxing the integrator's relative tolerance from \(10^{-10}\) to \(10^{-8}\) left the table unchanged at two decimal places. These are numerical checks, not biological validation.

## Different metrics imply different design questions

If a molecule unfolds too readily at equilibrium, stabilizing its native state is one possible design objective. If unfolded molecules aggregate rapidly, changing their interactions or loss kinetics is another. A general description such as poor heat resistance does not uniquely determine which molecular property needs changing.

A higher thermal transition temperature also does not establish a longer monomer shelf life. The synthetic heating range is not an extrapolation to refrigerated storage. Such an extrapolation would need evidence about whether the same mechanism operates at the storage temperature and whether activity can be lost without removing soluble monomers.

For an AI system selecting from many candidates, the measurement definition becomes part of the search objective. If unfolding and aggregation are mixed in that objective, the reason for a high score is mixed too. Generating more candidates cannot resolve that ambiguity. Distinguishing explanations through independent measurements is part of molecular design itself.

## Limitations and conclusion

The model assumes rapid unfolding equilibrium, a single irreversible pathway and constant heating rate. It omits reversible association, particle-size distributions, precipitation, fluorescence quenching and multidomain structure. A shift with concentration or heating rate alone would not identify the aggregation mechanism of a real molecule.

This calculation does not validate BigHat's design performance, candidate ranking or revised instrument metrics. It does establish why the target quantity matters: **an equilibrium unfolding midpoint and the temperature at which native monomers survive a particular heating protocol answer different questions. A single melting-temperature number cannot explain a design improvement until those questions are separated.**

## Data and code availability

All original calculations use synthetic inputs. The [code and results archive](shared/claude-antibody-thermal-metrics/claude-antibody-thermal-metrics.zip) contains fixed parameters, integration code, tables, the figure and environment information. Run `python analysis.py` to reproduce them. It contains neither the source study's raw data nor third-party figures.

## References

1. <span id="ref-1"></span>Anthropic. [Early progress on accelerating drug development with Claude](https://www.anthropic.com/research/early-progress-drug-development) [Internet]. Anthropic; 2026 Oct 27 [cited 2026 Oct 30]. Section: BigHat Biosciences.
2. <span id="ref-2"></span>Kunz P, Zinner K, Mücke N, Bartoschik T, Muyldermans S, Hoheisel JD. The structural basis of nanobody unfolding reversibility and thermoresistance. Scientific Reports. 2018;8:7934. [doi:10.1038/s41598-018-26338-z](https://doi.org/10.1038/s41598-018-26338-z).
3. <span id="ref-3"></span>Lang BE, Cole KD. [Measurement of the Thermal Unfolding of Proteins by Differential Scanning Calorimetry and Fluorescent Reporter Dyes](https://www.nist.gov/publications/measurement-thermal-unfolding-proteins-differential-scanning-calorimetry-and) [Internet]. National Institute of Standards and Technology; 2015 Jan 15 [cited 2026 Oct 30]. Publication abstract and bibliographic record.
