#ivri korem 2020
"""
a twilio and flask python app that responses when being calld
"""
#importing
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

#making the voice assistant response when being called
app = Flask(__name__)

@app.route("/voice", methods=["GET", "POST"])
def voice():

    VoiceResponse.say("hi, bye")


#running the app
app.run(debug=True)