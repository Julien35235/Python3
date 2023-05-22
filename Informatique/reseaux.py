import tweepy

# Authentification auprès de l'API Twitter
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)

# Récupérer le nombre d'abonnés d'un utilisateur spécifié
user = "example_user"
api = tweepy.API(auth)
followers_count = api.get_user(user).followers_count

print("Le nombre d'abonnés de", user, "sur Twitter est de", followers_count)
