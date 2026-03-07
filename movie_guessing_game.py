import random

def play_game():
    # Movie list inside the Python file
    movies = [
        "Titanic","Inception","Avatar","The Godfather","The Dark Knight","Pulp Fiction",
        "Forrest Gump","Interstellar","The Matrix","Goodfellas","Schindler's List",
        "Fight Club","The Shawshank Redemption","The Silence of the Lambs","The Green Mile",
        "Gladiator","Django Unchained","The Departed","The Wolf of Wall Street",
        "The Social Network","Catch Me If You Can","Braveheart","Slumdog Millionaire",
        "The Truman Show","The Pursuit of Happyness","La La Land","Whiplash","Parasite",
        "Joker","A Beautiful Mind","The Grand Budapest Hotel","Black Swan","Her",
        "Life of Pi","The Pianist","The King's Speech","A Star Is Born","Birdman",
        "Spotlight","Argo","Crash","12 Years a Slave","Moonlight","The Shape of Water",
        "Boyhood","The Big Short","The Blind Side","Se7en","The Usual Suspects",
        "Gone Girl","Prisoners","Mystic River","The Sixth Sense","Fargo","Heat",
        "American History X","No Country for Old Men","The Revenant","Unforgiven",
        "Taxi Driver","Requiem for a Dream","Lost in Translation",
        "Eternal Sunshine of the Spotless Mind","The Notebook","The Help",
        "The Theory of Everything","The Imitation Game",
        "The Curious Case of Benjamin Button","The Aviator","Gran Torino",
        "The Breakfast Club","Good Will Hunting","Dead Poets Society",
        "Cast Away","The Terminal","Hidden Figures","A Quiet Place",
        "The Greatest Showman","The Proposal","Crazy Rich Asians",
        "Knives Out","The Da Vinci Code","300","The Last Samurai",
        "The Book Thief","Lucy","The Fighter","Creed","The Equalizer",
        "The Conjuring","Memento","The Babadook","The Prestige",
        "The Big Lebowski","Oldboy","American Beauty","Room","Shutter Island"
    ]

    name = input("What is your name? ")
    print("Good luck!", name)

    movie = random.choice(movies).lower()
    print("Guess the Movie")

    guesses = ""
    turns = 5

    while turns > 0:
        failed = 0

        for char in movie:
            if char in guesses or char == " ":
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1

        print()

        if failed == 0:
            print("You Win!")
            print("The movie is:", movie)
            break

        guess = input("Guess a character: ").lower()
        guesses += guess

        if guess not in movie:
            turns -= 1
            print("Wrong guess!")
            print("You have", turns, "more guesses.")

        if turns == 0:
            print("You Lose! The movie was:", movie)

while True:
    play_game()
    retry = input("Do you want to play again? (y/n): ").lower()
    if retry != 'y':
        print("Thank you for playing!")
        break