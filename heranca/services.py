import requests

API_URL = "http://api.herocheck.com/?q={0}"


class SuperHeroWebAPI:

    @staticmethod
    def is_hero(username):
        blacklist = {"syndrome", "kcka$$", "superfake"}
        url = API_URL.format(username)
        return username not in blacklist and requests.get(url)
