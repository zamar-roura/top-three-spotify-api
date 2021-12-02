import spotipy
from spotipy.oauth2 import SpotifyOAuth
import logging
logging.basicConfig(filename='songs.log', level=logging.INFO)

# CONFIG FILES


PLAYLIST_PREFIX = "spotify:playlist:"
TRACK_PREFIX = "spotify:track:"

BERBEL_PLAYLIST = {"name":"Berbel Playlist","id":"37i9dQZF1EpzuvL0ktzBJ2"}
PEREZ_PLAYLIST = {"name":"Perez Playlist","id":"37i9dQZF1EpwUpNRS93jc7"}
ZAMAR_PLAYLIST = {"name":"Zamar Playlist","id":"37i9dQZF1EpmC3nNg7sL1z"}

PLAYLISTS = [ZAMAR_PLAYLIST, PEREZ_PLAYLIST, BERBEL_PLAYLIST]

THREE_TOP_THREE_PLAYLIST = "6CoDpuS2BbnKfTszk9eB38"


class ThreeTopThreeManager:
    def __init__(self) -> None:
        scope = 'playlist-modify-public'
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,open_browser=False))

    def playlist_contains_track(self, track_id, playlist_id):
        """
        Does the playlist contain X song?
        """
        offset = 0
        while True:
            response = self.sp.playlist_items(f"{PLAYLIST_PREFIX}{playlist_id}",
                                              offset=offset,
                                              fields='items.track.id,total',
                                              additional_types=['track'])
            if len(response['items']) == 0:
                break

            tracks = [track['track']['id'] for track in response['items']]
            if track_id in tracks:
                return True
            offset = offset + len(response['items'])
        return False

    def get_first_three(self, playlist_id):
        """
        Give me the top three songs of a playlist.
        In the case of 'On repeat' is the first three.
        """
        response = self.sp.playlist_items(f"{PLAYLIST_PREFIX}{playlist_id}",
                                          offset=0,
                                          fields='items.track.id,total',
                                          additional_types=['track'])
        return [track['track']['id'] for track in response['items'][0:3]]

    def insert_three_top_three(self):
        """
        Main function.
        """
        for playlist in PLAYLISTS:
            playlist_name = playlist['name']
            playlist_id = playlist['id']
            
            # Get the 3 songs!
            three_tracks = self.get_first_three(playlist_id)
            
            # If song is not in THREE TOP THREE. Add it!
            for track in three_tracks:
                if(not(self.playlist_contains_track(track, THREE_TOP_THREE_PLAYLIST))):
                    track_name = self.sp.track(f"{TRACK_PREFIX}{track}")['name']
                    logging.info(f"Adding {track_name} from {playlist_name}")
                    
                    self.sp.playlist_add_items(
                        THREE_TOP_THREE_PLAYLIST, [track])


if __name__ == "__main__":
    a = ThreeTopThreeManager()
    a.insert_three_top_three()

