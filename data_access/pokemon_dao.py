import pandas as pd

class PokemonDataAccess(object):

    def __init__(self):
        self.df = pd.read_csv('pokemon.csv')


    def get_stats(self, code):
        # this should return a pre-set dataframe in the format expected by the repo



        df = self.df[['name','attack', 'defense', 'speed']]
        pokemon_stats = df.loc[df['name'] == code]
        
        return pokemon_stats
        
    def get_capture_rate(self, code):
        # this should return a pre-set dataframe in the format expected by the repo
        df = self.df[['name','capture_rate']]
        pokemon_capture_rate = df.loc[df['name'] == code]
        
        return pokemon_capture_rate      
        


    def get_gen_info(self, code):
        # this should return a pre-set dataframe in the format expected by the repo
         # this should return a pre-set dataframe in the format expected by the repo
        df = self.df[['name','abilities', 'classfication', 'pokedex_number', 'generation']]
        pokemon_gen_info = df.loc[df['name'] == code]
        return pokemon_gen_info        