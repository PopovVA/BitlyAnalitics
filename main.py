import requests
import os


def check_authorization():
  headers = {
    'Authorization': 'Bearer {}'.format(TOKEN)
  }
  url = 'https://api-ssl.bitly.com/v4/user'
  response = requests.get(url, headers=headers)
  return response.ok

def create_short_link(long_url):
  data = {
  "long_url": long_url
   }
  headers = {
    'Authorization': 'Bearer {}'.format(TOKEN)
  }
  url = 'https://api-ssl.bitly.com/v4/bitlinks'
  response = requests.post(url, json=data, headers=headers)
  if not response.ok:
    return
  short_link = response.json()["link"]
  return short_link

def get_amount_clicks(short_link):
  headers = {
    'Authorization': 'Bearer {}'.format(TOKEN)
  }
  url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
  url = url_template.format(short_link)
  response = requests.get(url, headers=headers)
  if not response.ok:
    return None
  amount_clicks = response.json()["total_clicks"]
  return amount_clicks

def short_link(input_url):
  url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{}'
  url = url_template.format(input_url)
  headers = {
    'Authorization': 'Bearer {}'.format(TOKEN)
  }
  response = requests.get(url, headers=headers)
  return response.ok

def main():
  TOKEN = os.getenv("token")
  input_url = input("Type any link: ")

  if authorize():
    print ('Authorization is succes')
  else:
    print ('Error: Authorization is failed')
    quit()

  if short_link(input_url):
    amount_clicks = get_amount_clicks(input_url)
    msg_tmp = 'Amount clicks : {}'
    link = msg_tmp.format(amount_clicks)
  else:
    link = create_short_link(input_url)
    if link is None:
      print ('Wrong link')
      quit()
  print (link)
 

if __name__ == '__main__':
 main()
