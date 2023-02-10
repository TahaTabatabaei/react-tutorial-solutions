# Simple Test with selenium

The script `test.py` contains a test class, including three methods. The function `setUp` is for initialization. The function `tests` contains the main parts of the tests.
It contains 4 tests:

## reset:
    It tests if the reset button is visible. We simulate a set of actions, then we look to see if the reset button is discoverable. 
    It passes.

## test win:
    We build a scenario which leads to X winning the game.
    It passes.

## test play again:
    After finishing the scenario which results in X winning, we look to see if the "play again" button is discoverable.
    It passes.

## test draw:
    We build a scenario which leads to X winning the game.
    It passes.

The `tearDown` function closes driver.