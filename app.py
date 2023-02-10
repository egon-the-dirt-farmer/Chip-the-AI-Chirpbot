# ====================================================================================================================
# /*
# APP NAME: Chip the AI Chirp Bot - Tweet Bot
# APP URI: https://franklinmedia.com.au/apps/chip-ai-chirp-bot/
# AUTHOR: Z3r0-K3lv1n
# AUTHOR URI: https://franklinmedia.com.au/z3r0-k3lv1n
# DESCRIPTION: Meet Chip, the AI Chirp Bot! Chip is a Twitter bot that uses artificial intelligence to send out tweets
# at regular intervals. With Chip, you can keep your followers engaged with unique and interesting content, all while
# taking a hands-off approach to tweeting.
# Using the OpenAI, tweepy, time, and prompts libraries, Chip is able to generate tweets based on prompts provided by
# the OpenAI library. This means that you can set Chip up with a list of prompts, and it will create tweets based on
# those prompts using artificial intelligence.
# Chip also comes with a separate config file to store sensitive information such as API keys, making it easy to set
# up and use.
# With Chip, you can keep your Twitter account active and engaging, even when you don't have the time to manually
# tweet. Give Chip a try and see how it can benefit your social media presence!
# TAGS: Twitter bot, Artificial intelligence, Python, OpenAI, tweepy, Configuration, API keys, Social media,
# Tweet generation, Interval tweeting
# Version: 1.1
# LICENSE: Franklin Media Australia Pty Ltd - Private Use Copyright License
# LICENSE URI:https://www.franklinmedia.com.au/impressum-credits/website-terms-conditions/private-use-copyright-license/
# COPYRIGHT LICENSE FOR PRIVATE USE ONLY
# Chip the AI Chirp Bot - AI Twitter Bot is privately licensed by Franklin Media Australia Pty Ltd for
# non-commercial use only. This means that you may use the software for personal or internal business purposes, but
# you may not distribute, sell, or use it for any commercial purpose without the express written permission of
# Franklin Media Australia Pty Ltd.
# By using Chip the AI Chirp Bot - AI Twitter Bot, you agree to be bound by the terms of the Franklin
# Media Australia Pty Ltd - Private Use Copyright License. The full text of this license can be found here.
# Please note that this software is provided "as is" without warranty of any kind, express or implied. Franklin Media
# Australia Pty Ltd shall not be liable for any damages arising from the use of this software.
# If you have any questions or concerns about the license for The Basic Universal Translator - The Cunning Linguist,
# please contact Franklin Media Australia Pty Ltd at admin@franklinmedia.com.au.
# */
# ====================================================================================================================

#  Import required python libraries
import configparser
import time
import openai
import tweepy
import random

# Import required internal modules
import prompts
import tw_config

# ---------------------------------------------------------------------
# Twitter Authentication Variables
consumer_key = tw_config.api_key
consumer_secret = tw_config.api_secret
access_token = tw_config.access_token
access_token_secret = tw_config.access_token_secret
# ---------------------------------------------------------------------

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(consumer_key=consumer_key, consumer_secret=consumer_secret,
                     access_token=access_token, access_token_secret=access_token_secret)
api = tweepy.API(auth)

index = 0
prev_index = None


# Read the Openai API Key from the config file
def read_api_key(file_path):
    # Read the Config file
    config = configparser.ConfigParser()
    config.read(file_path)

    # Read the API key from the text file
    with open(config['openai']['api_key'], 'r') as key:
        api_key = key.read()

    return api_key


# Set the API key for OpenAI using the configuration file
openai.api_key = read_api_key('config.ini')


def gpt3_completion():
    # The country variable will call the variable countries from the prompts module. This is a list of countries
    # that the index variable initially set at 0 will cycle through the entire list one ofter the other as the index
    # variable is incremented by one with each run of the mainloop()
    # country = prompts.countries[index]
    # Ask GPT-3 a question
    prompt = f"{prompts.ai_personality}{prompts.prompt_options[index]} {prompts.content_hashtag} {prompts.char_count}"
    # prompt_celebrate = f"{prompts.ai_personality} Offer a traditional new year greeting to the people in {country} in the official " \
    #          f"languages of {country} and do not mention any dates in the response. {prompts.char_count}"
    model = "text-davinci-003"
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    answer = response.get('choices')[0].get('text')
    tweet = f"{answer}\n{prompts.hashtags}"
    return tweet


# USE Tweepy Library to send a Tweet
def send_tweet():
    api.update_status(gpt3_completion())


def tweet_loop():
    # Send the tweet
    send_tweet()
    return gpt3_completion()


def mainloop():
    global prev_index  # make the prev_index variable global so it can be accessed and modified inside the function
    tweet_delay = 600
    try:
        # Generate a random index
        prompt_index = random.randint(0, len(prompts.prompt_options) - 1)
        # If the random index is the same as the previous index, keep generating new indices until a new one is chosen
        while prompt_index == prev_index:
            prompt_index = random.randint(0, len(prompts.prompt_options) - 1)
        # Update the previous index variable
        prev_index = prompt_index
        tweet_loop()
        # Print out the tweet in the terminal
        print(tweet_loop())
    except Exception as e:
        print(f'Error: {e}')
    finally:
        time.sleep(tweet_delay)  # 3600 = 1 hour. This means it will tweet every 60 minutes



if __name__ == '__main__':
    while index <= len(prompts.prompt_options):
        mainloop()  # Run the mainloop()
        index += 1  # Increment the index variable by the integer after the = sign
        if index > len(prompts.prompt_options):  # If the index is greater than the length of the prompt_options list
            index = 0 # Reset the index to 0


