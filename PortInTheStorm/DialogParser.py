class CharacterItem:
    def __init__(self, left_character, right_character):
        self.left_character = left_character
        self.right_character = right_character
        self.type = "Character"

class DialogItem:
    def __init__(self, text):
        self.text = text
        self.type = "Dialog"

def Parse(filename):
    cmd_lst = []
    with open(filename) as f:
        for line in f:
            if len(line) == 0:
                continue
            if line[0] == ';':
                splitln = list(filter(None, line[1:].split(" ")))

                if len(splitln) == 2:
                    character_cmd = CharacterItem(splitln[0], splitln[1])
                    cmd_lst.append(character_cmd)
                else:
                    raise MyAssertError("invalid parsing for file character sprites")
            else:
                cmd_lst.append(DialogItem(line))
    return cmd_lst