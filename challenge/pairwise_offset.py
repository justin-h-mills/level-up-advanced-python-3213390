def pairwise_offset(sequence: list[any], fillvalue: str = '*', offset: int = 0) -> list[tuple[any, any]]:
    # Create lists for padding with the specified fill value and concatenate with the original sequence
    top = list(sequence) + [fillvalue] * offset
    bottom = [fillvalue] * offset + list(sequence)

    # Pair the elements of the top and bottom lists and return as a list of tuples
    return list(zip(top, bottom))