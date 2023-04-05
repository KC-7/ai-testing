from flask import Flask, render_template, request
import openai
import os

if os.path.isfile('env.py'):
    import env

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_itinerary', methods=['POST'])
def generate_itinerary():

    destination = request.form['destination']
    climate = request.form['climate']
    activities = request.form['activities']
    group = request.form['group']
    accommodation = request.form['accommodation']
    relaxing = request.form['relaxing']
    cuisine = request.form['cuisine']
    attractions = request.form['attractions']
    transportation = request.form['transportation']
    cultural = request.form['cultural']
    duration = request.form['duration']
    hobbies = request.form['hobbies']
    itinerary = request.form['itinerary']
    other = request.form['other']

    prompt = f"Create a detailed dream holiday itinerary using the following information:"
    input_text = f"{prompt}\nDestination: {destination}\nClimate: {climate}\nActivities: {activities}\nGroup: {group}\nAccommodation: {accommodation}\nRelaxing/Adventurous: {relaxing}\nCuisine: {cuisine}\nAttractions: {attractions}\nTransportation: {transportation}\nCultural Experiences/Historical Sites: {cultural}\nDuration: {duration}\nHobbies/Interests: {hobbies}\nItinerary preference: {itinerary}\nOther: {other}\n"

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=input_text,
      temperature=0.7,
      max_tokens=750,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    itinerary = response.choices[0].text
    return f"Your Custom Itinerary, courtesy of eTravel.Guru: {itinerary}"


if __name__ == '__main__':
    app.run()
