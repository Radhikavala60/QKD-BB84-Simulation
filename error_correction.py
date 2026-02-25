def simple_error_correction(alice_key, bob_key):
    corrected_key = []

    for i in range(len(alice_key)):
        if alice_key[i] == bob_key[i]:
            corrected_key.append(alice_key[i])

    return corrected_key