import math
import random

def main():
    make_basic_sentence(1, "past")
    make_basic_sentence(1, "present")
    make_basic_sentence(1, "future")
    make_basic_sentence(2, "past")
    make_basic_sentence(2, "present")
    make_basic_sentence(2, "future")


    make_complex_sentence(1, "past")
    make_complex_sentence(1, "present")
    make_complex_sentence(1, "future")
    make_complex_sentence(2, "past")
    make_complex_sentence(2, "present")
    make_complex_sentence(2, "future")

    get_prepositional_phrase(1)

        

def make_basic_sentence(quantity, tense):
    det = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    # prep = get_preposition
    sentence = f"{det.capitalize()} {noun} {verb}."
    print(sentence)

def make_complex_sentence(quantity, tense):
    det = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    adj =  get_adjective(quantity)
    prep_phrase = get_prepositional_phrase(quantity)

    sentence = f"{det.capitalize()} {adj} {noun} {verb} {prep_phrase}."
    print(sentence)

    
    



def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "two", "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
            words = ["drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    else:
        # tense == "future"
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word



def get_preposition(quantity):
    """Return a randomly chosen preposition
    from this list of prepositions:
        "aboard", "about", "above", "across", "after", "against", "along", "amid", "among", "anti", "around", "as", "at", "before", "behind", "below", "beneath", "beside", "besides", "between", "beyond", "but", "by", "concerning","considering", "despite", "down", "during", "except", "excepting", "excluding", "following", "for", "from", "in", "inside", "into", "like", "minus", "near", "of", "off", "on", "onto", "opposite", "outside", "over", "past", "per", "plus", "regarding", "round", "save", "since", "than", "through", "to", "toward", "towards", "under", "underneath", "unlike", "until", "up","upon", "versus", "via", "with", "within", "without"

    Return: a randomly chosen preposition.
    """
    if quantity == 1 or quantity == 2:
        words = ["aboard", "about", "above", "across", "after", "against", "along", "amid", "among", "anti", "around", "as", "at", "before", "behind", "below", "beneath", "beside", "besides", "between", "beyond", "but", "by", "concerning","considering", "despite", "down", "during", "except", "excepting", "excluding", "following", "for", "from", "in", "inside", "into", "like", "minus", "near", "of", "off", "on", "onto", "opposite", "outside", "over", "past", "per", "plus", "regarding", "round", "save", "since", "than", "through", "to", "toward", "towards", "under", "underneath", "unlike", "until", "up","upon", "versus", "via", "with", "within", "without"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word
    

def get_prepositional_phrase(quanitiy):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    prep = get_preposition(quanitiy)
    det = get_determiner(quanitiy)
    noun = get_noun(quanitiy)
    phrase = f"{prep} {det} {noun}"
    return phrase


def get_adverb(quantity):
    if quantity == 1 or quantity == 2:
        words = ["boldly", "bravely", "brightly", "cheerfully", "deftly", "devotedly", "eagerly", "elegantly", "faithfully"]
        # Randomly choose and return a determiner.
        word = random.choice(words)
        return word

def get_adjective(quantity):
    if quantity == 1 or quantity == 2:
        words = ["adventurous", "aggressive", "ashamed", "attractive", "beautiful", "calm", "embarrassed", "funny"]
        # Randomly choose and return a determiner.
        word = random.choice(words)
        return word


main()















