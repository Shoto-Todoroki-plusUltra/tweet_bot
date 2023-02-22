# tweet_bot

So basically, this is a tweet bot (as the name suggests). This bot sends tweets in a given time interval. The tweets sent are preferably in tracery, but you can make your own "pattern" of tweets in the get_text.py file. For now the get_text.py file is written for tracery.

To deploy it, first set up the get_text.py file, if you're using tracery, then it's already in order! In that case all you have to do is to write your tracery json into tracery_json.json file.

Next, go to the send_req_.py file and enter your cookies. Of course a template for it is already created and the "xxx" will have to be replaced by your cookies. You can get your cookies, preferably, using Burp Suite (https://portswigger.net/burp) by intercepting your request on twitter.
To do so, first download and start burp suite and also, preferably foxyproxy extension for chrome (https://chrome.google.com/webstore/detail/foxyproxy-standard/gcknhkkoolaabfmlnjonogaaifnjlfnp?hl=en).
Then, go to chrome and open twitter website and sign into it. And set foxyproxy to a given address (say 127.0.0.1:8080).
Now go to burp suite and click on proxy tab. Click on "Intercept is off" to turn it on.
Now write any random tweet, and click tweet. You may see some actuvity on burp suite (or may have already seen), click on drop until you see a post request to something like https://api.twitter.com/xxx/CreateTweet (xxx is user specific). Now copy the specifics like cookies and the url and paste it into send_req_.py into the right places.

Now, go to your nextTime.txt file and enter nothing else (not even a space or new line) but the time you want your first tweet to go in, after epoch in seconds (you can get present time passed since epoch using:
from time import time
print(time())
)

Now, go to your interval.txt file and enter (once again) nothing else but the interval in which the tweets should be sent in seconds. Basically the time difference between the two tweets.

Now, everything is in order. Go to your server and start final.py file.
You can deploy your project at github actions.

:)💜💜
