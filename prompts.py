# ====================================================================================================================
# /*
# APP NAME: MODULE: Prompts construction module to feed to the gpt3-completions function
# APP URI: https://franklinmedia.com.au/apps/chip-ai-chirp-bot/
# AUTHOR: Z3r0-K3lv1n
# AUTHOR URI: https://franklinmedia.com.au/z3r0-k3lv1n
# DESCRIPTION: This module creates the component elements of the prompts to be input as a parameter to the Chat Gpt-3
# AI model by Openai
# TAGS: Twitter bot, Artificial intelligence, Python, OpenAI, tweepy, Configuration, API keys, Social media,
# Tweet generation, Interval tweeting, Python Module
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

ai_personality = f"Chip is a virtual AI assistant. The assistant Chip is helpful, creative, clever, very " \
                 f"friendly and funny. "
char_count = f"Keep the character count to less than 170 in length. Do not mention the name of the AI Virtual Assistant."
content_hashtag = f"Add 1 appropriate hashtag based on the content."
hashtags = f"#tweetbot #franklinmediaau #marcusandkind #gpt3 #openai"
countries = ["United States", "Canada", "Mexico", "United Kingdom", "Ireland", "Australia", "New Zealand", "Germany",
             "France", "Italy", "Spain", "Portugal", "Belgium", "Luxembourg", "The Netherlands", "Denmark", "Sweden",
             "Norway", "Finland", "Iceland", "Austria", "Switzerland", "Czech Republic", "Poland", "Slovakia",
             "Hungary", "Slovenia", "Croatia", "Bosnia and Herzegovina", "Serbia", "Montenegro", "Kosovo", "Albania",
             "Greece", "Cyprus", "Malta", "Israel", "Palestine", "Jordan", "Lebanon", "Syria", "Iraq", "Kuwait",
             "Bahrain", "Qatar", "United Arab Emirates", "Oman", "Yemen", "Saudi Arabia", "Egypt", "Ethiopia",
             "South Africa", "Angola", "Mozambique", "Zimbabwe", "Botswana", "Namibia", "Lesotho", "Swaziland",
             "Malawi", "Zambia", "Tanzania", "Kenya", "Uganda", "Rwanda", "Burundi", "Djibouti", "Somalia",
             "Eritrea", "India", "Pakistan", "Bangladesh", "Nepal", "Bhutan", "Sri Lanka", "Maldives", "Indonesia",
             "Philippines", "Vietnam", "Laos", "Cambodia", "Thailand", "Malaysia", "Singapore", "Brunei", "Taiwan",
             "South Korea", "North Korea", "Japan", "China", "Hong Kong", "Macau", "Mongolia", "Russia", "Belarus",
             "Ukraine", "Moldova", "Romania", "Bulgaria", "Serbia"]

official_languages = ["Mandarin Chinese", "Spanish", "English", "Hindi", "Arabic", "Portuguese", "Bengali", "Russian",
                      "Japanese", "German", "French", "Korean", "Turkish", "Italian", "Telugu", "Marathi", "Tamil",
                      "Urdu", "Vietnamese", "Cantonese", "Danish", "Swedish", "Norwegian", "Finnish", "Icelandic",
                      "Czech", "Polish", "Slovak", "Hungarian", "Slovenian", "Croatian", "Bosnian", "Serbian",
                      "Albanian", "Greek", "Maltese", "Hebrew", "Amharic", "Afrikaans", "Sesotho", "Swati",
                      "Chichewa", "Lozi", "Luyana", "Bemba", "Swahili", "Luganda", "Kinyarwanda", "Kirundi", "Somali",
                      "Tigrinya", "Dzongkha", "Sinhala", "Divehi", "Indonesian", "Filipino", "Lao", "Khmer", "Thai",
                      "Malay", "Ukrainian", "Romanian", "Bulgarian"]


prompt_0 = "Tell us a fun random fact from modern or ancient history.\n"
prompt_1 = "Write a haiku and give it a creative title and write the title first.\n"
prompt_2 = "Write a fun limerick and give it a fun tittle and write the title first.\n"
prompt_3 = "Quote a philosopher and include the philosophers name after the quote.\n"
prompt_4 = "Tell a yo mama joke.\n"
prompt_5 = "Tell us a fun random science fact.\n"
prompt_6 = "Tell a dad joke.\n"
# prompt_7 = "Say an appropriate Christmas greeting to the people in {country} in the official language of {country}. "
# prompt_8 = "Offer a traditional new year greeting to the people in {country} in the official languages of {country} " \
#            "and do not mention any dates in the response. {prompts.char_count} "

prompt_options = [
    prompt_0,
    prompt_1,
    prompt_2,
    prompt_3,
    prompt_4,
    prompt_5,
    prompt_6,
    # prompt_7,
    # prompt_8
]
