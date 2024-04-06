from .base import BaseQuery


class QuestionOfToday(BaseQuery):
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
