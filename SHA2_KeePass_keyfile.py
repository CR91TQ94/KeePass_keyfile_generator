import hashlib
import binascii

# Security Warning:
# Using this method to generate KeePass keyfiles can be very 
# dangerous if not used properly. The security of your keyfile 
# relies heavily on the secrecy and strength of your brain-key. 
# If the brain-key is weak or easily guessable, it could lead to
#  someone breaking your keys and gaining unauthorized access 
# to your KeePass database. Always use a strong, unique brain-key 
# and handle the generated keyfile with extreme caution.
# 
# How it works:
# This script will generate a secure keyfile 
# for KeePass using SHA2-256 hashing. Remember 
# to keep your brain-key secure to protect your 
# KeePass database.


# HERE YOU WILL ENTER YOUR PASSWORD/PASSPHRASE, between quotemarks.
# REMEMBER: even 'space', is calculated!
input_text = "password"


# Calculate SHA-256 hash of the input
sha256_hash = hashlib.sha256(input_text.encode('utf-8')).hexdigest()
A = sha256_hash
# Convert SHA-256 hash from HEX to raw
raw_hash = binascii.unhexlify(A)
# Calculate SHA-256 hash of the raw data
sha256_hash = hashlib.sha256(raw_hash).hexdigest()
B = sha256_hash[:8]
# XML document structure
xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<KeyFile>
    <Meta>
        <Version>2.0</Version>
    </Meta>
    <Key>
        <Data Hash="{B}">{A}
        </Data>
    </Key>
</KeyFile>
"""

# Save the XML document as a file with .keyx extension 
# >>>>>>>>>>>>>>>>>> HERE YOU ENTER YOUR FILENAME AS YOU WISH 
# >>>>>>>>>>>>>>>>>> rename it and make more obscure, naming it 
# >>>>>>>>>>>>>>>>>> like x, or 123 or similar.
file_name = "SHA2key.keyx"
with open(file_name, "w") as file:
    file.write(xml_content)
