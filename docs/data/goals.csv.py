"""import packages"""
import sys
import asyncio
import json
import codecs
import nest_asyncio
import pandas as pd
import aiohttp

from understat import Understat


async def main():
    """pull player data from understat"""
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        #player = await understat.get_player_grouped_stats(8418)
        #shots = await understat.get_player_shots(8418, {'season': "2022", \
        # 'player_assisted': 'Alphonso Davies'})
        shots = await understat.get_player_shots(8393, {'season': "2024"})
        #print(json.dumps(player))
        omar_string=json.dumps(shots, indent=4, ensure_ascii=False)
        ##print(shots)
        json.dump(shots, sys.stdout, indent=4, ensure_ascii=False)
        #pd.DataFrame.from_dict(player)
        with codecs.open("./omarshots.json", "w", "utf-8") as jsonfile:
            jsonfile.write(omar_string)
        jsonfile.close()

nest_asyncio.apply()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

df=pd.read_json('./omarshots.json')

df_result_grouped=df.groupby(['result']).count().sort_values(by=['id'], ascending=False)['id']
df_result_grouped.to_csv('./docs/result.csv', encoding='ascii')

df_assisted_grouped=df.groupby(['player_assisted']).count().sort_values(by=['id'],\
ascending=False)['id']
df_assisted_grouped.to_csv('./docs/assisted.csv')

df_type_grouped=df.groupby(['shotType']).count().sort_values(by=['id'], ascending=False)['id']
df_type_grouped.to_csv('./docs/type.csv', encoding='iso-8859-1')

df_situation_grouped=df.groupby(['situation']).count().sort_values(by=['id'], ascending=False)['id']
df_situation_grouped.to_csv('./docs/situation.csv', encoding='iso-8859-1')

df_action_grouped=df.groupby(['lastAction']).count().sort_values(by=['id'], ascending=False)['id']
df_action_grouped.to_csv('./docs/action.csv', encoding='iso-8859-1')

df_minute_grouped=df.groupby(['minute']).count().sort_index(ascending=True)['id']
df_minute_grouped.to_csv('./docs/minute.csv', encoding='iso-8859-1')
