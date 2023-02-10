## Test with selenium

The scripe contains a test class, including 3 methods. The function `setUp`
is the initializations. The function `tests` has the main parts of tests.
It contains 4 tests:

# 1- rest:
    It tests if the reset button is visable. We simulate a set of actions, then we look if 
    reset button is dicoverable.
    It pass.

# 2- [test win]:
    We bulid a scenario which leads X wining the game.
    It pass.

# 3- test play again:
    After finishing the scenario which X is winner, we look to see if play again button is 
    discoverable.
    It pass. 

# 4- test draw:
    We bulid a scenario which leads X wining the game.
    It pass

The `tearDown` function close driver.