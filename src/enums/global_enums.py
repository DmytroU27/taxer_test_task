from enum import Enum


class GlobalErrorMessages(Enum):
    COMMON_NAME_ERROR = "Subject common name in the table does not match the common name in the list"
    SUBJECT_CN_ERROR = "Subject common name is incorrect in the table"
    ISSUER_CN_ERROR = "Issuer common name is incorrect in the table"
    VALID_FROM_DATA_ERROR = "Valid from data is incorrect in the table"
    VALID_TILL_DATA_ERROR = "Valid till data is incorrect in the table"

