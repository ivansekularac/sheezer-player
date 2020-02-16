import requests
import json

class RapidAPI:

    __headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "3060c38672msha6ca68fb91aa196p106ce5jsn9c6ba1778834"
    }

    @staticmethod
    def track_call(id):
        url = "https://deezerdevs-deezer.p.rapidapi.com/track/" + str(id)
        response = requests.request("GET", url, headers=RapidAPI.__headers)
        return response.json()

    @staticmethod
    def search(keywords):
        url = "https://deezerdevs-deezer.p.rapidapi.com/search"
        querystring = {"q":f"{ keywords }"}
        response = requests.request("GET", url, headers=RapidAPI.__headers, params=querystring).json()
        return response['data']


class Converter:

    @staticmethod
    def hhmmss(ms):
        # s = 1000
        # m = 60000
        # h = 360000
        h, r = divmod(ms, 360000)
        m, r = divmod(r, 60000)
        s, _ = divmod(r, 1000)
        return ("%d:%02d:%02d" % (h,m,s)) if h else ("%d:%02d" % (m,s))