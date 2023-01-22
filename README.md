# Python and Neo4j GraphDB
This project was an assignment as part of my master's degree at Macquarie University. The assignment consisted of multiple tasks:
1. Write a [program](https://github.com/felix-rosenberger/Assignment-2-Python-and-GraphDB/blob/master/tweet_curation.py) to clean wrongly formatted JSON file containing 10000 tweets
2. Use the JSON file to [create the data model in the Neo4j GraphDB](https://github.com/felix-rosenberger/Assignment-2-Python-and-GraphDB/blob/master/Graph_Model_Queries.ipynb). The respective nodes are:
- Tweet
- Source
- Retweet
- Link (Tweet URL)
- Hashtag
- User
- Mentioned User \
\
All nodes are then connected through relationships.
3. [Query the graph data model](https://github.com/felix-rosenberger/Assignment-2-Python-and-GraphDB/blob/master/Graph_Queries.ipynb) for the following problems:
- Find the top five most used sources (app or site) to post or share a tweet. For each source return the source name and the number of tweets sent via that source.
- Find the top five most used hashtags across all tweets on each day between 26th and 31st March 2016 (inclusive). For each day, return the date and a list of the five top hashtags in order of popularity on that day.
- Find all users that use any of the same hashtags as user "m_mrezamm". This query must exclude any retweets since these posts would automatically contain common tags. The query must return the user name and the number of hashtags that were used in their tweets that are also used by "m_mrezamm". Order results by the number of hashtags used in common.
- The original dataset does not contain information about which users follow each other. For this exercise we will infer that any user that MENTIONS another user in a tweet FOLLOWS that user. Write a Cypher expression which creates FOLLOW relationships based on this assumption, for example if UserA mentions UserB in a tweet, then it is assumed that UserA FOLLOWS UserB. Each FOLLOWS relationship added to the graph should also have a ‘weight’ property with a value of 1.
- Using the FOLLOWS relationship derived in Problem 4, use the Neo4j Graph Data Science library to calculate the most popular nodes using Degree Centrality from the FOLLOWS subgraph. Then, find the top five users with the highest Degree Centrality score. (consider using NATURAL orientation and the weight property for the graph projection).
