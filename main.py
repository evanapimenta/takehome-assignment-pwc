def format_address(address: str) -> dict:

    split_address = address.split()

    if "No" in split_address[-2]:
        return {
        " ".join(split_address[:-2]) 
        .replace(",", ""): " ".join(split_address[-2:])
        .replace(",", "")
        }

    elif split_address[-1][0].isdigit():
        return {
        " ".join(split_address[:-1])
        .replace(",", ""): split_address[-1]
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