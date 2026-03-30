## PHASE 1: Understanding Recommenders

### PROMPT 1: Understanding "Content-based vs collaborative filtering":

Explain the difference between content-based filtering and collaborative filtering in simple words for this music recommender project.

![Explanation](screenshots/img1.png)

### PROMPT 2: Understanding songs.csv structure

Look at the songs.csv file and explain which features are the most useful for a simple content-based recommender and why.

![Explanation](screenshots/img2.png)

### PROMPT 3: Identifying key features

For this project, would genre, mood, and energy be enough as the main features for a first version of the recommender? I want to keep it simple at the beginning and maybe use the other features later as refinements.

![Explanation](screenshots/img3.png)

### Defining our own “algorithm recipe”:

This recommender needs to:

- Identify user's preferences like genre, mood, and energy level.
- Look at each song in the dataset and compare it to the user's preferences:
  - If a song matches user's genre -> add points (otherwise, don't add anything)
  - If a song matches user's mood -> add points (otherwise, don't add anything)
  - If a song has the same energy level or very similar -> add more points, otherwise add less
- Calculate total points for each song
- Sort the list based on the total points
- Recommend songs starting with the songs that received the most points first and then those that got less.

### PROMPT 4: Checking our "algorithm recipe" with Copilot's suggestion:

Here's my simple algorithm for this music recommender:

This recommender will:

- Identify the user's preferences, such as genre, mood, and energy level.
- Look at each song in the dataset and compare it to the user's preferences:
  - If a song matches the user's genre, add points.
  - If a song matches the user's mood, add points.
  - If a song's energy level is close to the user's target energy, add more points. If it is less similar, add fewer points.
- Calculate a total score for each song.
- Sort all songs based on their total score.
- Recommend the songs with the highest scores first.

Is this a good beginner-friendly algorithm for this task? Please improve it if needed, but keep it simple enough.

![Explanation](screenshots/img4.png)

=> For the first version of my recommender, I want to keep the system simple by focusing on three main features: genre, mood, and energy. Genre will have the strongest weight (most points), mood will also add points (next most), and energy will help to improve the ranking by preferring songs whose energy level is closer to the user's target. Once every song gets a total score, the system will sort the songs in descending order and recommend the highest-scoring songs first. Later, I can improve the recommender by adding smaller refinements such as tempo, valence, danceability, and acousticness.

---

## PHASE 2: Designing Scoring Logic

Understanding the weight formula
Manually computing a song score
Predicting which song ranks first
Spotting weight imbalance issues
