# ASSERT
# GET


def test_login_page(db, client):
    """
    Test that the login page loads.
    """
    response = client.get("/accounts/login/")
    assert response.status_code == 200


def test_signup_page(db, client):
    """
    Test that the signup page loads.
    """
    response = client.get("/accounts/signup/")
    assert response.status_code == 200


def test_logout_page(db, client):
    """
    Test that the logout page loads.
    """
    response = client.get("/accounts/logout/")
    assert response.status_code == 302


def test_train_create_page_without_user_logged(db, client):
    """
    Test that the train create page loads.
    """
    response = client.get("/train/create/")
    assert response.status_code == 302


def test_train_delete_without_user_logged(db, client):
    """
    Test that the train delete page loads.
    """
    response = client.get("/train/delete/1")
    assert response.status_code == 301


# def test_train_delete_with_user_logged(db, client, train_factory):
#     """
#     Test that the train delete page loads.
#     """
#     train = train_factory()
#     id = train.id
#     response = client.get("/train/delete/{}".format(id))
#     assert response.status_code == 301
