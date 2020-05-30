class Tries:

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        current_node = self.root
        for letters in word:
            if letters not in current_node:
                # create a new dictionary aka child of it
                # assign the dictionary to the previous dictionary aka parent
                current_node[letters]={}

            #move pointer down to node
            current_node = current_node[letters]

        #mark the end of word
        current_node["*"] = "*"

    def checkForWord(self,word):
        current_node = self.root
        # checks one child to the next child
        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]

        #basically check if ‘*’ is at the end. if not it will return false
        return "*" in current_node
