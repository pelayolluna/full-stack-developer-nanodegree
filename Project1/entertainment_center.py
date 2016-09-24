import fresh_tomatoes
import media

# Movie local variables
storyline = '''A nameless disillusioned young urban male (Edward Norton) fights
insomnia by attending disease support groups until he meets a
kindred spirit -and soap salesman (Brad Pitt). Together they form
Fight Club, where young men can exert their frustrations and angst
upon one another.'''
image = "https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Fight_Club_poster.jpg/220px-Fight_Club_poster.jpg"# noqa
trailer = "https://www.youtube.com/watch?v=SUXWAEX2jlg"

# Object instance
fight_club = media.Movie("Fight Club", storyline, image, trailer)

# Movie local variables
storyline = '''Director Bryan Singer's labyrinthine crime drama centers
on five career criminals who meet after being rounded up for a
standard police line-up. Upon their release, the men band together to
pull off an intricate heist involving 3 million dollars worth of
emeralds. Their success brings them to the attention of the enigmatic
Keyser Soze, an unseen, nefarious, and mythic underworld crime figure
who coerces them into pulling off an important and highly dangerous
job. The scenes that follow make 'The Usual Suspects' one of the most
fascinating crime thrillers in cinema history.'''
image = "https://upload.wikimedia.org/wikipedia/en/thumb/9/9c/Usual_suspects_ver1.jpg/220px-Usual_suspects_ver1.jpg"# noqa
trailer = "https://www.youtube.com/watch?v=oiXdPolca5w"

# Object instance
usual_suspects = media.Movie("The Usual Suspects", storyline, image, trailer)

# Movie local variables
storyline = '''A nameless disillusioned young urban male (Edward Norton)
fights insomnia by attending disease support groups until he meets a
kindred spirit -and soap salesman (Brad Pitt). Together they form Fight
Club, where young men can exert their frustrations and angst upon one
another.'''
<<<<<<< HEAD
image = '''https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Inception_%282010%29_theatrical_poster.jpg/220px-Inception_%28201029_theatrical_poster.jpg'''
=======
image = "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Inception_%282010%29_theatrical_poster.jpg/220px-Inception_%282010%29_theatrical_poster.jpg"# noqa
>>>>>>> 0985fe4861ce81f1124ee156de88e23397afb0fa
trailer = "https://www.youtube.com/watch?v=YoHD9XEInc0"

# Object instance
inception = media.Movie("Inception", storyline, image, trailer)

# Movie local variables
storyline = '''Caleb, a 24 year old coder at the world's largest internet
company, wins a competition to spend a week at a private mountain
retreat belonging to Nathan, the reclusive CEO of the company. But when
Caleb arrives at the remote location he finds that he will have to
participate in a strange and fascinating experiment in which he must
interact with Ava, the world's first true artificial intelligence,
housed in the body of a beautiful robot girl.'''
image = "https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Ex-machina-uk-poster.jpg/220px-Ex-machina-uk-poster.jpg"# noqa
trailer = "https://www.youtube.com/watch?v=gyKqHOgMi4g"

# Object instance
ex_machina = media.Movie("Ex Machina", storyline, image, trailer)

# Movie local variables
storyline = '''Maximus (Crowe) is a brave and loyal military general to
the Emperor Marcus Aurelius (Harris). His loyalty does not go
unnoticed as the Emperor makes preparations for Maximus to succeed
him after his death. But when the Emperor's son, Commodus (Phoenix)
finds out, he kills his father and orders the death of Maximus. While
he escapes, his wife and son are brutally murdered. He then ends up a
slave in North Africa and is sold to become a gladiator. Trained by
Proximo (Reed), a former gladiator himself, Maximus wins every battle
and soon finds himself sent to Rome to take part in the Gladitorial
Games. It is here that he plans to plot his vengeance and gain his
freedom. While all this is going on, his past lover, the Emperor's
daughter (Nielsen) works to restore democratic rule with the help
of a civil-minded senator (Jacobi).'''
image = "https://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Gladiator_ver1.jpg/220px-Gladiator_ver1.jpg"# noqa
trailer = "https://www.youtube.com/watch?v=0BLZbrLogTo"

# Object instance
gladiator = media.Movie("Gladiator", storyline, image, trailer)

# Movie's array
movies = [fight_club, usual_suspects, inception, ex_machina, gladiator]

# Open web interface
fresh_tomatoes.open_movies_page(movies)

