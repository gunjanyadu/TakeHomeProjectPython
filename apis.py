from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load the normalized data
normalized_data = pd.read_csv('normalized_data.csv', index_col='index')

# Bonus: Adding a placeholder column for star rating
normalized_data['star_rating'] = 0.0

# Enable CORS for all routes to allow cross-origin requests
# (You may want to restrict this in a production environment)
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# API to get all items in the normalized data set with pagination support
@app.route('/api/all_items', methods=['GET'])
def get_all_items():
    page = int(request.args.get('page', 1))
    items_per_page = int(request.args.get('items_per_page', 10))
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    paginated_data = normalized_data.iloc[start_index:end_index].to_dict(orient='records')
    return jsonify(paginated_data)

# API to get all attributes of a song by title
@app.route('/api/song_attributes', methods=['GET'])
def get_song_attributes():
    title = request.args.get('title')
    song_data = normalized_data[normalized_data['title'] == title].to_dict(orient='records')
    return jsonify(song_data)

# API to rate a song
@app.route('/api/rate_song', methods=['POST'])
def rate_song():
    data = request.get_json()
    title = data.get('title')
    rating = data.get('rating')
    normalized_data.loc[normalized_data['title'] == title, 'star_rating'] = rating
    return jsonify({'message': 'Rating updated successfully'})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
