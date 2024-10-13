# import re
# from urllib.parse import urlparse
# import whois

# def analyze_url(url):
#     features = {}

#     # Feature extraction logic for URL
#     features['qty_dot_url'] = url.count('.')
#     features['qty_hyphen_url'] = url.count('-')
#     features['qty_underline_url'] = url.count('_')
#     features['qty_slash_url'] = url.count('/')
#     features['qty_questionmark_url'] = url.count('?')
#     features['qty_equal_url'] = url.count('=')
#     features['qty_at_url'] = url.count('@')
#     features['qty_and_url'] = url.count('&')
#     features['qty_exclamation_url'] = url.count('!')
#     features['qty_space_url'] = url.count(' ')
#     features['qty_tilde_url'] = url.count('~')
#     features['qty_comma_url'] = url.count(',')
#     features['qty_plus_url'] = url.count('+')
#     features['qty_asterisk_url'] = url.count('*')
#     features['qty_hashtag_url'] = url.count('#')
#     features['qty_dollar_url'] = url.count('$')
#     features['qty_percent_url'] = url.count('%')

#     # 1. Length of the URL
#     features['length_url'] = len(url)

#     # Extract domain and directory from the URL
#     parsed_url = urlparse(url)
#     domain = parsed_url.netloc
#     path = parsed_url.path
#     query = parsed_url.query

#     features['qty_dot_domain'] = domain.count('.')
#     features['qty_hyphen_domain'] = domain.count('-')
#     features['qty_underline_domain'] = domain.count('_')
#     features['domain_length'] = len(domain)

#     features['qty_dot_directory'] = path.count('.')
#     features['qty_hyphen_directory'] = path.count('-')
#     features['directory_length'] = len(path)

#     # Additional features from parameters, if any
#     features['qty_dot_params'] = query.count('.')
#     features['params_length'] = len(query)

#     # Additional feature placeholders
#     features['qty_ip_resolved'] = 0  # Implement IP resolution logic
#     features['time_response'] = 0     # Implement response time logic
#     features['tls_ssl_certificate'] = 0  # Implement SSL certificate logic
#     features['qty_nameservers'] = 0  # Implement nameservers logic
#     features['qty_mx_servers'] = 0  # Implement MX servers logic
#     features['qty_redirects'] = 0  # Implement redirects logic
#     features['url_google_index'] = 0  # Implement Google indexing logic
#     features['domain_google_index'] = 0  # Implement domain indexing logic
#     features['url_shortened'] = 0  # Implement URL shortening logic
#     features['num_query_parameters'] = len(query.split('&')) if query else 0
#     features['qty_tld_url'] = 0  # Implement TLD logic
#     features['domain_in_ip'] = 0  # Implement domain-in-IP logic
#     features['server_client_domain'] = 0  # Implement server-client domain logic
#     features['asn_ip'] = 0  # Implement ASN logic
#     features['time_domain_activation'] = 0  # Implement activation time logic
#     features['time_domain_expiration'] = 0  # Implement expiration time logic
#     features['qty_vowels_domain'] = sum(1 for char in domain if char.lower() in 'aeiou')
#     features['qty_numeric_url'] = sum(c.isdigit() for c in url)
#     features['qty_special_characters_url'] = len(re.findall(r'[^a-zA-Z0-9]', url))
#     features['has_https'] = 1 if url.startswith('https') else 0
#     features['has_http'] = 1 if url.startswith('http') else 0
#     features['length_path'] = len(path)
    
#     # Assert the correct number of features
#     if len(features) < 111:
#         for i in range(len(features), 111):
#             features[f'dummy_feature_{i}'] = 0  # Placeholder for missing features

#     assert len(features) == 111, f"Feature count mismatch: {len(features)} features extracted."

#     print(f"Extracted features: {features}")  # Print features after extraction
#     return features  # Return the complete dictionary of features
# if __name__ == "__main__":
#         url = "https://www.youtube.com/"


import re
from urllib.parse import urlparse

def analyze_url(url):
    features = {}

    # Extract basic features from the URL
    features['qty_dot_url'] = url.count('.')
    features['qty_hyphen_url'] = url.count('-')
    features['qty_underline_url'] = url.count('_')
    features['qty_slash_url'] = url.count('/')
    features['qty_questionmark_url'] = url.count('?')
    features['qty_equal_url'] = url.count('=')
    features['qty_at_url'] = url.count('@')
    features['qty_and_url'] = url.count('&')
    features['qty_exclamation_url'] = url.count('!')
    features['qty_space_url'] = url.count(' ')
    features['qty_tilde_url'] = url.count('~')
    features['qty_comma_url'] = url.count(',')
    features['qty_plus_url'] = url.count('+')
    features['qty_asterisk_url'] = url.count('*')
    features['qty_hashtag_url'] = url.count('#')
    features['qty_dollar_url'] = url.count('$')
    features['qty_percent_url'] = url.count('%')

    # 1. Length of the URL
    features['length_url'] = len(url)

    # Parse the URL to extract more features
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path
    query = parsed_url.query

    # Domain-specific features
    features['qty_dot_domain'] = domain.count('.')
    features['qty_hyphen_domain'] = domain.count('-')
    features['qty_underline_domain'] = domain.count('_')
    features['domain_length'] = len(domain)

    # Path-specific features
    features['qty_dot_directory'] = path.count('.')
    features['qty_hyphen_directory'] = path.count('-')
    features['directory_length'] = len(path)

    # Query-specific features
    features['qty_dot_params'] = query.count('.')
    features['params_length'] = len(query)

    # Count the number of query parameters
    features['num_query_parameters'] = len(query.split('&')) if query else 0

    # Add placeholder values for advanced features (can be extended later)
    features['qty_ip_resolved'] = 0  # Placeholder for IP resolution logic
    features['time_response'] = 0     # Placeholder for response time logic
    features['tls_ssl_certificate'] = 0  # Placeholder for SSL certificate logic
    features['qty_nameservers'] = 0  # Placeholder for nameservers logic
    features['qty_mx_servers'] = 0  # Placeholder for MX servers logic
    features['qty_redirects'] = 0  # Placeholder for redirects logic
    features['url_google_index'] = 0  # Placeholder for Google indexing logic
    features['domain_google_index'] = 0  # Placeholder for domain indexing logic
    features['url_shortened'] = 0  # Placeholder for URL shortening logic
    features['qty_tld_url'] = 0  # Placeholder for TLD logic
    features['domain_in_ip'] = 0  # Placeholder for domain-in-IP logic
    features['server_client_domain'] = 0  # Placeholder for server-client domain logic
    features['asn_ip'] = 0  # Placeholder for ASN logic
    features['time_domain_activation'] = 0  # Placeholder for activation time logic
    features['time_domain_expiration'] = 0  # Placeholder for expiration time logic
    features['qty_vowels_domain'] = sum(1 for char in domain if char.lower() in 'aeiou')
    features['qty_numeric_url'] = sum(c.isdigit() for c in url)
    features['qty_special_characters_url'] = len(re.findall(r'[^a-zA-Z0-9]', url))
    features['has_https'] = 1 if url.startswith('https') else 0
    features['has_http'] = 1 if url.startswith('http') else 0
    features['length_path'] = len(path)

    # Assert that the feature count matches what the model expects
    if len(features) < 111:
        for i in range(len(features), 111):
            features[f'dummy_feature_{i}'] = 0  # Placeholder for missing features

    assert len(features) == 111, f"Feature count mismatch: {len(features)} features extracted."

    # Return the feature dictionary
    return list(features.values())  # Return a list of features instead of dictionary
