from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-30ceaf2b-2afa-4b4e-8ef5-e3b668b7236a')
my_region = 'na1'

me = lol_watcher.summoner.by_name(my_region, 'blxst')
# print(me)

my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)

versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']

try:
    response = lol_watcher.summoner.by_name(my_region, 'blxst')
except ApiError as err:
    if err.response.status_code == 429:
        print('future requests wait until the retry-after time passes')
    elif err.response.status_code == 404:
        print('name not found.')
    else:
        raise