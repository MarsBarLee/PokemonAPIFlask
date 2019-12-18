# pokemons.py is the View of the MVC pattern.
# this file is equivalent to Routes in Node (I think?)

from flask import Blueprint, abort, current_app, g
 # Blueprints are like React components: A blueprint defines a collection of views, templates, static files and other elements that can be applied to an application. For example, let’s imagine that we have a blueprint for an admin panel. This blueprint would define the views for routes like /admin/login and /admin/dashboard
import json
from repos import PokemonRepo
  # from views->pokemon_repo.py, import the class PokemonRepo
from data_access import PokemonDataAccess
from flasgger import Swagger

pokemons = Blueprint('pokemons', __name__)

@pokemons.route('/pokemon/stats/<code>', methods = ['GET']) # code is pokemon's name
def by_stats(code):
    repo = PokemonRepo(PokemonDataAccess())
    response = repo.get_stats(code)

    if (response == None):
        abort(404)
    return response
      # View of MVC pattern. Already JSONified on pokemon_repo.py which is the Model of MVC pattern

@pokemons.route('/pokemon/capture_rate/<code>', methods = ['GET'])
def capture_rate(code):
    repo = PokemonRepo(PokemonDataAccess())
    response = repo.get_capture_rate(code)

    if (response == None):
        abort(404)
    return response

      
@pokemons.route('/pokemon/general_info/<code>', methods = ['GET'])
def gen_info(code):
    repo = PokemonRepo(PokemonDataAccess())
    response = repo.get_gen_info(code)

    if (response == None):
        abort(404)
    return response





