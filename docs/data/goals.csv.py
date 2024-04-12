import asyncio
import json
import nest_asyncio
import codecs
import pandas as pd
import sys
import aiohttp

from understat import Understat


async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        #player = await understat.get_player_grouped_stats(8418)
        #shots = await understat.get_player_shots(8418, {'season': "2022", 'player_assisted': 'Alphonso Davies'})
        shots = await understat.get_player_shots(8418, {'season': "2023"})
        #print(json.dumps(player))
        jamal_string=json.dumps(shots, indent=4, ensure_ascii=False)
        ##print(shots)
        json.dump(shots, sys.stdout, indent=4, ensure_ascii=False)
        #pd.DataFrame.from_dict(player)
        with codecs.open("./jamalshots.json", "w", "utf-8") as jsonfile:
            jsonfile.write(jamal_string)
        jsonfile.close()
        
    
nest_asyncio.apply()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

df=pd.read_json('./jamalshots.json')

df_result_grouped=df.groupby(['result']).count().sort_values(by=['id'], ascending=False)['id']
df_result_grouped.to_csv('result.csv', encoding='iso-8859-1')

df_assisted_grouped=df.groupby(['player_assisted']).count().sort_values(by=['id'], ascending=False)['id']
df_assisted_grouped.to_csv('assisted.csv', encoding='iso-8859-1')

df_type_grouped=df.groupby(['shotType']).count().sort_values(by=['id'], ascending=False)['id']
df_type_grouped.to_csv('type.csv', encoding='iso-8859-1')

df_situation_grouped=df.groupby(['situation']).count().sort_values(by=['id'], ascending=False)['id']
df_situation_grouped.to_csv('situation.csv', encoding='iso-8859-1')

df_action_grouped=df.groupby(['lastAction']).count().sort_values(by=['id'], ascending=False)['id']
df_action_grouped.to_csv('action.csv', encoding='iso-8859-1')

df_minute_grouped=df.groupby(['minute']).count().sort_index(ascending=True)['id']
df_minute_grouped.to_csv('minute.csv', encoding='iso-8859-1')