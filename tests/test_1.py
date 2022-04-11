import pytest
#come back to this later
# from queries.select import hereoes_select, new

###something is going wrong here and I cannot figure out what it is.  Bring up as a blocker
# from demo import find_hero

## get tests set up correctly
def test_always_passes():

    assert True

#test
def test_search():
    assert demo.find_hero('The Hummingbird') == "It's a Bird! It's a plane! Oh wait, it's really just a bird... It's The Hummingbird!"