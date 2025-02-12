

# Video Clipper by Timestamps

This Python script allows you to clip segments from MP4 video files based on timestamps you provide. You can specify multiple timestamp ranges, and the script will output each clip as a separate MP4 file in a designated output folder.

## Features

*   **Timestamp-based clipping:** Easily extract specific portions of videos using start and end timestamps.
*   **Multiple clips per video:**  Provide multiple timestamp ranges to create several clips from a single video in one run.
*   **User-friendly input:**  Prompts for video file path, timestamps, and output folder name.
*   **Clear output filenames:**  Clips are named with the original filename, clip number, and timestamp range for easy identification.
*   **Error handling:**  Includes checks for invalid timestamp formats, incorrect timestamp ranges, and video loading errors.
*   **Output folder creation:** Automatically creates the output folder if it doesn't exist.

## Requirements

*   **Python 3.x**
*   **MoviePy library:** For video editing and manipulation.
*   **imageio library:**  MoviePy dependency for handling video files.

You can install the necessary libraries using pip:

```bash
pip install moviepy
pip install imageio
```

## Virtual Environment (Recommended)

It's highly recommended to use a virtual environment to isolate the project dependencies and avoid conflicts with other Python projects on your system. Here's how to create and use a virtual environment:

1.  **Create a virtual environment:** Navigate to the directory where you saved `clip_video.py` in your terminal and run:

    ```bash
    python -m venv venv
    ```
    This command will create a new virtual environment named `venv` in your project directory.

2.  **Activate the virtual environment:**

    *   **On Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
    *   **On Windows:**
        ```bash
        venv\Scripts\activate
        ```
    You should see `(venv)` at the beginning of your terminal prompt, indicating that the virtual environment is activated.

3.  **Install dependencies within the virtual environment:**  With the virtual environment activated, install the required libraries using pip:

    ```bash
    pip install moviepy
    pip install imageio
    ```
    These libraries will now be installed only within your virtual environment.

4.  **Run the script:** You can now run the `clip_video.py` script as described in the "How to Use" section.

5.  **Deactivate the virtual environment (when finished):** When you are done working with the script, you can deactivate the virtual environment by running:

    ```bash
    deactivate
    ```
    This will return you to your base Python environment.

## Installation

1.  **Download the script:** Save the Python code (provided in the `clip_video.py` file) as `clip_video.py` in your desired project directory.
2.  **Navigate to the script's directory:** Open your terminal or command prompt and change the directory to where you saved `clip_video.py`.
3.  **(Optional but Recommended) Create and activate a virtual environment:** Follow the steps in the "Virtual Environment (Recommended)" section above.
4.  **Install dependencies:** If you haven't already, and especially if you are using a virtual environment, install the required Python libraries using pip:

    ```bash
    pip install moviepy
    pip install imageio
    ```

## How to Use

1.  **Run the script:** Execute the script from your terminal using:

    ```bash
    python clip_video.py
    ```
    **(If using a virtual environment, ensure it is activated before running the script.)**

2.  **Follow the prompts:** The script will guide you through the process by asking for the following inputs:

    *   **Enter the path to your MP4 video file:**  Provide the full path to the MP4 video you want to clip. For example: `/path/to/your/video.mp4` or `C:\Videos\my_video.mp4`.
    *   **Enter timestamps:** Input the timestamp ranges in the format `minutes:seconds-minutes:seconds`, separated by commas.  For example: `00:10-00:25, 01:30-01:45, 02:00-02:10`.
        *   Ensure timestamps are in `minutes:seconds` format (e.g., `01:30` for 1 minute and 30 seconds).
        *   Use a hyphen `-` to separate the start and end timestamps of a clip.
        *   Separate multiple timestamp ranges with commas `,`.
    *   **Enter the name of the output folder:**  Choose a name for the folder where the clipped videos will be saved. If the folder doesn't exist, it will be created.

3.  **Output:** Once the script finishes processing, you will find a new folder with the name you specified in the same directory where you ran the script. Inside this folder, you will find the clipped video segments as individual MP4 files. The filenames will be in the format: `[original_filename]_clip_[clip_number]_[start_timestamp]-[end_timestamp].mp4`.

## Example Usage

Let's say you have a video file named `my_video.mp4` and you want to create two clips:

*   Clip 1: From 0 minutes 10 seconds to 0 minutes 25 seconds.
*   Clip 2: From 1 minute 30 seconds to 1 minute 45 seconds.

You would run the script and provide the following inputs:

```
Enter the path to your MP4 video file: /path/to/my_video.mp4
Enter timestamps in 'minutes:seconds-minutes:seconds' format, separated by commas (e.g., 00:10-00:20,01:30-01:45): 00:10-00:25, 01:30-01:45
Enter the name of the output folder: clipped_videos
```

After running the script, a folder named `clipped_videos` will be created (if it doesn't exist) in the same directory, and it will contain two files:

*   `my_video_clip_1_00m10-00m25.mp4`
*   `my_video_clip_2_01m30-01m45.mp4`

## Important Notes

*   **Virtual Environment:** Using a virtual environment is strongly recommended to keep your project dependencies isolated and organized.
*   **Timestamp Format:**  Ensure you use the correct `minutes:seconds` format for timestamps. Incorrect formatting will lead to errors.
*   **Start and End Times:** The start timestamp must be before the end timestamp for each clip.
*   **Video Duration:** If an end timestamp exceeds the video's duration, the clip will be cut at the end of the video, and a warning message will be displayed.
*   **Error Messages:** The script provides error messages to help you identify and fix any issues with input file paths, timestamp formats, or video processing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

[Your Name/Username] (Optional)
[Your Email Address] (Optional)

