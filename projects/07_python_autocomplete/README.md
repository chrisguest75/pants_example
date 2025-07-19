# NOTES

Aim to get a quick skeleton for the quick development of python code.

## Running

NOTE: Make sure you are in the folder before you execute the tests.  

## Debugging

There is a `launch.json` file that will start and debug the file.  

## Recreate

* `uv init`
* `uv add pytest`
* Add tests and __init__.py
* Add test
  ```py 
  def test_step():
      assert True
  ```

* Write a simple test and run it
* `uv run pytest -vv`
* `uv run main.py`

* Single step
  * Tests - Using the test tube
  * Main - Using the `launch.json`
