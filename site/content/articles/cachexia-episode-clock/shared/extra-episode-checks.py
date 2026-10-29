"""Additional aggregate-only episode checks.

Usage: python extra-episode-checks.py path/to/released_episode_table.csv
Requires pandas. Reads the public table cited in the article; prints no IDs
or individual records. Does not reimplement episode detection or survival analysis.
"""
import json
import sys
import pandas as pd

d = pd.read_csv(sys.argv[1], usecols=[
    'episode', 'nadir_day', 'end_day', 'weight_loss_max',
    'weight_loss_start_to_end'])
e = d.loc[d.episode == 1].copy()
gap = e.weight_loss_max - e.weight_loss_start_to_end
delay = e.end_day - e.nadir_day
result = {
    'n_episodes': len(e),
    'n_gap_positive_tolerance_1e_minus_8': int((gap > 1e-8).sum()),
    'n_gap_at_least_5_percentage_points': int((gap >= 5).sum()),
    'percent_gap_at_least_5_percentage_points': float((gap >= 5).mean()*100),
    'gap_quantiles_percentage_points': gap.quantile([0, .5, .9, 1]).to_dict(),
    'nadir_to_end_quantiles_days': delay.quantile([0, .5, .75, .9, 1]).to_dict(),
}
print(json.dumps(result, indent=2))
