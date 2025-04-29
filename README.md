# Python-Project-CIS351

## Music Recommendation Project [code](Final.py)

### Introduction
**Description**: This console-based project utilizes the public Spotify API to accept user input for music recommendations. The user will be prompted for an artist, genre, if they want to specify a year of the music's release, and if they would like explicit content. It will repeat this process until a user would like to exit or get their list of recommendations. Once they are done, they will get a list of songs with an artist's name that are similar to their criteria. 

**Key Features**:
+ Spotify API Implementation - The project works uses the Spotify API to retrieve recommendations. [API link](https://developer.spotify.com/documentation/web-api) 
+ API ID encoding – The program utilizes Base64 encoding to convert the user token before including it in the API’s authorization header.
+ API query conversion - The user's preferences will be converted to a string to match the API's search crtieria and design. 
+ Customizable Filtering - The program utilizes basic input handling to accept user preferences while also having error handling logic. 

### Interface Design

**API Usage**: The API credentials are accepted in json format. It has two sections; the header, and the data. These are returned to the API based on the token URL. Once the access token is accepted, the query can be accepted. The query is a string that is split based on the search criteria for each input. 

**Errors and Exceptions**: The program has error handling in the user input section to ensure there is a string entered into the program. If the string does not match what the API has, there will be no recommendations given to the user. There is specific error handling for the year and explicit content acceptance, as they are optional criteria. 

### Assumptions and Dependencies 

**Accessbility**: Since the program utilizes API calls, it may not work on public IDE's. A user will need to have their own IDE downloaded on their system to access the program. 
