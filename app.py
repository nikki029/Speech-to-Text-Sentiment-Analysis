# main.py (python example)

import os
from dotenv import load_dotenv
import json

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
)

load_dotenv()



# URL to the audio file
AUDIO_URL = {
    "url": "https://dpgr.am/spacewalk.wav"
}

API_KEY = os.getenv("DEEPGRAM_API_KEY")





def main():
    try:
        # STEP 1 Create a Deepgram client using the API key
        deepgram = DeepgramClient(API_KEY)

        #STEP 2: Configure Deepgram options for audio analysis
        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )

        # STEP 3: Call the transcribe_url method with the audio payload and options
        response = deepgram.listen.prerecorded.v("1").transcribe_url(AUDIO_URL, options)

        # STEP 4: Save the response to a JSON file
        with open("output.json", "w") as f:
            json.dump(response.to_dict(), f, indent=4)

        # print("JSON response saved to output.json")

        # Extract transcript from JSON response
        with open("output.json", "r") as f:
            data = json.load(f)
            transcript = data["results"]["channels"][0]["alternatives"][0]["transcript"]

        # Print the transcript
        return transcript

    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
     main()



