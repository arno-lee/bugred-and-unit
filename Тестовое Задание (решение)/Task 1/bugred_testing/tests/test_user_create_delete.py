import pytest
from selenium import webdriver

from Framework.BugredHome import BugredHome
from Framework.Utils.Browser import Browser
from Framework.Utils.Config import Config


@pytest.fixture(scope='module')
def setup():
  config = Config("tests/config")
  browser = Browser(webdriver.Chrome)

  yield config

  browser.quit()

@pytest.fixture(scope='module')
def test_data():
  full_user_details = {
    "name" : "Sandra Lee Westfield",
    "email" : "sandra_westfield_2024@primemail.com",
    "password" : "asdfgh",
    "avatar" : "avatar_path",
    "birthday" : "12/10/2000",
    "gender" : "Женский",
    "date_start" : "10/05/2020",
    "hobby" : "Reading, gardening",
    "name1" : "Sandra",
    "surname1" : "Westfield",
    "fathername1" : "Lee",
    "cat" : "Clara",
    "dog" : "Booch",
    "parrot" : "Pinky",
    "cavy" : "Lil Joe",
    "hamster" : "Chuck",
    "squirrel" : "Lilly",
    "phone" : "+1 366 245 536 233",
    "adres" : "Seattle, Westfield lane, 22",
    "inn" : "43152252636"
  }
  yield full_user_details

@pytest.mark.order(1)
def test_add_user_and_exit(setup, test_data):
  config = setup
  full_user_details = test_data
  
  bugred_home = BugredHome()
  log_in_form = bugred_home.log_in_form()

  users_home = log_in_form.log_in(config.credentials.user_email, config.credentials.password)

  add_user_form = users_home.users_panel.add_user_form()
  add_user_form.add_multiple_fields(full_user_details)

  assert users_home.users_panel.users_list.email_present(full_user_details["email"]), "No user created"

  users_home.nav_bar.user_exit()

@pytest.mark.order(2)
def test_log_new_user_view_and_exit(test_data):
  full_user_details = test_data

  bugred_home = BugredHome()
  log_in_form = bugred_home.log_in_form()
  users_home = log_in_form.log_in(full_user_details["email"], full_user_details["password"])

  users_home.users_panel.search_user_form.search_user(full_user_details["email"])
  assert users_home.users_panel.users_list.email_present(full_user_details["email"])

  user_profile = users_home.users_panel.users_list.view_1st()
  assert full_user_details["name"] == user_profile.user_name.text, "User name does not match"
  assert full_user_details["email"] == user_profile.email.text, "User email does not match"
  assert full_user_details["phone"] == user_profile.phone.text, "User phone does not match"

  user_profile.nav_bar.user_exit()

@pytest.mark.order(3)
def test_find_new_user_and_delete(setup, test_data):
  config = setup
  full_user_details = test_data

  bugred_home = BugredHome()
  log_in_form = bugred_home.log_in_form()
  users_home = log_in_form.log_in(config.credentials.user_email, config.credentials.password)

  users_home.users_panel.search_user_form.search_user(full_user_details["email"])
  users_home.users_panel.users_list.delete_1st()
  assert users_home.users_panel.users_list.table_empty, "User has not been deleted"
  