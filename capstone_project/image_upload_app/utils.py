import uuid

def generate_reference_number(ref_length):
    # Generate a UUID version 4 and return the hex representation
    return str(uuid.uuid4()).upper().replace('-', '')[:ref_length]  # Adjust length as needed
