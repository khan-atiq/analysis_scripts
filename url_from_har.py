import json

# Function to extract URIs from a HAR file
def extract_uris_from_har(har_file_path):
    with open(har_file_path, 'r') as f:
        har_data = json.load(f)

    uris = set()

    # Iterate over entries in the HAR file
    for entry in har_data['log']['entries']:
        request = entry['request']
        uri = request['url']
        uris.add(uri)

    return uris

# Example usage
har_file_path = './customer9MaywitWSS.har'
uris = extract_uris_from_har(har_file_path)

# Print the extracted URIs
for uri in uris:
    print(uri)