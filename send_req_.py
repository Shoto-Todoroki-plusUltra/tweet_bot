import json
import requests
import threading
import time

def tweet(tweet_text="abcd"):
    url = "https://api.twitter.com/XXX/CreateTweet"
    headers = {
        "Host": "api.twitter.com",
        "Cookie": 'guest_id_marketing=xxx; guest_id_ads=xxx; _ga=xxx; kdt=xxx; auth_multi="xxx:xxx"; auth_token=xxx; personalization_id="xxx"; guest_id=xxx; twid=xxx; ct0=xxx; _gid=xxx', 
        "Content-Length": "1110",
        "Sec-Ch-Ua" : '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        "X-Twitter-Client-Language": "en",
        "X-Csrf-Token": 'xxx',
        "Sec-Ch-Ua-Mobile": '?0',
        "Authorization": 'xxx',
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        "Content-Type": 'application/json',
        "X-Twitter-Auth-Type": "OAuth2Session",
        "X-Twitter-Active-User": "yes",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Accept": "*/*",
        "Origin": 'https://twitter.com',
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://twitter.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

    data = {"variables":{"tweet_text":tweet_text,"dark_request":False, "media":{"media_entities":[],"possibly_sensitive":False},"withDownvotePerspective":False,"withReactionsMetadata":False,"withReactionsPerspective":False,"withSuperFollowsTweetFields":True,"withSuperFollowsUserFields":True,"semantic_annotation_ids":[]},"features":{"view_counts_public_visibility_enabled":True,"view_counts_everywhere_api_enabled":True,"longform_notetweets_consumption_enabled":False,"tweetypie_unmention_optimization_enabled":True,"responsive_web_uc_gql_enabled":True,"vibe_api_enabled":True,"responsive_web_edit_tweet_api_enabled":True,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":True,"interactive_text_enabled":True,"responsive_web_text_conversations_enabled":False,"responsive_web_twitter_blue_verified_badge_is_enabled":True,"verified_phone_label_enabled":True,"standardized_nudges_misinfo":True,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":False,"responsive_web_graphql_timeline_navigation_enabled":True,"responsive_web_enhance_cards_enabled":False},"queryId":"xxx"}
    response = requests.post(url, headers=headers, json=data)
