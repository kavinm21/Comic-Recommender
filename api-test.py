import os
from dotenv import load_dotenv

load_dotenv()

public_key = os.getenv('PUBLIC_KEY')
private_key = os.getenv('PRIVATE_KEY')

from marvel import Marvel

m = Marvel(public_key, private_key)

comics = m.comics

data = comics.all(titleStartsWith='Daredevil',dateRange="2020-01-01,2021-01-01", limit="25")

df = data['data']['results']
print(data['data']['count'])
print(df[0])