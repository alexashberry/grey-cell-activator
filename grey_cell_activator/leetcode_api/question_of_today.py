from .base import BaseQuery


class QuestionOfToday(BaseQuery):
    base_url = "https://leetcode.com"
    query = """
        query questionOfToday {
        activeDailyCodingChallengeQuestion {
            date
            userStatus
            link
            question {
            acRate
            difficulty
            freqBar
            frontendQuestionId: questionFrontendId
            isFavor
            paidOnly: isPaidOnly
            status
            title
            titleSlug
            hasVideoSolution
            hasSolution
            topicTags {
                name
                id
                slug
            }
            }
        }
        }
    """

    def __init__(self) -> None:
        self.title, self.difficulty, self.url = self._get()

    def _get(self) -> tuple[str, str, str]:
        data = self._make_request()

        question = data["data"]["activeDailyCodingChallengeQuestion"]
        url = self.base_url + question["link"]
        title = question["question"]["title"]
        difficulty = question["question"]["difficulty"]

        return title, difficulty, url

    def __str__(self) -> str:
        return (
            f"Question Of Today\n"
            f"{self.title}\n"
            f"Difficulty: {self.difficulty}\n"
            f"{self.url}"
        )
