#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
#get the data
data=pd.read_csv('/Users/chiragbansal/Downloads/ratings.csv')
data.head(50)


# In[2]:


#get the data
movie_titles_genre=pd.read_csv('/Users/chiragbansal/Downloads/movies.csv')
movie_titles_genre.head(50)


# In[3]:


#merge the data of both the above tables
data=data.merge(movie_titles_genre,on='movieId',how='left')
data.head(50)


# In[4]:


#find average rating of each movie
Average_ratings=pd.DataFrame(data.groupby('title')['rating'].mean())
Average_ratings.head(50)


# In[5]:


#merge'Total Ratings' column to above table 
Average_ratings['Total Ratings']=pd.DataFrame(data.groupby('title')['rating'].count())
Average_ratings.head(50)


# In[6]:


#sort values according to 'Total Ratings' column
moviemat=data.pivot_table(index='userId',columns='title',values='rating')
moviemat.head()
Average_ratings.sort_values('Total Ratings',ascending=False,kind='mergesort').head(50)


# In[7]:


#create a table where the values of the matrix represent the rating for each movie by each user
movie_user = data.pivot_table(index='userId',columns='title',values='rating')
movie_user.head(50)


# In[8]:


#here i am choosing 'Toy Story (1995)' movie to test the recommender system
#find the correlation values for the selected movie with the other movies
correlations = movie_user.corrwith(movie_user['Toy Story (1995)'])
correlations.head(50)


# In[9]:


#remove all the empty values
recommendation = pd.DataFrame(correlations,columns=['Correlation'])
recommendation.dropna(inplace=True)
#merge 'Total Ratings' column to the correlation table
recommendation = recommendation.join(Average_ratings['Total Ratings'])
recommendation.head()


# In[10]:


#filter all the movies with a correlation value to Toy Story (1995) 
recc = recommendation[recommendation['Total Ratings']>100].sort_values('Correlation',ascending=False,kind='mergesort').reset_index()
#merge the movies dataset for verifying the recommendations
recc = recc.merge(movie_titles_genre,on='title', how='left')
recc.head(50)


# In[11]:


#We can see that the top recommendations are pretty good. The movie that has the highest/full correlation to Toy Story is Toy Story itself. The movies such as The Incredibles,Finding Nemo and Alladin show high correlation with Toy Story.


# In[ ]:




