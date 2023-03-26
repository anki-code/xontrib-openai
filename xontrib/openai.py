"""
TODO: Please add here the short description of the xontrib to show in `xonfig web`.
"""
from xonsh.built_ins import XSH



__all__ = ()

print('This is xontrib-openai!')


# Good start! Get more documentation -> https://xon.sh/contents.html#guides

# Accessing environment variables
# Note! If you want to create new env variables please name it with the beginning of the xontrib name
# i.e. if the xontrib called xontrib-hello-world name the variables as XONTRIB_HELLO_WORLD_NEW_VARIABLE

# Some code in Using Python API:
var = XSH.env.get("VAR", "default")
result = XSH.subproc_captured_stdout(['echo', '1'])

