#!/usr/bin/python3

import requests, json

USER = '#####'
PASS = '#####'

def generate_lnurl():

    data = {
            'satoshis': '50',
    }

    response = requests.post(
        'https://lntxbot.alhur.es/generatelnurlwithdraw',
        auth=(USER, PASS),
        data=json.dumps(data),
        )

    # response =  requests.post(
    #     'https://lntxbot.alhur.es/generatelnurlwithdraw',
    #     headers = {'Grpc-Metadata-macaroon': macaroon},
    #     data=json.dumps(data),
    # )

    response = json.loads(response.text)
    print(response)

if __name__ == '__main__':
    try:
        generate_lnurl()
    except KeyboardInterrupt:
        sys.exit('Manually Interrupted')
