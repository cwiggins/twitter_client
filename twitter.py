from twython import Twython
from format_timeline import *
app_key = 'TkKK5AjoWzHSEdNejKiOQ'
app_secret = 'zs7fk3KBSjdBQdU0Mks5mr80mdCuUivzOWODoW8RyE'
oauth_token = '183630095-jvkb3yBqbbOVfM0liLYndJ7dOZbUnxnflKztIfyr'
oauth_token_secret = 'n5HOGg76QBWslzr4zBaDE70rUfk2siHtxRYIQL6Eyc'
t = Twython(app_key,
		app_secret,
		callback_url = 'http://google.com')

auth_props = t.get_authentication_tokens()

#oauth_token = auth_props['oauth_token']
#oauth_token_secret = auth_props['oauth_token_secret']

print 'Connect to Twitter via: %s' % auth_props['auth_url']

t = Twython(app_key, app_secret, oauth_token = oauth_token,
		oauth_token_secret = oauth_token_secret)

auth_tokens = t.get_authorized_tokens()

homeTimeline = format_timeline(t.getHomeTimeline())

#print homeTimeline

#update = raw_input('>' )
#t.updateStatus(status = update)
