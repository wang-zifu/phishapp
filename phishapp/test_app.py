import base64
import json
import requests
import argparse
import sys

# http://127.0.0.1:5000/predict
# http://192.168.99.100:5000/predict
# https://phishapp.dhondtdoit.ch/predict

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="url of the endpoint", action="store")
    parser.add_argument("-p", "--path",  help="path of the image to be classified", action="store")
    args = parser.parse_args()

    if not args.url or not args.path:
        print("ERROR: Please provide both a url and a path.")
        sys.exit(1)

    with open(args.path, "rb") as img_file:
        img_string = base64.encodebytes(img_file.read()).decode()
    r = requests.post(args.url, json={"image": img_string})

    parsed = json.loads(r.text)
    print(json.dumps(parsed, indent=4))
