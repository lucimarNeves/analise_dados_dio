## Análise_dados_dio dos trends do twitter

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


##
#Análise de sentimentos

##bibliotecas utilizadas
import tweepy as tw
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from textblob import TextBlob
from tweepy import Cursor

##token de acesso fornecido pelo twitter
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""

##autenticação
auth = tw.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

##validação caso ocorra algum problema
if(not api):
    print("Authenticcation failed!")
    sys.exit(-1)
    
##especificando o país para coleta de dados
BRAZIL_WOE_ID = 23424768
woeid = BRAZIL_WOE_ID

##removendo hashtags
trends = api.trends_place(id = woeid, exclude = "hashtags")

##escolhendo assunto específico para amostragem de dados
searchString = ['alcool', 'gasolina']

##usando a biblioteca Cursor do tweepy
tweets = tw.Cursor(api.search, q = searchString,lang='pt', since='2021-09-24', tweet_mode='extended').items(100)
all_tweets = [tweet.full_text for tweet in tweets]

##criando dataframe
dados = pd.DataFrame(all_tweets, columns=["Tweets" ])

##exibindo dados
dados.head()

##excluindo dados duplicados
dados.drop_duplicates(inplace = True)

##normalizando 
dados['Tweets'].value_counts(normalize = True)

##Analise de sentimentos dados recentes na home_timeline, especificando a quantidade itens e a home_timeline
 tweets = api.home_timeline(count=200)

##classe de configuração da análise de sentimentos

class TweetAnalyzer():
    
    def clean_tweet(self, tweet):
          return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))

        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1

    def tweets_to_data_frame(self, tweets):
        
        dados = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])

        
        dados['len'] = np.array([len(tweet.text) for tweet in tweets])
        dados['date'] = np.array([tweet.created_at for tweet in tweets])
        dados['source'] = np.array([tweet.source for tweet in tweets])
        dados['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        dados['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        dados['sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in dados['tweets']])
        
        return dados

        tweet_analyzer = TweetAnalyzer()
 
 ##criando dataframe da análise de sentimentos
 dados = tweet_analyzer.tweets_to_data_frame(tweets)
 
 #Análise de sentimentos

# 0 - sentimento negativo
# 1 - sentimento positivo
# -1 - sentimento neutro


#exibindo os dados 
dados.head()

#bibliotecas para plotagem de gráficos
import seaborn as sns
import matplotlib as plt

#plotando gráfico de barras
sns.set()
ax = dados['sentiment'].value_counts().plot.bar()
ax.set_ylabel('Quantidade')
ax.set_xlabel('Sentiment')

#imprimindo de forma detalhada a análise
dados = tweet_analyzer.tweets_to_data_frame(tweets)
dados['sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in dados['tweets']])
print(dados.head(10))

#gráfico de retweets 
sns.set()
ax = dados['retweets'].value_counts().plot.bar()
ax.set_title('Total de retweets ')
ax.set_ylabel('Quantidade')
ax.set_xlabel('Retweets')

#gráfico likes com data
sns.set()
time_likes = pd.Series(data=dados['len'].values, index=dados['date'])
time_likes.plot(figsize=(16, 4), color='b')

#gráfico retweets com data
time_retweets = pd.Series(data=dados['retweets'].values, index=dados['date'])
time_retweets.plot(figsize=(16, 4), color='b')

#configuração da data base

import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client.get_database('dados_tweets')

collection = db_get_collection('tweets')









