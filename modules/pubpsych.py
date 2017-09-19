import pandas as pd
from pandas.io.json import json_normalize
import urllib.parse

def flatten(mylist, liste):
    for item in mylist:
        if isinstance(item, list):
            flatten(item, liste)
        else:
            liste.append(item)
    return(liste)

def do_search(query_text, fieldname, output_format):
    numberOfRows = 200
    mydfs = []
    startResult = 1

    # get size of result set
    df = pd.read_json('http://pubpsych.zpid.de/zpid/select?q=DB=PSYNDEX%20' + urllib.parse.quote_plus(
        query_text) + '&fl=' + fieldname +'&rows=200&wt=json')
    numberOfPages = divmod(df['response']['numFound'], numberOfRows)

    # catch big search results
    realNumberOfPages = numberOfPages[0] + 1
    if realNumberOfPages > 10:
        realNumberOfPages = 10

    for n in range(0, realNumberOfPages):
        queryUrl = 'http://pubpsych.zpid.de/zpid/select?q=DB=PSYNDEX%20' + urllib.parse.quote_plus(
            query_text) + '&page=' + str(n) + '&fl=' + fieldname +'&rows=200&start=' + str(startResult) + '&wt=json'
        startResult = startResult + 200
        mydfs.append(pd.read_json(queryUrl))

    mydf2 = []

    for m in range(0, len(mydfs)):
        mydf2.extend(mydfs[m]['response']['docs'])

    df2 = json_normalize(mydf2)
    l = df2.values.tolist()

    liste = []
    flat_list = flatten(l, liste)
    df3 = pd.DataFrame({fieldname.lower(): flat_list})
    df4 = df3[[fieldname.lower()]].groupby([fieldname.lower()]).size().reset_index(name='count').sort_values(['count'], ascending=0)
    if output_format == 'json':
        out = df4.to_json(orient='index')
    else:
        out = df4[:50].to_html(escape=False, index=False)

    if not out:
        return 0
    else:
        return out