def test1():
    """Test UserInput."""
    from UserInput import user_input
    assert user_input('Name') == 'Bugs'
    assert user_input('Surname', default='Bunny') == 'Bunny'
    assert user_input('Bird', choices=('Tweety','Beaky')) == 'Tweety'
    assert user_input('Bird', choices=('Tweety','Beaky')) == 'Beaky'
    assert not user_input('empty input', empty_ok=True)
    assert user_input('last one') == 'The end.'
