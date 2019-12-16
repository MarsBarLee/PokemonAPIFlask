from flask import Blueprint, abort, current_app, g
import json
from repos import PokemonRepo
from data_access import PokemonDataAccess
from flasgger import Swagger

pokemons = Blueprint('pokemons', __name__)

@pokemons.route('/pokemon/stats/<code>', methods = ['GET'])
def by_stats(code):
    """Returns CSCompanyID corresponding to given ticker
    ---
      responses:
        200:
          description: CSCompanyID as int, 6 digits minimum
          examples:
            [[902100]]
    """
    repo = PokemonRepo(PokemonDataAccess())
    response = repo.get_stats(code)

    if (response == None):
        abort(404)
    return response

@pokemons.route('/pokemon/capture_rate/<code>', methods = ['GET'])
def capture_rate(code):
    """Returns a valid response corresponding to given cscompanyid
    ---
      responses:
        200:
          description: returns a valid CSCompanyID as int, 6 digits minimum
          examples:
            [[123456]]
    """
    repo = PokemonRepo(PokemonDataAccess())
    response = repo.get_capture_rate(code)

    if (response == None):
        abort(404)
    return response

      
@pokemons.route('/pokemon/general_info/<code>', methods = ['GET'])
def gen_info(code):
    """Returns columns providing details on specific pokemons
    ---
      responses:
        200:
          description: row of col:'companyId parentCompanyId ultimatParentCompany displayName properName st company details based on company index given.ate zipcode isoCountryCode isoCurrencyCode bloombergTicker'
          examples:
           '[1,11,111,"361","361 Degrees","new york",11111,"USA","USD","1361HK"]'

    """
    repo = PokemonRepo(PokemonDataAccess())
    response = repo.get_gen_info(code)

    if (response == None):
        abort(404)
    return response





