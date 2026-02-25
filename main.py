from bb84 import generate_raw_key, sift_key
from error_correction import simple_error_correction
from privacy_amplification import privacy_amplification

def main():
    key_length = 20

    print("---- BB84 QKD Simulation ----\n")

    # Step 1: Raw Key Generation
    alice_bits, alice_bases, bob_bases, bob_results = generate_raw_key(key_length)

    print("Alice Bits:     ", alice_bits)
    print("Alice Bases:    ", alice_bases)
    print("Bob Bases:      ", bob_bases)
    print("Bob Results:    ", bob_results)

    # Step 2: Basis Sifting
    sifted_alice, sifted_bob = sift_key(alice_bits, alice_bases, bob_bases, bob_results)

    print("\nSifted Alice Key:", sifted_alice)
    print("Sifted Bob Key:  ", sifted_bob)

    # Step 3: Error Correction
    corrected_key = simple_error_correction(sifted_alice, sifted_bob)

    print("\nCorrected Key:  ", corrected_key)

    # Step 4: Privacy Amplification
    final_key = privacy_amplification(corrected_key)

    print("\nFinal Secure Key (Hashed):", final_key)

if __name__ == "__main__":
    main()