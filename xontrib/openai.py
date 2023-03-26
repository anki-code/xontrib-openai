"""
Use Open AI models in xonsh shell. 
"""

@aliases.register("ai")
def __ai(args):
    import openai
    openai.api_key = __xonsh__.env.get('OPENAI_API_KEY', '')
    response = openai.Completion.create(**{
        'prompt': ' '.join(args),
        'engine': __xonsh__.env.get('OPENAI_MODEL', 'text-davinci-003'),
        'max_tokens': __xonsh__.env.get('OPENAI_MAX_TOKENS', 100)
    })
    print(response.choices[0].text.strip())
