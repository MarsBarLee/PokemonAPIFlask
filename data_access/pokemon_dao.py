# pokemon_dao.py is the Model of the MVC pattern. The Model takes information from the database, our pokemon.csv. We use Restful API 
import pandas as pd

class PokemonDataAccess(object):

    def __init__(self):
        self.df = pd.read_csv('pokemon.csv') # use pandas to read csv


    def get_stats(self, code):
        # this should return a pre-set dataframe(rows, columns) in the format expected by the repository
        # df['column_name']
        df = self.df[['name','attack', 'defense', 'speed']] # selecting specific columns. the kaggle csv has multple columns to choose from
        pokemon_stats = df.loc[df['name'] == code]
            # Acess dataframe, return those with column name = name you're looking for in url. In pokemons.py, @pokemons.route('/pokemon/stats/<code>
            # pandas.DataFrame.loc. Access a group of rows and columns by labels
        
        return pokemon_stats # return the column values. Will be jsonified in pokemon_repo.py which is the Controller of MVC controller
        
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