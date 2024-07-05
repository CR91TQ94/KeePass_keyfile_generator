from Crypto.Hash import keccak, SHA256
import binascii

# Textual input
input_text = "abcd"

# Calculate KECCAK-512 hash of the input
keccak_hash = keccak.new(digest_bits=512)
keccak_hash.update(input_text.encode('utf-8'))
A = keccak_hash.hexdigest()

# Convert KECCAK-512 hash from HEX to raw
raw_hash = binascii.unhexlify(A)

# Calculate SHA-256 hash of the raw data
sha256_hash = SHA256.new(raw_hash).hexdigest()
B = sha256_hash[:8]

# XML document structure
xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<KeyFile>
    <Meta>
        <Version>2.0</Version>
    </Meta>
    <Key>
        <Data Hash="{B}">
            {A}
        </Data>
    </Key>
</KeyFile>
"""

# Save the XML document as a file with .keyx extension
file_name = "key.keyx"
with open(file_name, "w") as file:
    file.write(xml_content)
