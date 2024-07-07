import re

def validateToken(token):
    return bool(re.search("^[01]+$", token))

def deleteSpaces(token):
    return token.replace(" ", "")

def deleteComma(token):
    return token.replace(",", "")

def formatToken(token):
    noSpaceToken = deleteSpaces(token)
    return deleteComma(noSpaceToken)

if __name__ == "__main__":
    token = "1011,010010100110111010,01   110011"
    newToken = formatToken(token)
    k = validateToken(newToken)
    print(newToken)
    print(k)
