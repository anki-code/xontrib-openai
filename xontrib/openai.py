"""
Use Open AI models in xonsh shell. 
"""

aliases['ai'] = """openai api @(__xonsh__.env.get('OPENAI_METHOD', 'completions.create')) \
                     -m @(__xonsh__.env.get('OPENAI_MODEL', 'text-davinci-003')) \
                     -t @(__xonsh__.env.get('OPENAI_TONALITY', 0))  \
                     -M @(__xonsh__.env.get('OPENAI_MAX_TOKENS', 500)) \
                     @('--stream' if __xonsh__.env.get('OPENAI_STREAM', True) else '') \
                     -p @(' '.join($args))"""
