"""
Music Recommendation Project
CIS 351 
Arthur Gramlich
https://developer.spotify.com/documentation/web-api
https://tastedive.com/read/api
"""

import requests
import base64


def SpotifyCall():
    ClientID = 'fc6f168611ea4070a649c258c141a82a'
    ClientSecret = 'f33b999e8e8a4e6982cbaaf093de97cb' 
    AuthString = f'{ClientID}:{ClientSecret}' 
    B64Auth = base64.b64encode(AuthString.encode()).decode() #encode the user's info for Authorization header

    TokenUrl = 'https://accounts.spotify.com/api/token' 
    
    headers = {
    'Authorization': f'Basic {B64Auth}'  #Authentication for spotify API call
} 
    data = {
        'GrantType': 'ClientCredentials' #verifies the client credentials flow with the API
    }

    response = requests.post(TokenUrl, headers=headers, data=data) #requests access token from token URL
    AccessToken = response.json().get('access_token') #gets access token and converts it from json format 
    
    searchUrl = 'https://api.spotify.com/v1/search'
    searchHeaders = {
        'Authorization': f'Bearer {AccessToken}'  #Use the access token to authorize the request
    }
    searchParams = {
        'q': 'Adele',      #query term placeholder to be replaced by user input 
        'type': 'artist',   #type placeholder to be replaced later
        'limit': 5         #result limit set to 5
    }

    searchResponse = requests.get(searchUrl, headers=searchHeaders, params=searchParams)
    SpotifyResults = searchResponse.json()  #convert the json response to a python dictionary

def TastediveCall ():
    TastediveUrl = 'https://tastedive.com/api/similar'
    
    params = {
        'q': 'Adele',
        'type': 'music', #hard set to music recommendations
        'limit': '5', #result limit set to 5
        'k': '1049043-CIS351Mu-3297E7B1' 
    }
    
    response = requests.get(TastediveUrl, params=params) 
    TastediveResults = response.json() #converts json response to python dictionary
    
"""Next Step is to get the user input for each parameter and add to a combined dictionary of recommendations."""