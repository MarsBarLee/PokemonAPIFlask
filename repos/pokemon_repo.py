# pokemon_repo.py is the Controller of the MVC pattern.
import json
import pandas as pd

class PokemonRepo(object):

    def __init__(self, da):
        self.__datastore = da

    def get_stats(self, code):
        result = self.__datastore.get_stats(code) # refer to pokemon_dao.py which is the Model of MVC pattern, for how get_status function works
        if result is None:
            return None
        return result.to_json(orient='records')
            # Encoding/decoding a Dataframe using 'records' formatted JSON. Dataframe is default is ‘columns’ allowed values are: {‘split’,’records’,’index’,’columns’,’values’,’table’}
            # Controller of MVC pattern

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

