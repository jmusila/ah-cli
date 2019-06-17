import sys
import requests
import click

from halo import Halo

spinner = Halo(text='Loading', spinner='dots', text_color='magenta')
url = "https://ah-django-staging.herokuapp.com/api"


@click.group()
def main():
    """
        Simple CLI for consuming Authors Haven App
    """
    pass


@main.command()
@click.argument("slug")
def get(slug):
    """
        This return a particular article from the given slug on Authors Haven API
    """
    spinner.start()
    url_format = url+"/{}/"
    spinner.stop()
    spinner.clear()
    click.echo(slug)

    response = requests.get(url_format.format(slug))

    click.echo(response.json())


@main.command()
@click.argument("limit")
def get_all_articles(limit):
    """
       This returns all the articles form Authors Haven API
    """
    spinner.start()
    url_format = url + "/articles/feed/"
    spinner.start
    spinner.clear
