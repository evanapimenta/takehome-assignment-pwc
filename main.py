def format_simples_address(address: str) -> dict:
    split_address = address.split()
    return {
        split_address[0]: split_address[1]
    }


def format_complex_address(address: str) -> dict:
    split_address = address.split()
    return {
        " ".join(split_address[:-1])
        .replace(",", ""): split_address[-1]
        .replace(",", "")
    }


def format_foreign_address(address: str) -> dict:
    split_address = address.split()

    if "No" in split_address[-2]:
        return {
            " ".join(split_address[:-2]) 
            .replace(",", ""): " ".join(split_address[-2:])
            .replace(",", "")
        }

    elif not split_address[-1].isdigit():
        return {
        " ".join(split_address[1:])
        .replace(",", ""): split_address[0]
        .replace(",", "")
    }
    else:
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
    print("Address with whitespace test (complex test)")
    print(format_complex_address("Rio Branco 23"))  # -> {"Rio Branco": "23"}
    print(format_complex_address("Quirino dos Santos 23b"))  # -> {"Quirino dos Santos": "23b"}
    print("Foreign Address test")
    print(format_foreign_address("4, Rue de la Republique"))  # -> {"Rue de la Republique": "4"}
    print(format_foreign_address("100 Broadway Av"))  # -> {"Broadway Av": "100"}
    print(format_foreign_address("Calle Sagasta, 26"))  # -> {"Calle Sagasta": "26"}
    print(format_foreign_address("Calle 44 No 1991"))  # -> {"Calle 44": "No 1991"}