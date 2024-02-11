def format_simples_address(address: str) -> dict:
    split_address = address.split()
    return {
            " ".join(split_address[:-1])
            .replace(",", ""): split_address[-1]
            .replace(",", "")
        }


if __name__ == "__main__":
    print("Simple test")
    print(format_simples_address("Miritiba 339"))  # -> {"Miritiba": "339"}
    print(format_simples_address("Babaçu 500"))  # -> {"Babaçu": "500"}
    print(format_simples_address("Cambuí 804B"))  # -> {"Cambuí": "804B"}