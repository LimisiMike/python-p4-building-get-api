from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Review, Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "<h1>Index for Game/Review/User API</h1>"

@app.route('/games')
def games():

    games = []
    for game in Game.query.all():
        game_dict = {
            "title": game.title,
            "genre": game.genre,
            "platform": game.platform,
            "price": game.price,
        }
        games.append(game_dict)

    response = make_response(
        jsonify(games),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response
# Sorting by title => games_by_title = Game.query.order_by(Game.title).all()
# Return the first 10 games => first_10_games = Game.query.liit(10).all()

@app.route('/games/<int:id>')
def game_by_id(id):
    game = Game.query.filter_by(id=id).first()


    # if game is None:
    #     response_body = {'error': 'Game not found'}
    #     response = make_response(jsonify(response_body), 404)
    #     response.headers["Content-Type"] = "application/json"
    #     return response
    # --------------------No need of this commented section---------------
    # game_dict = {
    #     "title": game.title,
    #     "genre": game.genre,
    #     "platform": game.platform,
    #     "price": game.price,
    # }
    
    game_dict = game.to_dict()

    response = make_response(
        jsonify(game_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response

if __name__ == '__main__':
    app.run(port=5555)