while True:
    hands = int(input("Enter the number of hands: "))
    total_hand_shakes = hands * (hands - 1) // 2
    print(f"Total hand shakes: {total_hand_shakes}")