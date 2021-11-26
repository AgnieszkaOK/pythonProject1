import unittest

import pytest

from twitter import Twitter

'''
class TwitterTest(unittest.TestCase):
    def setUp(self):
        self.twitter=Twitter()

    def test_initialization(self):
        self.assertTrue(self.twitter)

    def test_tweet_single(self):
        # When
        self.twitter.tweet('Test message')
        #then
        self.assertEqual(self.twitter.tweets, ['Test message'])

if __name__=='__main__':
    unittest.main()
'''
@pytest.fixture
def twitter():
    twitter = Twitter()
    return twitter

def test_twitter_initialization(twitter):
    assert twitter

def test_tweet_single_message(twitter):
    twitter.tweet('Test message')
    assert twitter.tweets == ['Test message']

def test_tweet_long_message(twitter):
    with pytest.raises(Exception):
        twitter.tweet('test'*41)
    assert twitter.tweets == []


@pytest.mark.parametrize("message, expected", (
        ("test #first message", ["first"]),
        ("#first test message", ["first"]),
        ("#FIRST test message", ["first"]),
        (" test message #first", ["first"]),
        ("#first #second test message", ["first", "second"]),

))
def test_tweet_with_hashtag(message, expected):
    twitter = Twitter()
    assert twitter.find_hashtags(message) == expected



'''def test_tweet_with_hashtag():
    twitter = Twitter()
    message = "test #first message"
    twitter.tweet(message)
    assert 'first' in twitter.find_hashtags(message)

def test_tweet_with_hashtag_on_begining():
    twitter = Twitter()
    message = "#first test message"
    twitter.tweet(message)
    assert 'first' in twitter.find_hashtags(message)

def test_tweet_with_hashtag_on_begining_uppercase():
    twitter = Twitter()
    message = "#FIRST test message"
    twitter.tweet(message)
    assert 'FIRST' in twitter.find_hashtags(message)
'''

