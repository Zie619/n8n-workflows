import json
import os
import sys
import subprocess

def clip_video_ffmpeg(video_path, clips, output_dir):
    """Clips a video using ffmpeg for memory efficiency."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, clip_info in enumerate(clips):
        if not isinstance(clip_info, dict) or "start" not in clip_info or "end" not in clip_info:
            print(f"Skipping invalid clip data: {clip_info}")
            continue

        start_time = clip_info["start"]
        end_time = clip_info["end"]
        output_path = os.path.join(output_dir, f"clip_{i+1}.mp4")

        print(f"Creating clip: {output_path} from {start_time}s to {end_time}s")

        command = [
            "ffmpeg",
            "-i", video_path,
            "-ss", str(start_time),
            "-to", str(end_time),
            "-c:v", "libx264",
            "-c:a", "aac",
            "-y",  # Overwrite output file if it exists
            output_path
        ]

        try:
            subprocess.run(command, check=True, capture_output=True, text=True)
            print(f"Successfully created {output_path}")
        except FileNotFoundError:
            print("Error: ffmpeg command not found. Please ensure ffmpeg is installed and in your system's PATH.")
            sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"Error creating clip {output_path}:")
            print(f"Stderr: {e.stderr}")
            continue

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python clip_video.py <video_path> <clips_json_string> <output_dir>")
        sys.exit(1)

    video_path = sys.argv[1]
    clips_json_str = sys.argv[2]
    output_dir = sys.argv[3]

    try:
        clips = json.loads(clips_json_str)
        if isinstance(clips, str):
            clips = json.loads(clips)

        if not isinstance(clips, list):
            print(f"Error: Parsed JSON is not a list. Got: {type(clips)}")
            sys.exit(1)

        clip_video_ffmpeg(video_path, clips, output_dir)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Received string for parsing: {clips_json_str}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
