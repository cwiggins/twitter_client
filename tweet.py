class twitter_user(object):
	def __init__(self, contributors_enabled = False, created_at = None,
            default_profile_image = True, description = None, favorites_count = None,
            followers_count = None, friends_count = None, geo_enabled = False,
            id_str = None, is_translator = False, lang = None, listed_count = None,
            location = None, name = None, profile_image_url = None,
            profile_image_url_https = None, profile_use_background_image = True,
            protected = False, screen_name = None, status = None,
            statuses_count = None, time_zone = None, url = None, utc_offset = None,
            verified = None, withheld_in_countries = None, withheld_scope = None):
        self.contributors_enabled = contributors_enabled
        self.created_at = created_at
        self.default_profile_image = default_profile_image

