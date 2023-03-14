def test_test():
    assert 1 == 1


def test_user_age_is_42(user):
    assert user.age == 43

def test_user_age_is_55(user):
    assert user.age == 55