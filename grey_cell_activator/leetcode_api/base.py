import requests


class BaseQuery:
    api_url: str = "https://leetcode.com/graphql/"
    query: str = ""

    def __init__(self) -> None:
        raise NotImplementedError()

    def _make_request(self) -> dict:
        response = requests.post(self.api_url, json={"query": self.query})
        return response.json()
