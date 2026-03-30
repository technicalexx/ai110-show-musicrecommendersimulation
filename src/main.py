"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

# from recommender import load_songs, recommend_songs
from src.recommender import load_songs, recommend_songs


def print_recommendations(profile_name, user_prefs, songs, k=5):
    print(f"\n=== {profile_name} ===")
    print(f"User preferences: {user_prefs}\n")

    recommendations = recommend_songs(user_prefs, songs, k=k)

    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{i}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv") 

    profiles = {
        "Pop + Happy + High-ish energy": {"genre": "pop", "mood": "happy", "energy": 0.80},
        "Lofi + Chill + Low energy": {"genre": "lofi", "mood": "chill", "energy": 0.35},
        "Rock + Intense + Very high energy": {"genre": "rock", "mood": "intense", "energy": 0.92},
        "Edge-case conflicting profile": {"genre": "ambient", "mood": "intense", "energy": 0.95},
    }

    for profile_name, user_prefs in profiles.items():
        print_recommendations(profile_name, user_prefs, songs)

    # # Debug: verify numeric conversions
    # print("\nDebug Info:")
    # print(f"First song: {songs[0]}")
    # print(f"Type of id: {type(songs[0]['id'])}")
    # print(f"Type of energy: {type(songs[0]['energy'])}")
    # print(f"Type of tempo_bpm: {type(songs[0]['tempo_bpm'])}")
    # print()

    # # Starter example profile
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    # recommendations = recommend_songs(user_prefs, songs, k=5)

    # print("\nTop recommendations:\n")
    # for rec in recommendations:
    #     # You decide the structure of each returned item.
    #     # A common pattern is: (song, score, explanation)
    #     song, score, explanation = rec
    #     print(f"{song['title']} - Score: {score:.2f}")
    #     print(f"Because: {explanation}")
    #     print()


if __name__ == "__main__":
    main()
