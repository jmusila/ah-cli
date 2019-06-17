import sys
import requests

from halo import Halo

spinner = Halo(text='Loading', spinner='dots', text_color='magenta')
url = "https://ah-django-staging.herokuapp.com/api"

