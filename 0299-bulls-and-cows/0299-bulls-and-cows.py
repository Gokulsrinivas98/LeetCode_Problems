class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # bull = cow = 0
        # s = []
        # for i in range(len(secret)):
        #     if guess[i] == secret[i]:
        #         bull += 1
        #         s.append(i)
        #     # elif guess[i] !=secret[i] and guess[i] in secret and guess[i] not in s:
        #     elif guess[i] !=secret[i] and guess[i] in secret and i not in s:
        #         s.append(i)
        #         cow += 1
        # return str(bull)+"A"+str(cow)+"B"
        bull = sum(guess[i] == secret[i] for i in range(len(secret)))
        cow = collections.Counter(secret) & collections.Counter(guess)
        return str(bull)+"A"+str(sum(cow.values())-bull)+"B"