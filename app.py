from flask import Flask, render_template, request
import openai
import env
import os

app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_itinerary', methods=['POST'])
def generate_itinerary():
    destination = request.form['destination']
    budget = request.form['budget']
    duration = request.form['duration']
    activities = request.form['activities']
    accommodation = request.form['accommodation']

    prompt = f"Here's an itinerary for your ideal holiday to {destination}:"
    input_text = f"Destination: {destination}\nBudget: {budget}\nDuration: {duration}\nActivities: {activities}\nAccommodation: {accommodation}\n{prompt}\n"

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=input_text,
      temperature=0.7,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    itinerary = response.choices[0].text
    return itinerary


if __name__ == '__main__':
    app.run()
