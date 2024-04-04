def en_katt(namn: str) -> str:
    return f"Det var en katt som hette {namn}"


if __name__ == '__main__':
    katten: str = en_katt("Greta")
    print(katten)
    # en_katt(17)
