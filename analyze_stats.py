import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("output/player_tracking_log.csv")

frame_rate = 30
time_stats = df.groupby('id')['frame'].nunique().reset_index()
time_stats['time_on_screen_sec'] = time_stats['frame'] / frame_rate
print("Time on Screen (seconds):")
print(time_stats)

def compute_distance(group):
    coords = group[['cx', 'cy']].values
    dists = np.sqrt(np.sum(np.diff(coords, axis=0)**2, axis=1))
    return dists.sum()

distances = df.groupby('id').apply(compute_distance).reset_index(name='pixels_traveled')
print("\nDistance Traveled (pixels):")
print(distances)

summary = pd.merge(time_stats, distances, on='id')
summary.to_csv("output/analyze/player_summary_stats.csv", index=False)
print("\nSaved: output/analyze/player_summary_stats.csv")

for player_id in df['id'].unique():
    plt.figure(figsize=(8, 6))
    player_data = df[df['id'] == player_id]
    sns.kdeplot(x=player_data['cx'], y=player_data['cy'], fill=True, cmap="Reds", bw_adjust=0.5)
    plt.title(f"Heatmap - Player ID {player_id}")
    plt.gca().invert_yaxis()  
    plt.savefig(f"output/analyze/heatmap_player_{player_id}.png")
    plt.close()

print("\nHeatmaps saved for each player in /output/analyze")
