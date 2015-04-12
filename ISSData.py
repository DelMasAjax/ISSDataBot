from TwitterAPI import TwitterAPI
import tokens

api = TwitterAPI(tokens.consumer_key, tokens.consumer_secret, tokens.access_token_key, tokens.access_token_secret)

r = api.request('statuses/update', {'status':'Hello, World!'})
print r.status_code
