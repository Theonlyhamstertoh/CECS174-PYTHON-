print(
        f"An earthquake of magnitude {mag1 if mag1 > mag2 else mag2 } is {mag_diff if mag1 > mag2 else 1/mag_diff:.1f} times more powerful than an earthquake of magnitude {mag2 if mag1 > mag2 else mag1 }. "
    )