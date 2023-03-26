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

```xsh
$OPENAI_API_KEY = 'abcd1234'  # https://platform.openai.com/account/api-keys

# Defaults:
# $OPENAI_MODEL = 'text-davinci-003'  # https://platform.openai.com/docs/models/overview
# $OPENAI_MAX_TOKENS = 100

xontrib load openai

ai! write git commit on bash. Give me only command
# git commit -m "Commit message"

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

## Credits

This package was created with [xontrib template](https://github.com/xonsh/xontrib-template).
