import pandas as pd
import pickle
import random
import time
df_final = pickle.load(open('df_final.pkl','rb'))

cosine_similarity_array = pickle.load(open('cos_sim.pkl','rb'))

# Fetches the poster of a movie using movie id
def poster(movie_id):
    import requests
    web = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=d580ed432d7d56f0eb97549c4fcb2273&language=en-US'
    response = requests.get(web)
    try:
        return f"https://image.tmdb.org/t/p/original/{response.json()['poster_path']}"
    except:
        try:
            time.sleep(1)
            return f"https://image.tmdb.org/t/p/original/{response.json()['poster_path']}"
        except:
            return False


def trailer(movie_id):
    import requests
    web = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key=d580ed432d7d56f0eb97549c4fcb2273&language=en-US'
    response = requests.get(web)
    try:
        response.json()['results']
        trailer_df = pd.DataFrame(response.json()['results'])
        trailer_df['type'] = trailer_df['type'].str.lower()
        trailer_id= trailer_df[trailer_df['type']== 'trailer'].sample()['key'].values[0]
        link = 'www.youtube.com/watch?v={}'.format(trailer_id)
        return link
    except:
        try:
            time.sleep(1)
            response.json()['results']
            trailer_df = pd.DataFrame(response.json()['results'])
            trailer_df['type'] = trailer_df['type'].str.lower()
            trailer_id= trailer_df[trailer_df['type']== 'trailer'].sample()['key'].values[0]
            link = 'www.youtube.com/watch?v={}'.format(trailer_id)
            return link
        except:
            False


# The recommendation Function
# The recommendation Function
def recommend_list(movie):
    # retrieving the corresponding index for the movie.
    movie_idx = df_final[df_final['title'] == movie].index[0]

    # Getting the top 10 most similar movies. We get the indexes for movies using enumerate.
    no_of_similar_movies = 10
    movies = sorted(list(enumerate(cosine_similarity_array[movie_idx])), reverse=True, key=lambda x: x[1])[
             1:no_of_similar_movies]
    recommended_movies = []
    movie_trailers = []
    movie_posters = []
    # display the 6 movies randomly from 10 movies and thier genres as well.

    for movie_idx_sim_tuple in random.sample(movies, 6):
        movie_idx = movie_idx_sim_tuple[0]
        # Creating a list of recommended movies and  their genres
        recommended_movies.append((df_final.loc[movie_idx, 'title'], df_final.loc[movie_idx, 'Genre']))

        # Creating a list of movie trailers
        movie_trailers.append(trailer(df_final.loc[movie_idx, 'movie_id']))

        # Creating a list of movie posters
        movie_posters.append(poster(df_final.loc[movie_idx, 'movie_id']))
    return recommended_movies, movie_trailers, movie_posters



print(df_final.head())
