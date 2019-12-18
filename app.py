from flask import Flask, request
from views import pokemons
from data_access import PokemonDataAccess
# from here: https://www.kaggle.com/rounakbanik/pokemon
from flasgger import APISpec, Schema, Swagger, fields
# Flasgger(Flask+Swagger) is a Flask extension to extract OpenAPI-Specification from all Flask views registered in your API.
# Swagger is a simple yet powerful representation of your RESTful API. With the largest ecosystem of API tooling on the planet, thousands of developers are supporting Swagger in almost every modern programming language and deployment environment. With a Swagger-enabled API, you get interactive documentation, client SDK generation and discoverability.

app = Flask(__name__)

# spec = APISpec(
#     title='Entity API',
#     version='1.0.10',
#     openapi_version='2.0'
# )
# template = spec.to_flasgger(app)
# swagger = Swagger(app, template=template)
swagger = Swagger(app)

app.register_blueprint(pokemons)






@app.route("/", methods = ['GET'])
def hello():
    return """
<html>
   <body>
      <h1>Welcome to the Pokemon API!</h2>
   </body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
