# Import package
import urllib3, requests, json

# Set up request credential infor
api_key = "02834833a9dfe29dc2c55eb707c5a73c"
example_api_request = "https://api.themoviedb.org/3/movie/550?api_key="+api_key
bearer_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMjgzNDgzM2E5ZGZlMjlkYzJjNTVlYjcwN2M1YTczYyIsInN1YiI6IjVmNTE4YjEyNWFhZGM0MDAzMzY3MDZhNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.vExhd12qTYMuJPzRMRCQE9_W63_ReWbv98ANIdXb5jc"


def get_imdb_movies():
    response = requests.get(example_api_request)    # Get response message
    json_data = response.json()     # get json object
    parse_data = json.dumps(json_data, indent=4, sort_keys=True)    # conver json to str for pretty format
    print(parse_data)


    return parse_data