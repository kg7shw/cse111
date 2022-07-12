from sentences import get_determiner, get_noun, get_verb


import pytest














# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])