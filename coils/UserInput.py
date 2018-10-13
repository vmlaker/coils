"""Like the input built-in, but with bells and whistles."""

import getpass

# Use raw_input for Python 2.x
try:
    input = raw_input
except NameError:
    pass


def user_input(
        field, default='', choices=None, password=False,
        empty_ok=False, accept=False):
    """Prompt user for input until a value is retrieved or default
    is accepted. Return the input.

    Arguments:

    *field* - Description of the input being prompted for.

    *default* - Default value for the input accepted with a Return-key.

    *password* - Whether the user input should not be echoed to screen.

    *empty_ok* - Whether it's okay to accept an empty input.

    *accept* - Whether to skip getting actual user input and just accept
    the default value, unless prevented by the combination of
    arguments *empty_ok* and *default*. That is, unless *default*
    is an empty string and *empty_ok* is False.
    """
    result = ''
    while not result:
        prompt = field
        if default:
            prompt += ' [{0}]'.format(default)
        prompt += ': '
        if accept and not (not default and not empty_ok):
            print(prompt)
            result = '{0}'.format(default)
        else:
            if password:
                result = getpass.getpass(prompt)
            else:
                result = input(prompt)
        result = result.strip()
        if not result:
            result = default
        if choices and result not in choices:
            print('Must be one of {0}'.format(choices))
            result = ''
        if empty_ok:
            break
    return result
