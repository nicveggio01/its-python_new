def is_valid_ipv4(address: str) -> bool:
    parts = address.split(".")

    if len(parts) !=4: 
        return False
    
    for p in parts:

        if not p.isdigit():
            return False
        
        if len(p)>1 and p.startswith("0"):
            return False
        numero= int(p)
        if numero < 0 or numero > 255:
            return False
    
    return True

print(is_valid_ipv4("255.255.255.255") )

        
        
