# keep going!
import re


class Parser:
    def __init__(self, pos):
        with open(pos) as f:
            mylist = f.read().splitlines()
            alist = []
        for line in mylist:
            aline = line.split("//", 1)[0]
            alist.append(aline)
        self.fileList = [x.strip() for x in alist if x.strip() != '']
        self.currentLine = -1
        self.currentCommand = None

    def hasMoreCommands(self):
        if self.currentLine + 1 <= len(self.fileList) - 1:
            return True
        else:
            return False

    def advance(self):
        self.currentLine = self.currentLine + 1
        self.currentCommand = self.fileList[self.currentLine]

    def commandType(self):
        if re.match('@', self.currentCommand) is not None:
            return 'A_COMMAND'
        elif re.match('\(', self.currentCommand) is not None:
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'

    def symbol(self):
        if self.commandType() == 'A_COMMAND':
            return self.currentCommand[1:]
        elif self.commandType() == 'L_COMMAND':
            return self.currentCommand[1:-1]
        else:
            return None

    def dest(self):
        if self.commandType() == 'C_COMMAND':
            positionOfEqual = self.currentCommand.find('=')
            if positionOfEqual != -1:
                return self.currentCommand[0:positionOfEqual].replace(" ", "")
            else:
                return 'null'

    def comp(self):
        if self.commandType() == 'C_COMMAND':
            positionOfEqual = self.currentCommand.find('=')
            positionOfsemicolons = self.currentCommand.find(';')
            if positionOfEqual == -1 and positionOfsemicolons == -1:
                return self.currentCommand.replace(" ", "")
            elif positionOfEqual == -1 and positionOfsemicolons != -1:
                return self.currentCommand[0:positionOfsemicolons].replace(" ", "")
            elif positionOfEqual != -1 and positionOfsemicolons == -1:
                return self.currentCommand[positionOfEqual + 1:].replace(" ", "")
            else:
                return self.currentCommand[positionOfEqual + 1:positionOfsemicolons].replace(" ", "")

    def jump(self):
        if self.commandType() == 'C_COMMAND':
            positionOfsemicolons = self.currentCommand.find(';')
            if positionOfsemicolons == -1:
                return 'null'
            else:
                return self.currentCommand[positionOfsemicolons + 1:].replace(" ", "")


if __name__ == '__main__':
    parser = Parser('E:/HackAssembler/test/add/Add.asm')
    print(parser.fileList)
    parser.advance()
    print(parser.currentCommand)
    print(parser.commandType())
    print(parser.dest())
    print(parser.comp())
    print(parser.jump())

