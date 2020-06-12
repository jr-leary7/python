import spotipy
import spotipy.util as util
import pandas as pd

spotipy_client_id='e366087d4535430dad643cc75ef3d834'
spotipy_client_secret='4523680ffab8465491ddc6b6d7a4331b'
spotipy_redirect_uri='https://developer.spotify.com/dashboard/applications/e366087d4535430dad643cc75ef3d834'

scope = 'user-library-read'
username = '12138762894'

#token = util.prompt_for_user_token(username, scope, client_id=spotipy_client_id, client_secret=spotipy_client_secret, redirect_uri=spotipy_redirect_uri)