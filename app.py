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

            # Append the time taken to the output file
            with open(output_file_path, "a", encoding="utf-8") as f:
                f.write(
                    f"\nTime taken for this transcription: {time_taken:.2f} seconds\n"
                )

            transcription_count += 1
            print(
                f"Transcription #{transcription_count} for '{filename}' has been saved. Time taken: {time_taken:.2f} seconds"
            )
        else:
            print(f"{filename} has an unsupported file extension. Skipping...")

    print(f"\nFinished processing {transcription_count} audio files.\n")
    print(f"Total time: {total_time:.2f} seconds")


if __name__ == "__main__":
    main()
