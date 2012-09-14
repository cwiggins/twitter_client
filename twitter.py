from twython import Twython
from format_timeline import *
import os
oauth_tokens = open('oauth_tokens','r')
app_key = oauth_tokens.readline()
app_secret = oauth_tokens.readline()
oauth_token = oauth_tokens.readline()
oauth_token_secret = oauth_tokens.readline()

t = Twython(app_key = app_key.strip('\n'), app_secret = app_secret.strip('\n'),
        callback_url = 'http://google.com')

auth_props = t.get_authentication_tokens()
print 'Connect to Twitter via: %s' % auth_props['auth_url']

t = Twython(app_key = app_key.strip('\n'), app_secret = app_secret.strip('\n'),
        oauth_token = oauth_token.strip('\n'), oauth_token_secret = oauth_token_secret.strip('\n'))
homeTimeline = format_timeline(t.getHomeTimeline())

#print homeTimeline

#update = raw_input('>' )
t.updateStatus(status = update)
