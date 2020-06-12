# ----------------------------------
import requests

import pprint

import argparse


# ----------------------------------

default_url = '<URL of chatbot>'
default_bot_id = 'ID'
default_quit_message = 'exit'
# ----------------------------------
def get_args():
    """Get arguments and return their list"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", type=str, default=default_url,
                        help="input bot generator url")
    parser.add_argument("-i", "--id", type=str, default=default_bot_id,
                        help="input bot id")
    return parser.parse_args()

def chat_show_result_one_utterance(url, bot_id, messageText):
    params = {'bot_id': bot_id, 'messageText': messageText}

    ## Make invocation for a turn
    x = requests.post(url, data=params)
    result = x.json()

    print('Utterance made = ' + messageText)
    output = result['output']
    print('Response obtained = ' + str(output['text']))

    pp = pprint.PrettyPrinter(indent=4)
    print('Full Response  = ' + str(pp.pprint(output)))

    ## Process output for issue-based rating of utterance, i.e., output

def do_chat(url, bot_id):

    # We will first chat with a default message and then continue
    #messageText = 'First chat test: How much data do you know about?'
    messageText = 'Hi!'

    chat_show_result_one_utterance(url, bot_id, messageText)

    # 'messageText' : 'How much data do you know about?'

    #url = 'URL of CHATBOT API'
    #params = {'bot_id': 'ID', 'messageText' : messageText}

    while messageText != default_quit_message:

        # Chat with previous meesage
        chat_show_result_one_utterance(url, bot_id, messageText)

        # Get message to chat about
        print('--> Enter text or <exit> to quit, without<>.')
        messageText = input("Enter text : ")
        messageText = messageText.strip()

# ----------------------------------

if __name__ == "__main__":
    ARGS = get_args()
    do_chat(ARGS.url, ARGS.id)

    print('--> All done.')