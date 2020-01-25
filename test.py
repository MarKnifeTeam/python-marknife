from dotenv import load_dotenv
from marknife import Marknife
import os

load_dotenv()

m = Marknife(os.getenv("APIUSER"), os.getenv("APIKEY"))

print(m.SayHello())

def cb(err=None, data=None):
    if err:
        return print(err)
    print(data)

r = m.Me(cb)
