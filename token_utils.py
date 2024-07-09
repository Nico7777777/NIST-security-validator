import re


def validateToken(_token: str) -> bool:
    return bool(re.search("^[01]+$", _token))


def deleteSpaces(_token: str) -> str:
    return _token.replace(" ", "")


def deleteComma(_token: str) -> str:
    return _token.replace(",", "")


def formatToken(_token: str) -> str:
    noSpaceToken = deleteSpaces(_token)
    return deleteComma(noSpaceToken)

# Only for testing purposes
# if __name__ == "__main__":
#     _token = "1011,010010100110111010,01   110011"
#     newToken = formatToken(_token)
#     k = validateToken(newToken)
#     print(newToken)
#     print(k)
