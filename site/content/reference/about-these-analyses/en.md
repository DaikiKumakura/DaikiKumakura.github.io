The articles, tools and glossary on this site are personal technical notes by Daiki Kumakura. This page states what they are, how they are made and checked, and how an error can be reported.

## Scope

- **Public information and simulation only.** Every analysis uses published papers and their supplements, public regulatory documents, public datasets, or simulation. No patient-level data that are not public are used.
- **Not clinical or regulatory advice.** The analyses compare exposure, estimate model parameters or examine what public data can support. They do not recommend a dose or a treatment for any patient or product, and the tools say so where they show numbers.
- **Not peer reviewed.** The articles are personal notes. Peer-reviewed work is listed on the [Publication](../publication.html) page, and an article of the working-paper category is labeled as not peer reviewed.
- **Personal views.** The notes do not represent any organization.

## How an analysis is made

1. **The question comes first.** Each analysis states its [question of interest and context of use](../glossary/qoi-cou.html) before the method, so the claim stays within what the data can support.
2. **Sources are cited and audited.** Papers are cited with DOIs. When a source is inconsistent (for example a table value that differs from its footnote), the article reports it and tests both versions.
3. **Code and inputs are shared.** An article with a computational core comes with a distribution file (analysis plan, code, input tables, results) so that the numbers can be reproduced. Random seeds are fixed, and the commands to rerun are given.
4. **Results are checked independently.** Typically the core calculation is recomputed with a different implementation or language, and compared with published values. The size of the agreement is reported in the article. Agreement with published values shows that a model was rebuilt correctly; it does not validate the model for another population (see [reimplementing a published population PK model](../glossary/poppk-reimplementation.html)).
5. **Limits are written down.** Each article separates what can and cannot be concluded, reports intervals and sensitivity analyses where they apply, and marks exploratory findings as exploratory.

Examples: [fixed doses of anti-PD-1 antibodies at extreme body weights](../writing/fixed-vs-weight-dosing-en.html), [reimplementing a published mosunetuzumab model](../writing/mosunetuzumab-public-pk-en.html), [borrowing an existing drug's dose comparison](../writing/borrowing-prior-dose-selection-en.html).

## Translations

Articles are available in Japanese and English. The original language is stated, and a translation is published after its numbers, figures and conclusions have been checked against the original.

## Updates and corrections

- Each article shows a version number. The date of the last update is in the page's structured data (`dateModified`) and the sitemap.
- A change that affects a number, a conclusion or a source raises the version and the update date. Typographical fixes do not.
- If you find an error, please report it through [GitHub Issues](https://github.com/DaikiKumakura/DaikiKumakura.github.io/issues) of the site repository, naming the article and the statement. The full history of every change is public in that repository.

## Citing

Each article ends with a "Cite this article" line with the author, year, title and URL. The article pages also carry citation metadata that reference managers such as Zotero and Mendeley can read.
