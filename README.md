# Player Re-Identification and Tracking – YOLOv8 + ReID (OSNet)

## Project Overview

This project tracks soccer players in broadcast video footage using a combination of object detection and Re-Identification (ReID). The main goal is to assign consistent, persistent IDs to players across frames, even when they leave and re-enter the camera view.

The project consists of two main phases:

1. **Detection Phase** (detect.py):

   - Uses YOLOv8 to detect players, referees, goalkeepers, and the ball.
   - Outputs annotated video with bounding boxes but without identity tracking.

2. **ReID Tracking Phase** (player.py):

   - Uses TorchReID (OSNet) to extract appearance features for each player.
   - Assigns persistent global IDs to players based on feature similarity.
   - Saves a new annotated video and a CSV log of tracking data.

---

## Project Structure

```
soccer/
├── best.pt                      # Trained YOLOv8 model
├── 15sec_input_720p.mp4         # Input video
│
├── output/
│   ├── detected_frames/         # Auto-filled by detect.py
│   ├── tracked_frames/          # Auto-filled by player.py
│   ├── detected_video_custom.mp4      # YOLO-only output
│   ├── tracked_video_reid_final.mp4   # ReID output
│   └── player_tracking_log.csv       # CSV tracking log
│
├── detect.py                    # Detection-only script
├── player.py                    # ReID tracking script
├── report.md                    # Project write-up
└── requirements.txt             # Dependency list
```

---

## Dependencies

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
opencv-python
ultralytics
torch
torchvision
torchreid
scikit-learn
numpy
Pillow
```

---

## Execution Steps

### 1. Clone or set up the project

Ensure you have all the files in the correct folder structure described above.

### 2. Run Detection (Optional Preview)

This detects players, referees, and the ball using YOLOv8 and saves bounding box annotations.

```bash
python detect.py
```

**Output:**

- Annotated frames: `output/detected_frames/`
- Video: `output/detected_video_custom.mp4`

### 3. Run Player Re-Identification Tracking

This uses YOLO detections and TorchReID to assign consistent player IDs.

```bash
python player.py
```

**Output:**

- ReID-based annotated video: `output/tracked_video_reid_final.mp4`
- Frame-by-frame tracking log: `output/player_tracking_log.csv`
- Optional: heatmaps and stat analysis (can be added separately)

---

## When to Run Each Script

| Script      | When to Run                                  |
| ----------- | -------------------------------------------- |
| `detect.py` | To preview YOLO detection output             |
| `player.py` | For full tracking with consistent global IDs |

---

## Notes

- The ReID system handles identity persistence but may still struggle with very long absences or similar appearances.
- To analyze player behavior, you can later use the tracking CSV to generate distance stats, heatmaps, or player timelines.

---

This project forms a foundational structure for intelligent sports analytics using single-camera soccer footage.

