import pytest
from sentences import make_basic_sentence, get_determiner, get_noun, get_verb, get_noun, make_complex_sentence, get_prepositional_phrase, get_preposition, get_adverb, get_adjective
import random




def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners



def test_get_noun():

    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    for i in range(9):

        word = get_noun(1)

        assert word in single_nouns


    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    for i in range(9):

        word = get_noun(2)

        assert word in plural_nouns


def test_get_verb():

    past_tense = ["drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"]
    for i in range(9):

        word = get_verb(1, "past")

        assert word in past_tense

    present_tense_singular = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for i in range(9):

        word = get_verb(1, "present")

        assert word in present_tense_singular

    present_tense_plural = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for i in range(9):

        word = get_verb(2, "present")

        assert word in present_tense_plural

    future_tense = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for i in range(9):

        word = get_verb(1, "future")

        assert word in future_tense

def test_get_prepositional_phrase():
    phrase = get_prepositional_phrase(1)
    words_list = phrase.split(' ')
    prep = words_list[0]
    det = words_list[1]
    noun = words_list[2]
    prep_words = ["aboard", "about", "above", "across", "after", "against", "along", "amid", "among", "anti", "around", "as", "at", "before", "behind", "below", "beneath", "beside", "besides", "between", "beyond", "but", "by", "concerning","considering", "despite", "down", "during", "except", "excepting", "excluding", "following", "for", "from", "in", "inside", "into", "like", "minus", "near", "of", "off", "on", "onto", "opposite", "outside", "over", "past", "per", "plus", "regarding", "round", "save", "since", "than", "through", "to", "toward", "towards", "under", "underneath", "unlike", "until", "up","upon", "versus", "via", "with", "within", "without"]

    assert prep in prep_words

def test_get_preposition():

    prep_words = ["aboard", "about", "above", "across", "after", "against", "along", "amid", "among", "anti", "around", "as", "at", "before", "behind", "below", "beneath", "beside", "besides", "between", "beyond", "but", "by", "concerning","considering", "despite", "down", "during", "except", "excepting", "excluding", "following", "for", "from", "in", "inside", "into", "like", "minus", "near", "of", "off", "on", "onto", "opposite", "outside", "over", "past", "per", "plus", "regarding", "round", "save", "since", "than", "through", "to", "toward", "towards", "under", "underneath", "unlike", "until", "up","upon", "versus", "via", "with", "within", "without"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(69):

        word = get_preposition(1)


        assert word in prep_words


def test_get_adjective():
    for _ in range(4):

        word = get_adjective(1)
        adj_words = ["adventurous", "aggressive", "ashamed", "attractive", "beautiful", "calm", "embarrassed", "funny"]


        assert word in adj_words




# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])