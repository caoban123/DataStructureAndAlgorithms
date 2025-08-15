def dequy(s,wordDict,word):
    if len(word) > len(s):
        return False
    if word == s:
        return True
    for i in wordDict:
        if dequy(s,wordDict,word + i):
            return True
    return False
# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
print(dequy(s,wordDict,""))