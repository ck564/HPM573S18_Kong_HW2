# Problem 1 - HUI3 Instrument

# HUI3 constants and attribute utility scores
Constant_1 = 1.371
Constant_2 = 0.371
dictUtilityScores = {'Vision':      [1.00, 0.98, 0.89, 0.84, 0.75, 0.61],
                    'Hearing':      [1.00, 0.95, 0.89, 0.80, 0.74, 0.61],
                    'Speech':       [1.00, 0.94, 0.89, 0.81, 0.68],
                    'Ambulation':   [1.00, 0.93, 0.86, 0.73, 0.65, 0.58],
                    'Dexterity':    [1.00, 0.95, 0.88, 0.76, 0.65, 0.56],
                    'Emotion':      [1.00, 0.95, 0.85, 0.64, 0.46],
                    'Cognition':    [1.00, 0.92, 0.95, 0.83, 0.60, 0.42],
                    'Pain':         [1.00, 0.96, 0.90, 0.77, 0.55]}

def score_calculation(vision, hearing, speech, ambulation, dexterity,
                     emotion, cognition, pain):


    """
    :param vision: functionality of vision, 6 attribute levels: 6 being worst
    :param hearing: functionality of hearing, 6 attribute levels: 6 being worst
    :param speech: functionality of speech, 5 attribute levels: 5 being worst
    :param ambulation: ability for ambulation, 6 attribute levels: 6 being worst
    :param dexterity: extent of dexterity function, 6 attribute levels: 6 being worst
    :param emotion: emotional status, 5 attribute levels: 5 being worst
    :param cognition: level of cognitive function, 6 attribute levels: 6 being worst
    :param pain: level of experienced pain, 5 attribute levels: 5 being worst
    :return: HUI3 utility score, with 1=perfect health and 0=dead
    """

    # input validation
    if not(vision in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Vision attribute level can only take values between 1 and 6, inclusive')
    if not(hearing in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Hearing attribute level can only take values between 1 and 6, inclusive')
    if not(speech in [1, 2, 3, 4, 5]):
        raise ValueError('Speech attribute level can only take values between 1 and 5, inclusive')
    if not(ambulation in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Ambulation attribute level can only take values between 1 and 6, inclusive')
    if not(dexterity in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Dexterity attribute level can only take values between 1 and 6, inclusive')
    if not(emotion in [1, 2, 3, 4, 5]):
        raise ValueError('Emotion attribute level can only take values between 1 and 5, inclusive')
    if not(cognition in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Cognition attribute level can only take values between 1 and 6, inclusive')
    if not(pain in [1, 2, 3, 4, 5]):
        raise ValueError('Pain attribute level can only take values between 1 and 5, inclusive')

    # score calculation
    score = 0
    score = (Constant_1 * dictUtilityScores['Vision'][vision-1] * dictUtilityScores['Hearing'][hearing-1]
            * dictUtilityScores['Speech'][speech-1] * dictUtilityScores['Ambulation'][ambulation-1]
            * dictUtilityScores['Dexterity'][dexterity-1] * dictUtilityScores['Emotion'][emotion-1]
            * dictUtilityScores['Cognition'][cognition-1] * dictUtilityScores['Pain'][pain-1]) - Constant_2

    return score


