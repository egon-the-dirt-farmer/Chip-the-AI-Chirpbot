### Technical Documentation
# Chip - AI ChirpBot
## Introduction
Chip is a twitterBot app that works in conjunction with the OpenAI GPT API, and has been developed by Franklin Media Australia Pty Ltd. It utilises 
the OpenAI API to generate responses to prompts supplied to the completions endpoint. The user can enter their name so that it will appear in the 
chatbox with the user responses on the right of the chatbox and the bot responses on the left side of the chatbox. The app is designed as a 
desktop chatbot to interface with the OpenAI narrow Artificial Intelligence API.

## Requirements
In order to use Chip, you will need the following:

* API Key from OpenAI
* Python 3.x installed on your system
* Required Python libraries: openai, tweepy, time, random, configparser

## How it Works
Chip has four primary files, the api_key file that simply requires an OpenAI API Key pasted into it and nothing else. The tw_config file that reads
the api_key file to import the api key. It has a prompts file with a list of prompts that are fed randomly into the OpenAI completions endpoint to
generate the desired tweet. It then has the primary app.py file that runs the code to run the Twitter bot.

## The app has the following main functions:
* read_api_key() - reads the api key for OpenAI the config.ini file.
* gpt3_completion() - submits the prompt to the OpenAI gompletions endpoint.
* send_tweeet() - sends an update status command to the Twitter API using the Tweepy library.
* tweet_loop() - creates a function that calls the send_tweet() function and returns the gpt3_completion()
* mainloop() - sets the mainloop to call all functions and run the twitter bot when called.


## Technical Details
* The app uses OpenAI's completion API to generate Tweets based on submitted prompts. 
* The app uses the text-davinci-003 engine to generate the text response from the API.
* The app sets the maximum tokens to 150 and temperature to 0.9 for the completion API.
* The app sets the n parameter to 1 for the completion API.
* The app sets the top_p parameter to 1, the frequency penalty to 0 and the presence_penalty to 0.6

## License
Chip is privately licensed by Franklin Media Australia Pty Ltd for non-commercial use only. You may use the software for personal or internal business 
purposes, but you may not distribute, sell, or use it for any commercial purpose without the express written permission of Franklin Media Australia 
Pty Ltd. By using Chip, you agree to be bound by the terms of the Franklin Media Australia Pty Ltd - Private Use Copyright License. 

Please note that this software is provided "as is" without warranty of any kind, express or implied. Franklin Media Australia Pty Ltd shall not be 
liable for any damages arising from the use of this software. If you have any questions or concerns about the license for Chip, please comment to the 
Franklin Media Australia programmers through their GitHub Repository.
