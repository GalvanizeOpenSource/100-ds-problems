from random import shuffle
from operator import mul


def make_prob_list(n, deck_size=60, hand_size=5, num_specials=3, intro=''):
    '''
    Calculate the probability of having n special cards in a deck of size
    deck_size with a hand of size hand_size. num_specials is the number of
    special cards you are looking for.
    The function also generates a string which starts with intro and
    contains the longform multiplication to calculate the probability.

    Parameters
    ----------
    n : int
        the number of special cards in the drawn hand

    deck_size : int
        the size of deck from which cards are being drawn

    hand_size : int
        the size of hand to draw up to

    num_specials : int
        the number of special cards in the deck

    intro : string, optional
        a string with any initial text desired for the probability calculation

    Returns
    -------
    base : string
        a string showing the multiplication of fractions and n choose k
        to demonstrate how the probability is calculated

    value : float
        the probability of drawing n many special cards in a hand of hand_size

    '''
    # helper functions for factorial and n choose k
    def f(x): return 1 if x == 0 else reduce(mul, range(1, x + 1))

    def nCk(x, y): return f(x)/(f(x - y) * f(y))

    remainder = hand_size - n
    start = map(lambda x: ((num_specials - x), float(deck_size - x)), range(n))
    if not start:
        start = [(deck_size, float(deck_size))]
    num = deck_size - num_specials
    den = deck_size - n

    for _ in range(remainder):
        start.append((num, float(den)))
        num -= 1
        den -= 1

    if '{}' in intro:
        base = intro.format(n)
    else:
        base = intro

    result = []
    for entry in start:
        base += u'{}/{} * '.format(*entry)
        result.append(entry[0]/entry[1])
    result.append(nCk(hand_size, n))
    value = reduce(mul, result)
    base += u'({} choose {}) = {:.4f}'.format(hand_size, n, value)
    return base, value


def p_n_stars(n):
    '''
    Calculate the probability of having n star cards in a 5 card hand with a
    60 card deck containing 3 star cards total

    Parameters
    ----------
    n : int
        the number of star cards in a 5 card hand

    Returns
    -------
    base : string
        the string representation of the probability calculation

    value : float
        the probability being calculated

    '''
    base, value = make_prob_list(n, intro=u'P({}\u2606) = ')
    return base, value


def p_d_given_nstars(d, n):
    '''
    Calculate the probability of having d many diamond cards assuming you had
    n many star cards with an initial 5 card draw. Star cards are required to
    be turned in for 3 new cards. Assumes there are 3 each of diamond and star
    cards in the deck when dealt. It does not matter for the probability if the
    star cards were present in the initial draw or acquired during the redraw
    as they are still turned in. This can lead to a final hand size larger than
    5 cards. Conditioning on the number of star cards means we use a deck size
    of 57 rather than 60, since it is impossible to alter the number of star
    cards in the hand.

    Parameters
    ----------
    d : int
        number of diamond cards

    n : int
        number of star cards

    Returns
    -------
    base : string
        string representation of the probability being calculated

    value : float
        P(d diamonds|n stars), probability of d many diamond cards given n
        many star cards
    '''
    num_cards = 5 - n + (n * 3)
    string = u'P({{}}\u2662|{}\u2606) = '.format(n)
    base, value = make_prob_list(d, 57, num_cards, intro=string)
    return base, value


def sim_card_draw(n=10000):
    '''
    Perform a simulation to estimate probability of getting a least one diamond
    card when drawing five cards. Deck has 60 cards, there are 3 star cards and
    3 diamond cards. If a star card is in your hand it is turned in for three
    new cards. This is done until no star cards remain.

    Parameters
    ----------
    n : int
        number of simulations to run

    Returns
    -------
    prob : float
        estimated probability of at least one diamond card in hand

    '''
    cards = tuple(['N' for _ in range(60-6)] + ['S', 'S', 'S', 'D', 'D', 'D'])
    count = 0.
    for _ in xrange(n):
        if individual_run(cards):
            count += 1.
    return count/n


def individual_run(cards):
    '''
    Run a single simulation of drawing a hand, replacing star cards with 3 new
    cards and then counting the number of diamond cards in your hand

    Parameters
    ----------
    cards : tuple
        tuple containing the deck from which to draw

    Returns
    -------
    count : int
        number of diamond cards in hand after turning in star cards for 3 new
        cards

    '''
    deck = list(cards)
    shuffle(deck)
    hand = [deck.pop() for _ in range(5)]
    while 'S' in hand:
        hand.remove('S')
        hand += [deck.pop() for _ in range(3)]
    return hand.count('D')


def exact_prob():
    '''
    Function to generate a string representing performing the exact calculation
    for the probability estimated by `sim_card_draw`. It creates a string
    suitable for following along with the calculation assuming reader is
    familiar with calculating probabilies of draws without replacement from a
    resevoir.

    Parameters
    ----------

    Returns
    -------
    output : string
        the string representing the probability calculation

    '''
    base = u'P(0\u2662|{0}\u2606) * P({0}\u2606)'

    d = 0
    output = u'P(>1\u2662) = 1 - P(0\u2662)\n'

    output += u'P({}\u2662) = '.format(d)
    output += u' + '.join(base.format(i) for i in range(4))
    output += u'\n\n'

    star_values = []
    for i in range(4):
        string, temp = p_n_stars(i)
        output += u'{}\n'.format(string)
        star_values.append(temp)
    output += u'\n'

    diamond_values = []
    for i in range(4):
        string, temp = p_d_given_nstars(d, i)
        diamond_values.append(temp)
        output += u'{}\n'.format(string)
    output += u'\n'

    output += u'P(>1\u2662) = 1 - ('
    out = u''
    value = 0.
    for d_val, s_val in zip(star_values, diamond_values):
        out += u'{:.4f} * {:.4f} + '.format(d_val, s_val)
        value += d_val * s_val

    output += u'{}) = {:.4f}\n'.format(out.strip(u' + '), 1 - value)
    return output


def make_solution():
    '''
    Generate the exact probability string for the deck drawing mechanics, then
    perform a numeric simulation of the same with 100000 runs. Print out the
    calculation string and add on a comparison to the simulated value. Then
    write this to disk at Probability_1_soln.txt

    Parameters
    ----------

    Returns
    -------

    '''
    output = exact_prob()
    sim = sim_card_draw(100000)
    output += u'this is ~= to the simulation value of: {:.4f}'.format(sim)
    with open('Probability_1_soln.txt', 'w') as f:
        f.write(output.encode('utf8'))


if __name__ == '__main__':
    make_solution()
