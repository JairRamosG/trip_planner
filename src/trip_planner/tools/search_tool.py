import json
import os

import requests
from langchain.tools import tool

class SearchTool():
    @tool('Search in the internet')
    def searcn_internet(query):
        """
        Useful to search in the internet about a given topic and return relevant results.
        """

        top_results = 4
        url = f"https://google.serper.dev/search"
        payload = json.dumps({"q" : query})
        headers = {
            'X-API-KEY' : os.getenv('SEPER_API_KEY'),
            'Content-Type': 'application/json'      
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        # check if there is an organic key
        if 'organic' in response.json():
            return "Sorry, I couldn't find any relevant information on the internet about that topic, there could be an error with your serper API KEY."
        else:
            results = response.json()['organic']
            string = []
            for result in results[:top_results]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}", f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}", "\n-------------------"
                    ]))
                except KeyError:
                    next
            return '\n'.join(string)
