import requests


class BaseQuery:
    url: str = "https://leetcode.com/graphql/"
    query: str = ""

    def post(self):
        response = requests.post(self.url, json={"query": self.query})
        return response.json()
