# Grupp 20 Reflektioner - Filip, Leo and Mikko  

## Link to the project:
https://github.com/BonnieToGamer/BurgerOrderer

## Short summary of the functionality testing.
The functionality tests checked how our project reacted if different types of data was sent instead of the correct data type. For example if no data was sent or the wrong burger name etc.

## How the tests was carried out 
We made automated tests that tests different parts of burgerer_orderer and kitchen_view. The tests were created to test the different api endpoints such as /api/getBurgers and /api/getSpecials, and check how they handle different types of data, like a different burger name or specials selections. To start a test you can use the command "make test", this will run through the tests.

## Latest testsession print out:
```bash
$ make test
# -- output skipped for brevity -- #

----------------------------- burger orderer tests -----------------------------

docker logs burger_orderer_test_container --since 5s
============================= test session starts ==============================
platform linux -- Python 3.12.6, pytest-8.3.3, pluggy-1.5.0 -- /opt/venv/bin/python
cachedir: .pytest_cache
rootdir: /app
collecting ... collected 8 items

tests/test_burger_orderer.py::test_get_burgers_get PASSED                [ 12%]
tests/test_burger_orderer.py::test_get_specials_default_burger PASSED    [ 25%]
tests/test_burger_orderer.py::test_get_specials_no_burger PASSED         [ 37%]
tests/test_burger_orderer.py::test_get_specials_no_burger_name PASSED    [ 50%]
tests/test_burger_orderer.py::test_get_specials_non_existent_burger PASSED [ 62%]
tests/test_burger_orderer.py::test_new_order_valid_data PASSED           [ 75%]
tests/test_burger_orderer.py::test_new_order_no_data PASSED              [ 87%]
tests/test_burger_orderer.py::test_new_order_malformed_order PASSED      [100%]

============================== 8 passed in 0.75s ===============================

------------------------------ kitchen view tests ------------------------------

docker logs kitchen_view_test_container --since 5s
============================= test session starts ==============================
platform linux -- Python 3.12.6, pytest-8.3.3, pluggy-1.5.0 -- /opt/venv/bin/python
cachedir: .pytest_cache
rootdir: /app
collecting ... collected 8 items

tests/test_kitchen_view.py::test_new_order_success PASSED                [ 12%]
tests/test_kitchen_view.py::test_new_order_broken_order PASSED           [ 25%]
tests/test_kitchen_view.py::test_new_order_broken_burger PASSED          [ 37%]
tests/test_kitchen_view.py::test_new_order_malformed_burger_data PASSED  [ 50%]
tests/test_kitchen_view.py::test_new_order_empty_burger_data PASSED      [ 62%]
tests/test_kitchen_view.py::test_new_order_broken_specials PASSED        [ 75%]
tests/test_kitchen_view.py::test_new_order_malformed_specials PASSED     [ 87%]
tests/test_kitchen_view.py::test_new_order_malformed_specials_data PASSED [100%]

============================== 8 passed in 0.10s ===============================
```

## Group experiences about automated testing
The testing went generally good. We already had a good understanding of what we should test, the complicated part of automated testing was to actually make the code for the tests. But once we understood how to make the code for one test, the rest of the code was not that hard to complete since it consists of the same code structure for each test.

## The groups individual debugging sessions
The debugging sessions can be viewed in our individual engineering journals.





