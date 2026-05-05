def calculate_statistics(numbers):
    """Calcula estatísticas básicas de uma lista de números.

    Args:
        numbers (list[float] | list[int]): Lista de valores numéricos.

    Returns:
        tuple[float, float, float, float]: Tupla contendo o total, a média, o valor máximo e o valor mínimo.

    Raises:
        ValueError: Se a lista estiver vazia.
    """
    if not numbers:
        raise ValueError("A lista não pode estar vazia.")

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


# Example usage
data = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total, media, maior, menor = calculate_statistics(data)

print("total:", total)
print("media:", media)
print("maior:", maior)
print("menor:", menor)
