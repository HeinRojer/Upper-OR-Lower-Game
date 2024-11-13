

import random


Data = {
    # Celebrities
    "Cristiano Ronaldo, a footballer from Portugal": 20000000,
    "Lionel Messi, a footballer from Argentina": 18000000,
    "Selena Gomez, a singer and actress from the USA": 6000000,
    "Dwayne Johnson, an actor and wrestler from the USA": 8000000,
    "Kylie Jenner, a media personality from the USA": 7000000,
    "Ariana Grande, a singer and actress from the USA": 5000000,
    "Kim Kardashian, a media personality from the USA": 6000000,
    "Beyoncé, a singer and actress from the USA": 4000000,
    "Justin Bieber, a singer from Canada": 5000000,
    "Taylor Swift, a singer and songwriter from the USA": 10000000,
    "Shah Rukh Khan, an actor from India": 3000000,
    "Billie Eilish, a singer from the USA": 4500000,
    "Zendaya, an actress and singer from the USA": 3500000,
    "Drake, a rapper and singer from Canada": 3800000,
    "Tom Holland, an actor from the UK": 4200000,
    "Chris Hemsworth, an actor from Australia": 3000000,
    "Jennifer Lopez, an actress and singer from the USA": 3800000,
    "Rihanna, a singer and businesswoman from Barbados": 4700000,
    "Keanu Reeves, an actor from Canada": 3500000,
    "Kanye West, a rapper and fashion designer from the USA": 5000000,

    # Sports Clubs
    "Real Madrid, a football club from Spain": 7000000,
    "Barcelona, a football club from Spain": 6000000,
    "Manchester United, a football club from England": 5000000,
    "Paris Saint-Germain, a football club from France": 4000000,
    "Juventus, a football club from Italy": 2000000,
    "Liverpool, a football club from England": 3000000,
    "Chelsea, a football club from England": 2000000,
    "Bayern Munich, a football club from Germany": 2000000,
    "Manchester City, a football club from England": 3000000,
    "Arsenal, a football club from England": 2000000,
    "Inter Milan, a football club from Italy": 1500000,
    "AC Milan, a football club from Italy": 1700000,
    "Tottenham Hotspur, a football club from England": 1200000,
    "Atletico Madrid, a football club from Spain": 1300000,
    "Borussia Dortmund, a football club from Germany": 1200000,
    "Napoli, a football club from Italy": 900000,
    "Ajax, a football club from the Netherlands": 800000,
    "AS Roma, a football club from Italy": 700000,
    "Newcastle United, a football club from England": 650000,
    "Galatasaray, a football club from Turkey": 500000,

    # Movies
    "Avatar, a movie directed by James Cameron": 1500000,
    "Avengers: Endgame, a Marvel movie": 1200000,
    "The Lion King, a Disney animated movie": 800000,
    "Frozen, a Disney animated movie": 600000,
    "The Batman, a superhero movie from DC": 1000000,
    "Spider-Man: No Way Home, a Marvel movie": 1800000,
    "Black Panther: Wakanda Forever, a Marvel movie": 1200000,
    "Toy Story, a Pixar animated movie": 500000,
    "Fast & Furious, a movie franchise": 1500000,
    "Harry Potter (Wizarding World), a movie franchise": 2000000,
    "The Super Mario Bros. Movie, an animated movie": 1100000,
    "Oppenheimer, a historical drama movie": 1300000,
    "Barbie, a live-action movie": 1400000,
    "The Matrix, a science fiction movie": 800000,
    "Titanic, a movie directed by James Cameron": 1200000,
    "Jurassic Park, a science fiction movie": 900000,
    "Inception, a science fiction thriller movie": 1000000,
    "Star Wars, a movie franchise": 1800000,
    "The Godfather, a crime drama movie": 600000,
    "The Dark Knight, a superhero movie from DC": 1000000
}

score = 0

AAA = True
while AAA == True :
    option_A = random.choice ( list ( Data.keys ( ) ) )
    option_B = random.choice ( list ( Data.keys ( ) ) )
    print()
    print(f"Score: {score}")
    print ( "Who has the highest average monthly searches" )
    print()
    print(f"Option A :  {option_A}")
    print("""
    
    ██╗   ██╗███████╗
    ██║   ██║██╔════╝
    ██║   ██║███████╗
    ██║   ██║╚════██║
    ╚██████╔╝███████║
    ╚═════╝ ╚══════╝╚

    """)
    print(f"Option B :  {option_B}")
    answer = ""
    if Data[option_A] > Data[option_B]:
        answer = "A"
    else:
        answer ="B"
    user_input = input("Enter Your Answer  : ").upper()
    if user_input == answer:
        print("You've got the right option")
        score +=1
    else:
        print("Sorry You've got the wrong answer")
        print(f"YOUR SCORE : {score} ")
        continue_user = input("Do you wanna give it an another try .\n 1. yes   2. no   ")
        if continue_user == "no":
            AAA = False
            print()
            print("Thank you for playing")