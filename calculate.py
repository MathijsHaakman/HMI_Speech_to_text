import os
import requests

with open(os.path.join("Results", "results.csv"), 'r') as list:
    list.readline()
    line = list.readline()
    print("number;wrr,wer")
    while line:
        data = line.split(";")
        reference = data[1]
        guess = data[3]

        r = requests.post(
            "http://api.robbit.me",
            json={
                "guess": guess,
                "reference": reference
            }
        ).json()

        print("{};{};{}".format(data[0], r["wrr"], r["wer"]))



        line = list.readline()