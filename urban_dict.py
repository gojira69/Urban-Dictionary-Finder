import requests
import json


def requestData(word):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    querystring = {"term": word}
    headers = {
        "X-RapidAPI-Key": "6bb4804c0bmshab33739dd5d1524p1457f5jsna74cb460920a",
        "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com",
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response


def Search(word):
    response = requestData(word)
    data = response.json()
    sorted_entries = sorted(data["list"], key=lambda x: x["thumbs_up"], reverse=True)
    print("===================", word, "===================\n\n")
    for entry in sorted_entries:
        print("Author:", entry["author"])
        print("Definition:", entry["definition"])
        print("Example:", entry["example"])
        print("Upvotes:", entry["thumbs_up"])
        print("Downvotes:", entry["thumbs_down"])
        print("Written On:", entry["written_on"])
        print("\n\n======================================\n\n")


def main():
    word = input("Ask Me Something: ")
    Search(word)


if __name__ == "__main__":
    main()