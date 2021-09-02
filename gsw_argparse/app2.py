#! /usr/bin/env python3
import argparse
import json
from urllib3 import PoolManager

HTTP = PoolManager()


def getLyrics(artist, title):
    # url = "https://api.lyrics.ovh/v1/{}/{}".format(artist, title)
    url = "https://shazam.p.rapidapi.com/search"

    file = open('api_key.txt', 'r')
    api_key = file.readline()

    querystring = {"term": title,
                   "locale": "en-US", "offset": "0", "limit": "5"}

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "shazam.p.rapidapi.com"
    }

    response = HTTP.request(
        "GET",
        url,
        headers=headers,
        fields=querystring)

    # response = HTTP.request('GET', url)

    if response.status == 200:
        return {"status": "success", "lyrics": response.data}
    else:
        return {"status": "failed", "cause": response.data}


parser = argparse.ArgumentParser(
    description="Retrieve song lyrics from the cloud")

group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
group.add_argument("-f", "--file", type=str,
                   help="save the lyrics to a text file")

"""

parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")

args = parser.parse_args()
answer = args.x**args.y

"""

parser.add_argument("lyrics", nargs=2, type=str,
                    help="{} & {}".format("artist", "song"))

args = parser.parse_args()

if len(args.lyrics) == 2:
    artist = args.lyrics[0].capitalize()
    title = args.lyrics[1].upper()


answer = getLyrics(artist, title)

if args.quiet:
    if answer["status"] == "success":
        print(answer["lyrics"])
    else:
        print(answer["cause"])
elif args.verbose:
    print("Searched for the lyrics to {} by {}\n\n".format(title, artist))

    if answer["status"] == "success":
        print(answer["lyrics"])
    else:
        print(answer["cause"])
else:
    print("Song {} by {}\n\n".format(title, artist))

    if answer["status"] == "success":
        print(answer["lyrics"])
    else:
        print(answer["cause"])
