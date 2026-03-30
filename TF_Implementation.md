## Summary:

In this project, we built a simple music recommender system that suggests songs based on a user's preferences. The recommender compares the user's preferred genre, mood, and energy level to the songs in the dataset, gives each song a score, and then ranks the songs from highest to lowest score.

The main goal of this project was to understand how recommendation systems make decisions, how scoring logic affects ranking, and how small design choices can create bias or unexpected results. We also used Copilot to help us think through the logic, implement the code, test different user profiles, and reflect on the strengths and limitations of the recommender.

## PHASE 1: Understanding Recommenders

### PROMPT 1: Understanding "Content-based vs collaborative filtering"

Explain the difference between content-based filtering and collaborative filtering in simple words for this music recommender project.

![Explanation](screenshots/img1.png)

### PROMPT 2: Understanding songs.csv structure

Look at the songs.csv file and explain which features are the most useful for a simple content-based recommender and why.

![Explanation](screenshots/img2.png)

### PROMPT 3: Identifying key features

For this project, would genre, mood, and energy be enough as the main features for a first version of the recommender? I want to keep it simple at the beginning and maybe use the other features later as refinements.

![Explanation](screenshots/img3.png)

### Defining our own “algorithm recipe”

This recommender needs to:

- Identify the user's preferences, such as genre, mood, and energy level.
- Look at each song in the dataset and compare it to the user's preferences:
  - If a song matches the user's genre, add points. Otherwise, do not add anything.
  - If a song matches the user's mood, add points. Otherwise, do not add anything.
  - If a song has the same energy level or a very similar energy level, add more points. Otherwise, add fewer points.
- Calculate the total points for each song.
- Sort the list based on the total points.
- Recommend the songs that received the highest scores first, followed by the songs that received lower scores.

### PROMPT 4: Checking our "algorithm recipe" with Copilot's suggestion

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

=> For the first version of my recommender, I wanted to keep the system simple by focusing on three main features: genre, mood, and energy. Genre would have the strongest weight, mood would also add points, and energy would help improve the ranking by preferring songs whose energy level is closer to the user's target. Once every song gets a total score, the system will sort the songs in descending order and recommend the highest-scoring songs first. Later, I can improve the recommender by adding smaller refinements such as tempo, valence, danceability, and acousticness.

---

## PHASE 2: Designing Scoring Logic

### Understanding the weight formula

Weights help us decide which features are more important for a user. For example, a user may care more about genre and less about energy, or more about mood than genre. However, it is important to keep the weights balanced because if we say that the right genre adds +100 points while mood adds only 5 points, then genre will dominate and overpower everything else. In that case, our recommender would mostly suggest songs from the same genre and ignore other features that may also be important to the user. That would not be an optimal solution.

Based on the previous Copilot suggestion, we can use the following weight formula:

**Total = genre points + mood points + weighted energy score**

Where:

- Genre match -> +3 points
- Mood match -> +2 points
- Energy score = 1 - abs(actual song energy - user preferred energy)

### PROMPT 5

Explain this scoring formula in simple words: genre match +3, mood match +2, and energy similarity based on 1 - |song_energy - user_energy|.

![Explanation](screenshots/img5.png)

For my first scoring formula, I decided to keep it simple:

- genre match = +3 points
- mood match = +2 points
- energy similarity = 1 - |song_energy - user_energy|

The final score is the sum of all three parts. This makes genre the strongest factor, mood the second strongest factor, and energy a smaller feature that helps refine the ranking.

If we wanted energy to have a bigger effect, we could multiply the energy score by an additional weight.

### Manually computing a song score

Song 1 example: "Happy" by Pharrell Williams

- genre = "pop" -> match -> +3 points
- mood = "happy" -> match -> +2 points
- energy = "high" (maybe 0.8) -> 1 - |0.8 - 0.8| = 1 - 0 = 1

**Total score = 3 + 2 + 1 = 6**

Song 2 example: "Frozen" by Madonna

- genre = "pop" -> match -> +3 points
- mood = "chill" -> no match -> 0 points
- energy = "mid" (maybe 0.4) -> 1 - |0.4 - 0.8| = 1 - 0.4 = 0.6

**Total score = 3 + 0 + 0.6 = 3.6**

### Predicting which song ranks first

The song "Happy" will rank higher because its total score is 6, which is higher than the 3.6 score of "Frozen."

### PROMPT 6: Spotting weight imbalance issues

Using songs.csv, I am using this scoring formula:

- genre match = +3
- mood match = +2
- energy similarity = 1 - |song_energy - user_energy|

Can you identify possible weight imbalance issues in this recommender and explain how they might affect which songs rank first? Please keep the explanation simple and beginner-friendly.

![Explanation](screenshots/img6.png)

=> The weights decide what the recommender cares about most. In our formula, genre matters the most, mood matters next, and energy only fine-tunes the ranking. That means songs with the right genre can sometimes rank too high, even if other parts of the match are weaker.

### PROMPT 7: Finalizing our scoring system

Let's finalize our "algorithm recipe" based on the following scoring system:

A common starting point is:

- +2.0 points for a genre match
- +1.0 point for a mood match
- similarity points based on how close the song's energy is to the user's target

![Explanation](screenshots/img7.png)

---

## PHASE 3: Implementation

### PROMPT 8: Implementing `load_songs()`

In recommender.py, implement `load_songs()` using Python's `csv.DictReader`.

Requirements:

- Read data from the `csv_path` argument
- Return a list of dictionaries
- Convert `id` to `int`
- Convert `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness` to `float`
- Keep `title`, `artist`, `genre`, and `mood` as strings
- Print "Loaded songs: X" where X is the number of loaded songs

Keep the code beginner-friendly and simple.

![Explanation](screenshots/img8.png)

![Explanation](screenshots/img9.png)

### PROMPT 10: Understanding the proposed `load_songs()` method

Using recommender.py, explain `load_songs()` line by line in simple words and explain why numeric conversion matters.

![Explanation](screenshots/img10.png)

### PROMPT 11: Implementing `score_song()`

In recommender.py, add a helper function called `score_song(user_prefs, song)`.

Use this scoring formula:

- genre match = +2.0
- mood match = +1.0
- energy similarity = 1 - abs(song["energy"] - user_prefs["energy"])

Requirements:

- Return both the numeric score and an explanation string
- The explanation should mention which parts matched, for example: "genre match (+2.0), mood match (+1.0), energy similarity (+0.98)"
- Keep the implementation simple and beginner-friendly

![Explanation](screenshots/img11.png)

![Explanation](screenshots/img12.png)

### PROMPT 12: Tracing `score_song()`

Using recommender.py, trace `score_song()` step by step for this user:

`{"genre": "pop", "mood": "happy", "energy": 0.8}`

Use Sunrise City from songs.csv as the song example.

![Explanation](screenshots/img13.png)

### PROMPT 13 and 14: Checking numeric conversions

Using recommender.py, what data types should each field have after `load_songs()` runs? Please list the expected type for `id`, `title`, `artist`, `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`, and explain why numeric conversion matters for `score_song()`.

![Explanation](screenshots/img14.png)

In `main.py`, temporarily add simple debug prints after `load_songs()` to show:

- the first loaded song
- `type(songs[0]["id"])`
- `type(songs[0]["energy"])`
- `type(songs[0]["tempo_bpm"])`

Keep it simple so I can verify numeric conversions.

![Explanation](screenshots/img15.png)

![Explanation](screenshots/img16.png)

I checked the numeric conversions after implementing `load_songs()`. This was important because CSV files load values as strings by default, but the recommender needs numeric values for scoring. I verified that `id` becomes an integer and that `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness` become floats. This helped me confirm that `score_song()` can correctly calculate energy similarity.

### PROMPT 15: Verifying sorting

Using recommender.py, explain how `recommend_songs()` sorts songs from highest score to lowest.

![Explanation](screenshots/img17.png)

I also verified how sorting should work before implementing `recommend_songs()`. Since each result is stored as `(song, score, explanation)`, the recommender needs to sort by the score value, which is index `1` in each tuple. Using `reverse=True` is important because recommendations should return the highest-scoring songs first, not the lowest-scoring songs.

### PROMPT 16: Implementing `recommend_songs()`

In recommender.py, implement `recommend_songs(user_prefs, songs, k=5)`.

Requirements:

- Loop through every song in `songs`
- Call `score_song(user_prefs, song)` for each song
- Store results in the format `(song_dict, score, explanation)`
- Sort the results from highest score to lowest score
- Return only the top `k` results
- Keep the code simple and beginner-friendly

![Explanation](screenshots/img18.png)

![Explanation](screenshots/img19.png)

### PROMPT 17: Understanding the implementation

Using recommender.py, explain how `recommend_songs()` works step by step after implementation.

![Explanation](screenshots/img20.png)

### Making sure the implementation works

Running `python -m src.main`

![Explanation](screenshots/img21.png)

Running tests by using `pytest`

![Explanation](screenshots/img22.png)

---

## PHASE 4: Evaluation & Bias

### PROMPT 18 and 19: Adding regular user profiles and edge cases

Using songs.csv, suggest 3 simple user profiles for evaluating my music recommender. I want profiles that are different enough to test different parts of the scoring logic, and I also want 1 edge-case or conflicting profile.

![Explanation](screenshots/img23.png)

Using songs.csv and my scoring logic in recommender.py, predict the expected top 3 results for each of these evaluation profiles:

1. `{"genre": "pop", "mood": "happy", "energy": 0.80}`
2. `{"genre": "lofi", "mood": "chill", "energy": 0.35}`
3. `{"genre": "rock", "mood": "intense", "energy": 0.92}`
4. `{"genre": "ambient", "mood": "intense", "energy": 0.95}`

Please explain briefly why each top result is expected.

![Explanation](screenshots/img24.png)

### Updating `main.py` to add our profiles

![Explanation](screenshots/img25.png)

### Checking if it works

![Explanation](screenshots/img26.png)

![Explanation](screenshots/img27.png)

### PROMPT 20: Explaining why a song ranked #1

Using recommender.py and songs.csv, explain why the #1 recommendation ranked first for the profile `{"genre": "pop", "mood": "happy", "energy": 0.80}`. Keep it simple and based on the scoring formula.

![Explanation](screenshots/img28.png)

### PROMPT 21: Running a small experiment

In recommender.py, temporarily modify `score_song()` for a Phase 4 experiment.

Change the scoring logic to:

- genre match = +1.0 instead of +2.0
- mood match = +1.0
- energy similarity should matter more by using:
  `2 * (1 - abs(song["energy"] - user_prefs["energy"]))`

Please clearly mark this as a temporary experiment so I can compare the rankings before and after.

![Explanation](screenshots/img30.png)

![Explanation](screenshots/img31.png)

### PROMPT 22: Identifying at least one bias/limitation

Using recommender.py and songs.csv, identify 2 biases or limitations revealed by these evaluation profiles. Please explain them in simple beginner-friendly language.

![Explanation](screenshots/img29.png)

### PROMPT 23: Interpreting unexpected results

Using recommender.py and songs.csv, help me interpret this unexpected result from my music recommender.

Profile:
`{"genre": "ambient", "mood": "intense", "energy": 0.95}`

Unexpected result:
`Spacewalk Thoughts ranked #1.`

Please explain what part of the scoring logic caused this result and what limitation or bias it reveals. Keep the explanation simple and beginner-friendly.

![Explanation](screenshots/img32.png)

---

## PHASE 5: Model Card

For this phase, I reviewed the required sections of the model card so I would understand what students are expected to include. I did not fully write out the entire model card, but I made sure I understood the purpose of each section, including intended use, data, strengths, limitations and bias, evaluation, future work, and personal reflection.

The main grading expectation seems to be clarity. Students should be able to explain their recommender in simple language, describe how it was tested, and reflect honestly on its limitations. My biggest takeaway is that even a simple weighted recommender can produce meaningful recommendations, but small choices in the scoring logic can strongly affect fairness, ranking quality, and the overall user experience.

I learned that recommendation systems do not need to be very complex to feel personalized. I was surprised by how much the weights affected the rankings, especially in edge cases. AI tools helped me move faster, but I still had to verify the logic and check whether the results actually made sense.
