import os
import requests
import json
from datetime import datetime, timedelta, timezone

def post_slack(payload):
  WEBHOOK_URL=os.environ['WEBHOOK_URL']
  res = requests.post(WEBHOOK_URL, json=payload)
  print(res.text)

def main():
  BASE_URL = 'https://getpocket.com/v3/get'
  JST = timezone(timedelta(hours=+9), 'JST')
  now_timestamp = (datetime.now(JST)-timedelta(minutes=5)).replace(hour=0, minute=0, second=0, microsecond=0).timestamp()
  payload = {
      'consumer_key': os.environ['CONSUMER_KEY'],
      'access_token': os.environ['ACCESS_TOKEN'],
      'state': 'unread',
      'sort': 'newest',
      'since': now_timestamp
      }
  res = requests.post(BASE_URL, json=payload)
  if len(res.json()['list']) == 0:
    post_payload = {
        "attachments": [
          {
            "pretext": "*Daily Pocket*",
            "title": "no Pocket today"
            }
          ]
        }
  else:
    attachments = [{'color': "#36a64f", 'title':item['resolved_title'], 'title_link':item['resolved_url'], 'text': item['excerpt']} for item in res.json()['list'].values()]
    attachments[0]['pretext'] = '*Daily Pocket*' 
    post_payload = {
        "attachments": attachments
        }

  post_slack(post_payload)

if __name__ == '__main__':
  main()
