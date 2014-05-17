__author__ = 'clev'

import os

def populate():
    club_feedone = add_feed(name='clubfeed1', genre='house', artist='djgoody', artist_flattr_account='http://www.poop.com')
    add_podcast(episode_number=22)
    club_feedtwo = add_feed(name='clubfeed2', genre='tech house', artist='djgy', artist_flattr_account='http://www.powwop.com')
    add_podcast(episode_number=44)
    add_podcast(episode_number=46)

def add_podcast(episode_number):
    p = podcast.objects.get_or_create(episode_number=episode_number)
    return p

def add_feed(name, genre, artist, artist_flattr_account):
    f = feed.objects.get_or_create(name=name, genre=genre, artist=artist, artist_flattr_account=artist_flattr_account)
    return f

if __name__ == '__main__':
    print "starting population script"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newstart.settings')
    from southtut.models import feed, podcast
    populate()