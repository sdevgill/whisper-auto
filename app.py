import os
import time
from datetime import timedelta

import whisper


input_folder = "./input/"
output_folder = "./output/"
valid_extensions = [
    ".mp3",
    ".wav",
    ".m4a",
]  # Add or modify the file extensions as needed

# Create folders if they don't exist
os.makedirs(output_folder, exist_ok=True)
os.makedirs(input_folder, exist_ok=True)


# Load the local whisper model.
# Available models: tiny, base, small, medium, large (default large-v2)
model = whisper.load_model("large", device="cuda")


def transcribe_and_append(
    audio_path, output_path, separator="\n--------------------------------\n"
):
    result = model.transcribe(audio_path)
    transcription = result["text"]

    with open(output_path, "a", encoding="utf-8") as output_file:
        output_file.write(separator)
        output_file.write(transcription)
        output_file.write(separator)


def main():
    transcription_count = 0
    total_time = 0

    print("--------------------------------")  # Add horizontal line at the start

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file has a valid audio file extension
        file_extension = os.path.splitext(filename)[1]
        if file_extension in valid_extensions:
            file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(
                output_folder, f"{os.path.splitext(filename)[0]}_transcription.txt"
            )

            # Measure the time taken to transcribe the audio file
            start_time = time.time()
            transcribe_and_append(file_path, output_file_path)
            time_taken = time.time() - start_time
            total_time += time_taken

            # Format the time taken for each file
            formatted_time = f"{int(time_taken // 3600):02d}:{int((time_taken % 3600) // 60):02d}:{int(time_taken % 60):02d}.{int((time_taken % 1) * 100):02d}"

            # Append the time taken to the output file
            with open(output_file_path, "a", encoding="utf-8") as f:
                f.write(f"\nTime: {formatted_time}\n")

            transcription_count += 1
            print(
                f"Transcription #{transcription_count} for '{filename}' has been saved. Time taken: {formatted_time}"
            )
        else:
            print(f"{filename} has an unsupported file extension. Skipping...")

    # Format the total time
    total_time_formatted = f"{int(total_time // 3600):02d}:{int((total_time % 3600) // 60):02d}:{int(total_time % 60):02d}.{int((total_time % 1) * 100):02d}"

    print(f"\nFinished processing {transcription_count} audio files.\n")
    print(f"Total time: {total_time_formatted}")

    print("--------------------------------")  # Add horizontal line at the end


if __name__ == "__main__":
    main()
