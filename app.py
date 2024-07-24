from flask import Flask, jsonify, request, render_template
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Flask app
app = Flask(__name__)

# Load model components
with open('model_components.pkl', 'rb') as file:
    cv, similarity, newmovies = pickle.load(file)

# Define recommendation function
def recommend(movie):
    index = newmovies[newmovies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = [newmovies.iloc[i[0]].title for i in distances[1:6]]
    return recommended_movies

# Define endpoint for recommendations
@app.route('/recommend', methods=['GET'])
def get_recommendations():
    movie_name = request.args.get('movie')
    if not movie_name:
        return jsonify({'error': 'Missing parameter: movie'}), 400
    
    recommendations = recommend(movie_name)
    return jsonify({'recommendations': recommendations})

# Define index page
@app.route('/')
def index():
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
