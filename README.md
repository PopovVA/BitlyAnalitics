# Bitly url shorterer

Pjocets has been created for demonstrate how working Bitly API, creating shorty link and get amount clicks

## How to install

1. Python3 should be already installed. Then use ```pip``` (or ```pip3```, if there is a conflict with Python2) to install dependencies:

```bash
$ pip install -r requirements.txt
```

2. Environments keys should be in ```.env``` file, he should contains one variable 
```
token=your_token_from_bitly
```

3. Now we can run the code
```
$ python3 'path to main.py' 'your link'
```
## Example
1. ```$ python3 main.py https://github.com/PopovVA```
2. ``` Authorization is succes```
3. ``` http://bit.ly/2FlWRqj ```

or if you already have bitly link, and want to get amount clicks

1. ```$ python3 main.py bit.ly/2FlWRqj```
2. ``` Authorization is succes```
3. ``` Amount clicks : 1 ```

## Project goals

The code is written for educational purposes on online-course for web-developers dvmn.org.
