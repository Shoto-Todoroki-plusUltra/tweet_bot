import json
import requests
import threading
import time

def tweet(tweet_text="abcd"):
    url = "https://api.twitter.com/graphql/yL4KIHnJPXt-JUpRDrBDDw/CreateTweet"
    headers = {
        "Host": "api.twitter.com",
        "Cookie": 'guest_id_marketing=v1%3A167086644521985376; guest_id_ads=v1%3A167086644521985376; _ga=GA1.2.2062832727.1670866452; kdt=KWyuVPHOOM5Xvw76DMgfSnDiDUJT67NUV8j1WAHp; auth_multi="1604164997457641472:73b8904130de6e52534be815a516ae7f5629d2a5"; auth_token=0eaebd2dbe6bbabd0f2ce728fe602df629cccb8f; personalization_id="v1_Vk3tBGwZA3NQ4e/GNmaxkA=="; guest_id=v1%3A167148540519027900; twid=u%3D1600754829957025792; ct0=033e61fe562dcec72419ab8504e1dd62dc01da4383a5e0fc3a3412989fabf20c0676e231fd8329d497798db1a4ec2a99d4fb9ce00f50985b747f52a7f68ca79185061502a1a71f5c5f58ade1e1ac1ba9; _gid=GA1.2.1451064700.1673696436', 
        "Content-Length": "1107",
        "Sec-Ch-Ua" : '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        "X-Twitter-Client-Language": "en",
        "X-Csrf-Token": '033e61fe562dcec72419ab8504e1dd62dc01da4383a5e0fc3a3412989fabf20c0676e231fd8329d497798db1a4ec2a99d4fb9ce00f50985b747f52a7f68ca79185061502a1a71f5c5f58ade1e1ac1ba9',
        "Sec-Ch-Ua-Mobile": '?0',
        "Authorization": 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
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

    data = {"variables":{"tweet_text":tweet_text,"dark_request":False, "media":{"media_entities":[],"possibly_sensitive":False},"withDownvotePerspective":False,"withReactionsMetadata":False,"withReactionsPerspective":False,"withSuperFollowsTweetFields":True,"withSuperFollowsUserFields":True,"semantic_annotation_ids":[]},"features":{"view_counts_public_visibility_enabled":True,"view_counts_everywhere_api_enabled":True,"longform_notetweets_consumption_enabled":False,"tweetypie_unmention_optimization_enabled":True,"responsive_web_uc_gql_enabled":True,"vibe_api_enabled":True,"responsive_web_edit_tweet_api_enabled":True,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":True,"interactive_text_enabled":True,"responsive_web_text_conversations_enabled":False,"responsive_web_twitter_blue_verified_badge_is_enabled":True,"verified_phone_label_enabled":True,"standardized_nudges_misinfo":True,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":False,"responsive_web_graphql_timeline_navigation_enabled":True,"responsive_web_enhance_cards_enabled":False},"queryId":"yL4KIHnJPXt-JUpRDrBDDw"}
    response = requests.post(url, headers=headers, json=data)