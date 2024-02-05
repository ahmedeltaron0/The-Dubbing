import requests

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "e5814446d2d8efe8e7dadae095c6603c"
}

data = {
  "text": '''انا اسمي احمداشتغل علي مشروع الدبلجه''',
  "model_id": "eleven_monolingual_v1",  # Use a model that best fits the default voice
  "voice_settings": {
    "language": "arabic",  # Set the language
    "stability": 0.5,  # Adjust stability
    "similarity_boost": 0.1,  # Adjust similarity boost
    "pitch": 0.0,  # Set pitch to default (normal)
    "speed":0.0,  # Set speed to default (normal)
    "volume": 1.0,  # Set volume to default (normal)
    "breathiness": 0.0,  # Set breathiness to default (normal)
    "articulation": 0.0,  # Set articulation to default (normal)
    "emotional_tone": 0.0,  # Set emotional tone to default (neutral)
    "glottal_tension": 0.0  # Set glottal tension to default (normal)
  }
}

response = requests.post(url, json=data, headers=headers)
with open('Tested audio T-T-S/output_arabic.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
