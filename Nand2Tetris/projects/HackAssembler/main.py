from hackParser import Parser
from code import Code
from symboltable import SymbolTable
import os


def to_bin(value, num):  # 十进制数据，二进制位宽
    bin_chars = ""
    temp = value
    for i in range(num):
        bin_char = bin(temp % 2)[-1]
        temp = temp // 2
        bin_chars = bin_char + bin_chars
    return bin_chars.upper()  # 输出指定位宽的二进制字符串


def executeStepByStep(filePosition):
    toPosition = os.path.splitext(filePosition)[0] + '.hack'
    parser = Parser(filePosition)
    code = Code()
    symbolTable = SymbolTable()
    actualLine = 0
    while parser.hasMoreCommands():
        parser.advance()
        if parser.commandType() == 'L_COMMAND':
            strSymbol = parser.symbol()
            strAddress = str(actualLine)
            symbolTable.addEntry(strSymbol, strAddress)
        else:
            actualLine = actualLine + 1
    parser.currentLine = -1
    parser.currentCommand = None
    serialNumber = 16
    with open(toPosition, mode='a+') as f:
        f.seek(0)
        f.truncate()
        while parser.hasMoreCommands():
            parser.advance()
            if parser.commandType() == 'A_COMMAND':
                mystr = parser.symbol()
                if mystr.isdigit():
                    number = int(mystr)
                    out = '0' + to_bin(number, 15)
                    f.write(out + '\n')
                else:
                    if symbolTable.isContains(mystr):
                        address = symbolTable.getAddress(mystr)
                        number = int(address)
                        out = '0' + to_bin(number, 15)
                        f.write(out + '\n')
                    else:
                        symbolTable.addEntry(mystr, str(serialNumber))
                        out = '0' + to_bin(serialNumber, 15)
                        f.write(out + '\n')
                        serialNumber = serialNumber+1
            elif parser.commandType() == 'C_COMMAND':
                c = parser.comp()
                d = parser.dest()
                j = parser.jump()
                cc = code.comp(c)
                dd = code.dest(d)
                jj = code.jump(j)
                out = '111' + cc + dd + jj
                f.write(out + '\n')
            else:
                pass


if __name__ == '__main__':
    executeStepByStep('E:/HackAssembler/test/max/Max.asm')
