import requests
import base64

def SpotifyToken():
    ClientID = 'fc6f168611ea4070a649c258c141a82a'
    ClientSecret = 'f33b999e8e8a4e6982cbaaf093de97cb' 
    AuthString = f'{ClientID}:{ClientSecret}' 
    B64Auth = base64.b64encode(AuthString.encode()).decode() #encode the user's info for Authorization header

    TokenUrl = 'https://accounts.spotify.com/api/token' 
    
    headers = {
    'Authorization': f'Basic {B64Auth}'  #Authentication for spotify API call
} 
    data = {
        'grant_type': 'client_credentials' #verifies the client credentials flow with the API
    }

    response = requests.post(TokenUrl, headers=headers, data=data) #requests access token from token URL
    AccessToken = response.json().get('access_token') #gets access token and converts it from json format 
    return AccessToken  # Make sure to return the token

def preferences():  #get user preferences for search parameters
    artist = input("What artist would you like recommendations for? ").capitalize()
    genre = input("What genre would you like recommendations for? ").capitalize()

    while True: #year answer must be yes or no
        yearAnswer = input("Do you want to filter by a specific year? (yes/no): ").lower()
        if yearAnswer in ['yes', 'no']:
            break
        print("Please enter 'yes' or 'no'.")

    if yearAnswer == 'yes':
        year = input("What year would you like the music to be from? ")
    else:
        year = ""

    while True: #explicit content answer must be yes or no
        explicitAnswer = input("Would you like explicit content? (yes/no): ").lower()
        if explicitAnswer in ['yes', 'no']:
            break
        print("Please enter 'yes' or 'no'.")
    allowExplicit = explicitAnswer == 'yes'

    return artist, genre, year, allowExplicit

def UseSpotify(artist, genre, year, allowExplicit): 
    query = [] #based on user answers for later search 
    if artist:
        query.append(f'artist:{artist}') 
    if genre: 
        query.append(f'genre:{genre}') 
    if year:
        query.append(f'year:{year}') 
    
    AccessToken = SpotifyToken()
    if not AccessToken:
        return 
    
    searchUrl = 'https://api.spotify.com/v1/search'
    searchHeaders = {'Authorization': f'Bearer {AccessToken}'}
    searchParams = {
        'q': ' '.join(query), #makes the list into a query string
        'type': 'track',
        'limit': 10
    }

    searchResponse = requests.get(searchUrl, headers=searchHeaders, params=searchParams)
    results = searchResponse.json() 
    
    tracks = []
    for track in results.get('tracks', {}).get('items', []):
        if allowExplicit or not track['explicit']:
            tracks.append({
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'year': track['album']['release_date'],
                'explicit': track['explicit']
            })
    
    return tracks

def main():
    access_token = SpotifyToken()

    songs = [] #final list of song recommendations 
    
    while True: #loops if the user wants more recommendations or recommendations for different artists
        artist, genre, year, allowExplicit = preferences() 
        tracks = UseSpotify(artist, genre, year, allowExplicit)

        if tracks:
            print("\nRecommended Tracks:")
            for track in tracks:
                print(f"Name: {track['name']}, Artist: {track['artist']}, Date: {track['year']}, Explicit: {track['explicit']}")
                songs.append(f"{track['name']} by {track['artist']}")
        else:
            print("No tracks found based on your preferences.")

        moreRecs = input("\nWould you like more recommendations? Type 'yes' to continue, or press any key to exit and get your list of recommendations. ")
        if moreRecs.lower() != 'yes':
            print("\nFinal list of recommended songs:")
            print(', '.join(songs)) 
            break

if __name__ == '__main__':
    main()