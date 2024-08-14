#!/usr/bin/python3
"""
queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list, after=None, occurence_count=[]):
    """prints a sorted count of given keywords"""

    if not after:
        occurence_count = [0] * len(word_list)

    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # reddit API requires a User-Agent header
    headers = {"User-Agent": "Mozilla/5.0"}
    # parameters to the request
    params = {"after": after}

    response = requests.get(
        endpoint, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()

        # Check occurrence of keywords in titles
        for post in data.get("data").get("children"):
            for title_word in post.get("data").get("title").split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == title_word.lower():
                        occurence_count[i] += 1

        after = data.get("data").get("after")
        if after is None:  # no more next posts!
            dup_list = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        dup_list.append(j)
                        occurence_count[i] += occurence_count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if occurence_count[j] > occurence_count[i] or (
                        word_list[i] > word_list[j]
                        and occurence_count[j] == occurence_count[i]
                    ):
                        # Swap counts and keywords to sort
                        # by count and keyword
                        temp = occurence_count[i]
                        occurence_count[i] = occurence_count[j]
                        occurence_count[j] = temp
                        temp = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = temp

            for i in range(len(word_list)):
                if (occurence_count[i] > 0) and i not in dup_list:
                    print(f"{word_list[i].lower()}: {occurence_count[i]}")
        else:
            # call recursive function again to continue fetching next posts
            count_words(subreddit, word_list, after, occurence_count)
