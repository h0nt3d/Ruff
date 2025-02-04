from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Your really silent......'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'bye' in lowered:
        return 'See you later!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice(['I do not understand...',
                       'What did you say?',
                       'Can you reprhase that?'])
