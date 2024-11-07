def laske(luku):

    for i in range(2, luku):
        jakojäännös = luku % i
        if jakojäännös == 0:
            return False
    return True