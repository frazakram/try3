from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import pickle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///searches.db'
db = SQLAlchemy(app)

class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String(150), nullable=False)

db.create_all()

# Load the model and other necessary files
with open('model_components.pkl', 'rb') as file:
    cv, similarity, newmovies = pickle.load(file)

def recommend(movie):
    try:
        index = newmovies[newmovies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        return [newmovies.iloc[i[0]].title for i in distances[1:6]]
    except IndexError:
        return []

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/recommend', methods=['GET'])
def get_recommendations():
    movie = request.args.get('movie')
    if not movie:
        return jsonify({'error': 'Please provide a movie title'}), 400

    # Log the search to the database
    new_search = Search(movie=movie)
    db.session.add(new_search)
    db.session.commit()

    recommendations = recommend(movie)
    if not recommendations:
        return jsonify({'error': 'Movie not found or no recommendations available'}), 404

    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
