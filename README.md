# RecommendationEngine-A recommendation engine is a type of data filtering tool using machine learning algorithms to recommend the most relevant items to a particular user or customer.
## Code-Here i have uploaded my jupyter notebook file and python file of my code of recommendation engine.To run the code on your pc,please edit the path of ratings.csv and movies.csv files in the code.Please enter the path where these dataset files are stored on your pc.
### Dataset- The dataset used in my code has also been uploaded here which consists of four csv files.
            * All ratings are contained in the file `ratings.csv`. Each line of this file after the header row represents one rating of one movie by one user, and has                 the following format:
              userId,movieId,rating,timestamp
            * All tags are contained in the file `tags.csv`. Each line of this file after the header row represents one tag applied to one movie by one user, and has the               following format:
              userId,movieId,tag,timestamp
            * Movie information is contained in the file `movies.csv`. Each line of this file after the header row represents one movie, and has the following format:
              movieId,title,genres
            * Identifiers that can be used to link to other sources of movie data are contained in the file `links.csv`. Each line of this file after the header row                   represents one movie, and has the following format:
              movieId,imdbId,tmdbId
