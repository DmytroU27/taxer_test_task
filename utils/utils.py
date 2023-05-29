from cryptography import x509
from cryptography.hazmat.backends import default_backend


def parsing_cert(file_name):
    cert_file = f"test_data/{file_name}.cer"
    with open(cert_file, 'rb') as f:
        cert_data = f.read()
    cert = x509.load_der_x509_certificate(cert_data, default_backend())
    subject, issuer = cert.subject, cert.issuer
    subject_cn = subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value
    issuer_cn = issuer.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value
    valid_from, valid_till = cert.not_valid_before, cert.not_valid_after
    return subject_cn, issuer_cn, valid_from, valid_till



