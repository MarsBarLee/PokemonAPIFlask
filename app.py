from flask import Flask, request
from views import pokemons
from data_access import PokemonDataAccess
from flasgger import APISpec, Schema, Swagger, fields



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
