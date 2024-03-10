import sys
import heapq
import numpy as np
import re
import itertools
import requests
from googleapiclient.discovery import build
import spacy
from bs4 import BeautifulSoup


exclude_filetype = ['jpg', 'jpeg', 'png', 'gif', 'tiff', 'psd', 'pdf', 'eps', 'ai', 'indd', 'raw']
extraction_method = api_key = engine_id = gemini_api_key = None
r = t = q = k = None
# r : relation to extract
# t : extraction confidence threshold
# q : seed query
# k : number of tuples requested in output

X = dict()  # dictionary of extracted tuples, {(tuple): score}
visited_urls = []
used_query = []
relations = {
    '1': 'Schools_Attended',
    '2': 'Work_For',
    '3': 'Live_In',
    '4': 'Top_Member_Employees'
}

def run_query(key, cx, q):
    """
    Call Google API and receive list of results.
    Image files or non-HTML files are filtered out

    :param key: Google API key
    :param cx: Google Engine id
    :param q: query in string
    :return: list of filtered results
    """
    service = build("customsearch", "v1", developerKey=key)
    res = (service.cse().list(q=q, cx=cx).execute())

    filtered_res = []
    for r in res['items']:
        if (r['link'].split('.')[-1] in exclude_filetype) or ('fileFormat' in r):
            continue
        filtered_res += [r]
    return filtered_res

def process_query_results(results):
    for i, res in enumerate(results):
        if res['link'] not in visited_urls:
            print('URL ( ' + str(i) + ' / ' + str(len(results)) + '): ' + res['link'])
            extract_relation(res['link'])
            visited_urls += [res['link']]

def get_website_text(url):
    print('Fetching text from url ...')
    try:
        html = requests.get(url, timeout=10).text
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()
        if len(text) > 10000:
            print('Trimming webpage content from ' + str(len(text)) + ' to 10000 characters')
            text = text[:10000]
        print('Webpage length (num characters): ' + str(len(text)))
        return re.sub(r'[\t\r\n]', '', text)
    except Exception as ex:
        return ''

def extract_relation():
    pass

if __name__ == "__main__":
    extraction_method, api_key, engine_id, gemini_api_key = sys.argv[1:5]
    r, t, q, k = sys.argv[5:]

    # if extraction_method == '-spanbert':
    #     print('Loading pre-trained spanBERT from ./pretrained_spanbert')
    #     print()
    #     spanbert = SpanBERT("./pretrained_spanbert")
    # elif extraction_method == '-gemini':
    #     pass # TODO: load library

    # print('____')
    # print('Parameters:')
    # print('Client Key	= ' + api_key)
    # print('Engine Key	= ' + engine_id)
    # print('Gemini Key	= ' + gemini_api_key)
    # print('Method		= ' + extraction_method)
    # print('Relation		= 	' + relations[r])
    # print('Threshold	= ' + str(t))
    # print('Query		= ' + q)
    # print('# of Tuples	= ' + str(k))

    # print('Loading necessary libraries; This should take a minute or so ...')
    nlp = spacy.load("en_core_web_lg")

    text = get_website_text('https://matix.io/extract-text-from-webpage-using-beautifulsoup-and-python/')
    doc = nlp(text)
    for sen in doc.sents:  
        print(sen)

    # iteration_count = 0
    # while True:
    #     print('=========== Iteration: ' + str(iteration_count)' - Query: ' + q + ' ==========='
        
    #     results = run_query(api_key, engine_id, query))
    #     process_query_results(results)

    #     if len(X) >= k:
    #         break
        
    #     # Choose next query
    #     if extraction_method == '-spanbert':
    #         # TODO: Fill in query selection method

    #     elif extraction_method == '-gemini'
    #         # TODO: Fill in query selection method:

    #     i = i + 1
    # print('Total # of iterations = ' + str(iteration_count + 1))