import json
import requests
import csv

ACCESS_TOKEN = None


def get_response(api, parameter):
    header = {"Authorization": ACCESS_TOKEN}
    url = "https://cloud.feedly.com/{}?".format(api, )

    if parameter != None:
        url = "{0}?{1}".format(url, parameter)

    try:
        response = requests.get(url, headers=header, verify=False, timeout=5)
        return json.loads(response.text)
    except Exception as e:
        print str(e)


def write_row(writer, result):
    tags = ""
    for tag in result["deliciousTags"]:
        try:
            tags += "|{}".format(tag)
        except UnicodeEncodeError as e:
            continue
    tags += "|"

    if "website" in result:
        writer.writerow([result["website"], result["subscribers"], tags])


search_term = ["food", "singapore", "asia", "chickenchop", "house", "finance", "investment", "ebook", "humor",
               "funny" "apple", "tech", "mac", "windows", "microsoft", "lifehack", "minimalistic", "cats", "dogs",
               "whiskey", "beer", "alcohol"]
feeds = []
for term in search_term:
    feeds.append(get_response("/v3/search/feeds", "query={0}&count=20".format(term))['results'])

# write to csv files
output = "feedly.csv"

with open(output, "wb") as csvfile:
    writer = csv.writer(csvfile, delimiter=",", quotechar="\"")
    writer.writerow(["website", "subscribers", "tags"])
    for feed in feeds:
        for r in feed:
            write_row(writer, r)
