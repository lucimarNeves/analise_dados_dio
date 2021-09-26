## analise_dados_dio dos trends do twitter

##coleta de dados

#bibliotecas
import tweepy as tw
import pandas as pd
import numpy as np
import re
from tweepy import Cursor

##token autenticação devem ser solicitadas ao twitter, mediante análise
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""

##autenticação
auth = tw.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

##validação, caso ocorra algum erro de autenticação
if(not api):
    print("Authenticcation failed!")
    sys.exit(-1)

##setando qual país quer verificar os dados
BRAZIL_WOE_ID = 23424768
woeid = BRAZIL_WOE_ID

##eliminando a hashtags
trends = api.trends_place(id = woeid, exclude = "hashtags")

##printando um cabeçalho
print("As principais tendências para o local são :")

##for para percorrer os campos verificando as tendências
for value in trends:
    for trend in value['trends']:
        print(trend['name'])
        
##Escolhendo um assunto específico para amostragem de dados
searchString = ['alcool', 'gasolina']

##utilizando a biblioteca Cursor do Tweepy
tweets = tw.Cursor(api.search, q = searchString,lang='pt', since='2021-09-24', tweet_mode='extended').items(100)
all_tweets = [tweet.full_text for tweet in tweets]

##criando o dataframe
df = pd.DataFrame(all_tweets, columns=["Tweets" ])

##exibindo o dataframe,  pode usar .head() para exibir poucos itens
df

##salvando os dados do dataframe em um arquivo .csv
df.to_csv("tweets.csv")












