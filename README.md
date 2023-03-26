<p align="center">
Use Open AI models in xonsh shell.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20xontrib%20for%20the%20xonsh%20shell!&url=https://github.com/anki-code/xontrib-openai" target="_blank">tweet</a>.
</p>


## Installation

To install use pip:

```xsh
xpip install -U xontrib-openai
# or: xpip install -U git+https://github.com/anki-code/xontrib-openai
```

## Usage

```python
$OPENAI_API_KEY = 'abcd1234'  # https://platform.openai.com/account/api-keys

# Defaults:
# $OPENAI_MODEL = 'text-davinci-003'  # https://platform.openai.com/docs/models/overview
# $OPENAI_MAX_TOKENS = 500

xontrib load openai
```

### Get shell commands
```python
ai! write git commit on bash. Give me only command
# git commit -m "Commit message"
```
```python
ai! how to remove all containers and images in docker. Only commands please
# docker stop $(docker ps -a -q)
# docker rm $(docker ps -a -q)
# docker rmi $(docker images -a -q)
```

### Get Python code
```python
ai! send post request with json data on python
# import requests
# import json
# 
# url = 'http://example.com/api/1/users'
# data = {
#   "first_name": "John",
#   "last_name": "Smith"
# }
# 
# headers = {'Content-type': 'application/json'}
# response = requests.post(url, data=json.dumps(data), headers=headers)
```

### Generate data
```python
ai! give me json where keys are fruits and values are most common fruit color
# {
#     "Apple": "Red",
#     "Banana": "Yellow",
#     "Orange": "Orange",
#     "Grape": "Purple",
#     "Strawberry": "Red",
#     "Lemon": "Yellow",
#     "Kiwi": "Green",
#     "Cherry": "Red",
#     "Watermelon": "Green"
# }
```

## Known issues

To use [`gpt-4`](https://platform.openai.com/docs/models/gpt-4) model join [wait list](https://openai.com/waitlist/gpt-4-api).

## Credits

This package was created with [xontrib template](https://github.com/xonsh/xontrib-template).
