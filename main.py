import os
import re
from moviepy.editor import VideoFileClip

def parse_timestamp(timestamp):
    """Parses a timestamp string (mm:ss) into seconds."""
    try:
        minutes, seconds = map(int, timestamp.split(':'))
        return minutes * 60 + seconds
    except ValueError:
        return None

def format_timestamp_for_filename(timestamp):
    """Formats a timestamp in seconds to mm:ss for filenames."""
    minutes = timestamp // 60
    seconds = timestamp % 60
    return f"{minutes:02d}m{seconds:02d}"

def clip_video(video_path, timestamps, output_folder):
    """Clips segments from a video based on provided timestamps."""
    try:
        video = VideoFileClip(video_path)
    except Exception as e:
        print(f"Error loading video: {e}")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    base_filename = os.path.splitext(os.path.basename(video_path))[0]

    for i, timestamp_range in enumerate(timestamps):
        try:
            start_time_str, end_time_str = timestamp_range.split('-')
            start_time = parse_timestamp(start_time_str.strip())
            end_time = parse_timestamp(end_time_str.strip())

            if start_time is None or end_time is None:
                print(f"Invalid timestamp format: {timestamp_range}")
                continue

            if start_time >= end_time:
                print(f"Start time must be before end time: {timestamp_range}")
                continue
            
            # Apply 30-second padding
            start_time = max(0, start_time - 30)  # Ensure start_time doesn't go below 0
            end_time = min(video.duration, end_time + 30) #Ensure end_time does not go above video duration.
            


            if end_time > video.duration:
                print(f"Warning: End time {end_time_str} exceeds video duration. Clipping to end of video.")
                end_time = video.duration

            clip = video.subclip(start_time, end_time)

            output_filename = (
                f"{base_filename}_clip_{i + 1}_"
                f"{format_timestamp_for_filename(start_time+30)}-{format_timestamp_for_filename(end_time-30)}.mp4"
            )
            output_path = os.path.join(output_folder, output_filename)
            clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
            print(f"Clip {i + 1} saved to: {output_path}")

        except ValueError:
            print(f"Invalid timestamp range format: {timestamp_range}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    video.close()

def main():
    """Main function to handle user input and video clipping."""
    video_path = input("Enter the path to your MP4 video file: ")
    while not os.path.exists(video_path) or not video_path.lower().endswith(".mp4"):
        print("Invalid file path or not an MP4 file. Please enter a valid path.")
        video_path = input("Enter the path to your MP4 video file: ")
    
    timestamp_input = input(
        "Enter timestamps in 'minutes:seconds-minutes:seconds' format, separated by commas (e.g., 00:10-00:20,01:30-01:45): "
    )
    timestamps = timestamp_input.split(',')

    output_folder = input("Enter the name of the output folder: ")

    clip_video(video_path, timestamps, output_folder)

if __name__ == "__main__":
    main()