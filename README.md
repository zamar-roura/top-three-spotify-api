To launch

ENV:
SPOTIPY_CLIENT_ID='a151833fa5834cecaded3ce6cbd3f906'
SPOTIPY_CLIENT_SECRET='5ea4b9377f3d49db91379181e016cbac'
SPOTIPY_REDIRECT_URI='https://zamar-roura.com'



docker run -e SPOTIPY_CLIENT_ID="a151833fa5834cecaded3ce6cbd3f906" -e SPOTIPY_CLIENT_SECRET="5ea4b9377f3d49db91379181e016cbac" -e SPOTIPY_REDIRECT_URI="https://zamar-roura.com" -d three-top-three 

Run python through inside docker first and make code accepted.