from watson_developer_cloud import SpeechToTextV1
import json
from os.path import join, dirname
import time

service = SpeechToTextV1(
    iam_apikey='',
    url='https://stream-fra.watsonplatform.net/speech-to-text/api'
)

#with open(join("Resources", "Audio", "1.mp3"),
#          'rb') as audio_file:
#    print(json.dumps(
#        service.recognize(
#            audio=audio_file,
#            content_type='audio/mp3').get_result(),
#        indent=2))


with open(join("Resources", "Transcribed_List.csv"), 'r') as list:
    list.readline()
    line = list.readline()
    print("{},{},{},{},{}".format("Number", "Text", "Confidence", "Transcript", "Milis"))
    while line:
        number, text = line.split(",", 1)
        text = text.strip()
        with open(join("Resources", "Audio", "{}.mp3".format(number)), 'rb') as audio_file:

            before = int(round(time.time() * 1000))
            result = service.recognize(
                audio=audio_file,
                content_type='audio/mp3'
            ).get_result()
            after = int(round(time.time() * 1000))
            result = result["results"][0]["alternatives"][0]
            print("{};{};{};{};{}".format(number, text, result["confidence"], result["transcript"].strip() + ".", after-before))

        line = list.readline()
