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

Understanding the weight formula:

Weight can help us identify what features are more (or less) important for a user. For example, user can care more about the genre and less about energy (or more about the mood of a song than the genre, etc.). However, it is important to keep it balanced because if we say that the right genre adds +100 points, while mood adds only 5 points, for example, then genre will be dominant and overpower everything else and our recommender will recommend only songs from the same genre and will ignore other features that can be important to the user -> not optimal solution.

Based on the previous Copilot's suggestion we can use the following weight formula:

Total = genre points + mood points + weighted energy score

Where:

Genre match -> + 3 points (mismatch -> 0 mpointe)
Mood match -> + 2 points (mismatch -> 0 points)
Energy Score = 1 - abs(actual song energy - user preferred energy)

### PROMPT 5:

Explain this scoring formula in simple words: genre match +3, mood match +2, and energy similarity based on 1 - |song_energy - user_energy|.

![Explanation](screenshots/img5.png)

For my first scoring formula, I decided to keep it simple:

- genre match = +3 points
- mood match = +2 points
- energy similarity = 1 - |song_energy - user_energy|

The final score is the sum of all three parts. This makes genre the strongest factor, mood the second strongest factor, and energy a smaller affecting feature.

If we wanted energy to have a bit bigger effect -> we could multiply our energy by additional weight

### Manually computing a song score:

Song 1 Example: "Happy" by Pharrell Williams

genre = "pop" -> match -> +3 points
mood = "happy" -> match -> +2 points
energy = "high" (maybe 0.9) -> 1 - |0.8 - 0.8| = 1 - 0 = 1
Total Score = 3 + 2 + 1 = 6

Song 2 Example: "Frozen" by Madonna

genre = "pop" -> match -> +3 points
mood = "chill" -> no match -> 0 points
energy = "mid" (maybe 0.4) -> 1 - |0.4 - 0.8| = 1 - 0.4 = 0.6
Total Score = 3 + 0 + 0.6 = 3.6

### Predicting which song ranks first:

Song "Happy" will rank higher because its total Score is 6 (> 3.6 of "Frozen" song)

PROMPT 6: Spotting weight imbalance issues

Using songs.csv, I am using this scoring formula:

- genre match = +3
- mood match = +2
- energy similarity = 1 - |song_energy - user_energy|

Can you identify possible weight imbalance issues in this recommender and explain how they might affect which songs rank first? Please keep the explanation simple and beginner-friendly.

![Explanation](screenshots/img6.png)

=> The weights decide what the recommender cares about most. In our formula, genre matters the most, mood matters next, and energy only fine-tunes the ranking. That means songs with the right genre can sometimes rank too high, even if other parts of the match are weaker.

### PROMPT 7: Finalizing our Scoring System:

Let's finalize our "algorithm recipe" based on the following scoring system:
Finalize your recipe. A common starting point is:
+2.0 points for a genre match.
+1.0 point for a mood match.
Similarity points based on how close the song's energy is to the user's target.

![Explanation](screenshots/img7.png)

---

PHASE 3: Implementation
