class ConsonantOrVowel:
    def __init__(self, letIn):
        self.letterInput = f"{letIn.lower()}"

    def consonantOrVowel(self):
        vowels = ('a', 'e', 'i', 'o', 'u')

        if self.letterInput in vowels:
            return "Vowel"
        else:
            return "Consonant"


c = ConsonantOrVowel('A')
print(c.consonantOrVowel())
