import json
import pandas as pd

class PokemonRepo(object):

    def __init__(self, da):
        self.__datastore = da

    def get_stats(self, code):
        result = self.__datastore.get_stats(code)
        if result is None:
            return None
        return result.to_json(orient='records')

    def get_gen_info(self, code):
        result = self.__datastore.get_gen_info(code)
        if result is None:
            return None
        return result.to_json(orient='records')

    def get_capture_rate(self, code):
        result = self.__datastore.get_capture_rate(code)
        if result is None:
            return None
        return result.to_json(orient='records')

