import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
api_key =os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
from app import main
import random
from flask import Flask, render_template, request


app = Flask(__name__)


def sentiment_analysis(transcription):
    # Prompts for sentiment analysis
    prompts = [
        """As an AI specializing in understanding human emotions, please analyze the sentiment of the following text. Consider the speaker's tone, underlying emotions, and any notable shifts in sentiment throughout the conversation. Provide insights into the emotional context and indicate whether the overall sentiment is positive, negative, or neutral.",
        "Imagine you're a literary critic analyzing a novel. Your task is to dissect the emotional undertones of the given text. Delve into the subtleties of the language used, character emotions, and thematic elements. Provide an insightful commentary on the sentiment expressed, highlighting key passages that evoke strong emotions.",
        "You're a therapist analyzing a client's session transcript. Explore the emotional landscape of the conversation, paying attention to tone, empathy, and underlying feelings. Offer interpretations on the client's emotional state, identifying potential triggers and coping mechanisms. Provide guidance on how to address any negative emotions and foster a positive outlook.",
        "You're a film critic reviewing a movie script. Your task is to evaluate the emotional depth and character development portrayed in the dialogue. Analyze the sentiment conveyed by the actors' performances, the pacing of the story, and the overall narrative arc. Offer critical insights into the emotional impact of the script, highlighting memorable scenes and poignant moments."""
    ]

    # Randomly select a prompt
    prompt = random.choice(prompts)

    # Generate sentiment analysis using GPT-3
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.6,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    
    # Extract sentiment analysis from response
    response_content = response.choices[0].message.content
    return response_content, prompt

# Perform sentiment analysis on the transcription
transcription = main()
sentiment = sentiment_analysis(transcription)
print(sentiment)



# Define the route for sentiment analysis result
@app.route('/sentiment')
def sentiment():
    # Perform sentiment analysis
    transcription = main()
    sentiment, prompt = sentiment_analysis(transcription)
    return render_template('result.html', sentiment=sentiment, prompt=prompt)


if __name__ == '__main__':
    app.run(debug=True)



