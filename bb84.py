import random

def generate_raw_key(length):
    alice_bits = [random.randint(0,1) for _ in range(length)]
    alice_bases = [random.choice(['+', 'x']) for _ in range(length)]
    bob_bases = [random.choice(['+', 'x']) for _ in range(length)]

    bob_results = []

    for i in range(length):
        if alice_bases[i] == bob_bases[i]:
            bob_results.append(alice_bits[i])
        else:
            bob_results.append(random.randint(0,1))

    return alice_bits, alice_bases, bob_bases, bob_results


def sift_key(alice_bits, alice_bases, bob_bases, bob_results):
    sifted_alice = []
    sifted_bob = []

    for i in range(len(alice_bits)):
        if alice_bases[i] == bob_bases[i]:
            sifted_alice.append(alice_bits[i])
            sifted_bob.append(bob_results[i])

    return sifted_alice, sifted_bob