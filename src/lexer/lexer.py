from errors import errorcodes
from tokens.tokens import Token, TokenType

from sys import exit

class Lexer:
    def __init__(self, filename):
        self.filename = filename
        self.source = open(filename, "r").read()
        self.idx = 0
        self.line = 1
        self.col = 0

    def peek(self):
        return self.source[self.idx] if not self.idx >= len(self.source) else "\0"

    def advance(self):
        if not self.atEnd():
            x = self.peek()
            if x == "\n":
                self.line += 1
                self.col = 0
            else:
                self.col += 1
            self.idx += 1
            return x
        else:
            return "\0"

    def atEnd(self):
        return self.idx >= len(self.source)

    def peekNext(self):
        if not self.atEnd():
            return self.source[self.idx + 1]
        else:
            return "\0"

    def skipWhitespace(self):
        while self.peek() in " \t\r\n":
            self.advance()

    def skipComment(self):
        while self.peek() != "\n":
            self.advance()

    def skipMultiLineComment(self):
        nesting = 1
        while nesting > 0:
            if self.peek() == "*" and self.peekNext() == "/":
                self.advance()
                self.advance()
                nesting -= 1
            elif self.peek() == "/" and self.peekNext() == "*":
                self.advance()
                self.advance()
                nesting += 1
            else:
                self.advance()

    def previous(self):
        if self.idx-1 >= 0:
            return self.source[self.idx-1]
        else:
            return "\0"

    def string(self):
        start = self.idx
        while self.peek() != '"' and not self.atEnd():
            if self.peek() == "\n":
                self.line += 1
                self.col = 0
            self.advance()
        if self.atEnd():
            errorcodes.ErrorCodes.printErrorMessage(errorcodes.ErrorCodes.UNTERMINATED_STRING, [ self.line, self.col ], self.filename, "Consider adding a closing \"")
        self.advance()
        return self.source[start:self.idx]

    def char(self):
        res = ""
        res += self.advance()
        if not self.peek() == "'":
            errorcodes.ErrorCodes.printErrorMessage(errorcodes.ErrorCodes.UNTERMINATED_STRING, [ self.line, self.col ], self.filename, "Consider adding a closing '")

        return res

    def number(self):
        res = ""
        isFloat = False
        while self.peek().isdigit():
            res += self.advance()

        if self.peek() == '.':
            res += self.advance()
            while self.peek().isdigit():
                res += self.advance()
            isFloat = True

        # hexadecimals
        if self.peek().lower() == 'x' and self.prev() == '0':
            res += self.advance()
            while self.peek().isdigit() or self.peek().isalpha():
                res += self.advance()

        # binary
        if self.peek().lower() == 'b' and self.prev() == '0':
            res += self.advance()
            while (self.peek().isdigit() or self.peek().lower() == '0' or self.peek().lower() == '1'):
                res += self.advance()

        return [res, isFloat]

    def identifier(self):
        res = ""
        while self.peek().isalnum() or self.peek() == "_":
            res += self.advance()

        return res

    def lex(self):
        tokens = []
        while not self.atEnd():
            self.skipWhitespace()
            if self.peek() == "/":
                if self.peekNext() == "/":
                    self.skipComment()
                elif self.peekNext() == "*":
                    self.skipMultiLineComment()
                else:
                    if self.peekNext() == "=":
                        tokens.append(Token("/=", TokenType.SLASHEQ, self.line, self.col))
                        self.advance()
                        self.advance()
                    else:
                        tokens.append(Token("/", TokenType.SLASH, self.line, self.col))
                        self.advance()
            elif self.peek() == "*":
                if self.peekNext() == "=":
                    tokens.append(Token("*=", TokenType.STAREQ, self.line, self.col))
                    self.advance()
                    self.advance()
                else:
                    tokens.append(Token("*", TokenType.STAR, self.line, self.col))
                    self.advance()
            elif self.peek() == "+":
                if self.peekNext() == "=":
                    tokens.append(Token("+=", TokenType.PLUSEQ, self.line, self.col))
                    self.advance()
                    self.advance()
                elif self.peekNext() == "+":
                    tokens.append(Token("++", TokenType.PLUSPLUS, self.line, self.col))
                    self.advance()
                    self.advance()
                else:
                    tokens.append(Token("+", TokenType.PLUS, self.line, self.col))
                    self.advance()
            elif self.peek() == "-":
                if self.peekNext() == "=":
                    tokens.append(Token("-=", TokenType.MINUSEQ, self.line, self.col))
                    self.advance()
                    self.advance()
                elif self.peekNext() == "-":
                    tokens.append(Token("--", TokenType.MINUSMINUS, self.line, self.col))
                    self.advance()
                    self.advance()
                else:
                    tokens.append(Token("-", TokenType.MINUS, self.line, self.col))
                    self.advance()
            elif self.peek() == "%":
                if self.peekNext() == "=":
                    tokens.append(Token("%=", TokenType.PERCENTEQ, self.line, self.col))
                    self.advance()
                    self.advance()
                else:
                    tokens.append(Token("%", TokenType.PERCENT, self.line, self.col))
                    self.advance()
            elif self.peek() == "=":
                if self.peekNext() == "=":
                    tokens.append(Token("==", TokenType.EQEQ, self.line, self.col))
                    self.advance()
                    self.advance()
                elif self.peekNext() == ">":
                    tokens.append(Token("=>", TokenType.ARROW, self.line, self.col))
                    self.advance()
                    self.advance()
                else:
                    tokens.append(Token("=", TokenType.EQ, self.line, self.col))
                    self.advance()
            elif self.peek() == "!":
                if self.peekNext() == "=":
                    tokens.append(Token("!=", TokenType.NEQ, self.line, self.col))
                    self.advance()
                    self.advance()
                else:
                    tokens.append(Token("!", TokenType.BANG, self.line, self.col))
                    self.advance()
            elif self.peek() == ">":
                if self.peekNext() == "=":
                    tokens.append(Token(">=", TokenType.GTEQ, self.line, self.col))
                    self.advance()
                    self.advance()
                elif self.peekNext() == ">":
                    if self.source[self.idx+2] == "=":
                        tokens.append(Token(">>=", TokenType.RSHIFTEQ, self.line, self.col))
                        self.advance()
                        self.advance()
                        self.advance()
                else:
                    tokens.append(Token(">", TokenType.GT, self.line, self.col))
                    self.advance()
            elif self.peek() == "<":
                if self.peekNext() == "=":
                    tokens.append(Token("<=", TokenType.LTEQ, self.line, self.col))
                    self.advance()
                    self.advance()
                elif self.peekNext() == "<":
                    if self.source[self.idx+2] == "=":
                        tokens.append(Token("<<=", TokenType.LSHIFTEQ, self.line, self.col))
                        self.advance()
                        self.advance()
                        self.advance()
                else:
                    tokens.append(Token("<", TokenType.LT, self.line, self.col))
                    self.advance()
            elif self.peek() == "&":
                if self.peekNext() == "=":
                    tokens.append(Token("&=", TokenType.AMPERSANDEQ, self.line, self.col))
                    self.advance()
                    self.advance()
                else:
                    tokens.append(Token("&", TokenType.AMPERSAND, self.line, self.col))
                    self.advance()
            elif self.peek() == "|":
                if self.peekNext() == "=":
                    tokens.append(Token("|=", TokenType.PIPEEQ, self.line, self.col))
                    self.advance()
                    self.advance()
                else:
                    tokens.append(Token("|", TokenType.PIPE, self.line, self.col))
                    self.advance()
            elif self.peek() == "^":
                if self.peekNext() == "=":
                    tokens.append(Token("^=", TokenType.CARETEQ, self.line, self.col))
                    self.advance()
                    self.advance()
                else:
                    tokens.append(Token("^", TokenType.CARET, self.line, self.col))
                    self.advance()
            elif self.peek() == "?":
                tokens.append(Token("?", TokenType.QUESTION, self.line, self.col))
                self.advance()
            elif self.peek() == ":":
                tokens.append(Token(":", TokenType.COLON, self.line, self.col))
                self.advance()
            elif self.peek() == ";":
                tokens.append(Token(";", TokenType.SEMICOLON, self.line, self.col))
                self.advance()
            elif self.peek() == ",":
                tokens.append(Token(",", TokenType.COMMA, self.line, self.col))
                self.advance()
            elif self.peek() == ".":
                tokens.append(Token(".", TokenType.DOT, self.line, self.col))
                self.advance()
            elif self.peek() == "(":
                tokens.append(Token("(", TokenType.LPAREN, self.line, self.col))
                self.advance()
            elif self.peek() == ")":
                tokens.append(Token(")", TokenType.RPAREN, self.line, self.col))
                self.advance()
            elif self.peek() == "[":
                tokens.append(Token("[", TokenType.LBRACKET, self.line, self.col))
                self.advance()
            elif self.peek() == "]":
                tokens.append(Token("]", TokenType.RBRACKET, self.line, self.col))
                self.advance()
            elif self.peek() == "{":
                tokens.append(Token("{", TokenType.LBRACE, self.line, self.col))
                self.advance()
            elif self.peek() == "}":
                tokens.append(Token("}", TokenType.RBRACE, self.line, self.col))
                self.advance()
            else:
                if self.peek().isalpha() or self.peek() == "_":
                    identifier = self.identifier()
                    match identifier:
                        case "let":
                            tokens.append(Token(identifier, TokenType.LET, self.line, self.col))
                        case "fn":
                            tokens.append(Token(identifier, TokenType.FN, self.line, self.col))
                        case "return":
                            tokens.append(Token(identifier, TokenType.RETURN, self.line, self.col))
                        case "if":
                            tokens.append(Token(identifier, TokenType.IF, self.line, self.col))
                        case "else":
                            tokens.append(Token(identifier, TokenType.ELSE, self.line, self.col))
                        case "while":
                            tokens.append(Token(identifier, TokenType.WHILE, self.line, self.col))
                        case "for":
                            tokens.append(Token(identifier, TokenType.FOR, self.line, self.col))
                        case "break":
                            tokens.append(Token(identifier, TokenType.BREAK, self.line, self.col))
                        case "continue":
                            tokens.append(Token(identifier, TokenType.CONTINUE, self.line, self.col))
                        case "true":
                            tokens.append(Token(identifier, TokenType.TRUE, self.line, self.col))
                        case "false":
                            tokens.append(Token(identifier, TokenType.FALSE, self.line, self.col))
                        case "null":
                            tokens.append(Token(identifier, TokenType.NULL, self.line, self.col))
                        case "and":
                            tokens.append(Token(identifier, TokenType.AND, self.line, self.col))
                        case "or":
                            tokens.append(Token(identifier, TokenType.OR, self.line, self.col))
                        case "import":
                            tokens.append(Token(identifier, TokenType.IMPORT, self.line, self.col))
                        case "as":
                            tokens.append(Token(identifier, TokenType.AS, self.line, self.col))
                        case "from":
                            tokens.append(Token(identifier, TokenType.FROM, self.line, self.col))
                        case "struct":
                            tokens.append(Token(identifier, TokenType.STRUCT, self.line, self.col))
                        case "enum":
                            tokens.append(Token(identifier, TokenType.ENUM, self.line, self.col))
                        case "trait":
                            tokens.append(Token(identifier, TokenType.TRAIT, self.line, self.col))
                        case "implements":
                            tokens.append(Token(identifier, TokenType.IMPLEMENTS, self.line, self.col))
                        case "new":
                            tokens.append(Token(identifier, TokenType.NEW, self.line, self.col))
                        case "delete":
                            tokens.append(Token(identifier, TokenType.DELETE, self.line, self.col))
                        case "sizeof":
                            tokens.append(Token(identifier, TokenType.SIZEOF, self.line, self.col))
                        case "extern":
                            tokens.append(Token(identifier, TokenType.EXTERN, self.line, self.col))
                        case "type":
                            tokens.append(Token(identifier, TokenType.TYPE, self.line, self.col))
                        case "static":
                            tokens.append(Token(identifier, TokenType.STATIC, self.line, self.col))
                        case "inline":
                            tokens.append(Token(identifier, TokenType.INLINE, self.line, self.col))
                        case "abstract":
                            tokens.append(Token(identifier, TokenType.ABSTRACT, self.line, self.col))
                        case "mut":
                            tokens.append(Token(identifier, TokenType.MUT, self.line, self.col))
                        case _:
                            tokens.append(Token(identifier, TokenType.IDENTIFIER, self.line, self.col))
                elif self.peek().isdigit():
                    num = self.number()
                    if num[1]:
                        tokens.append(
                            Token(num[0], TokenType.FLOAT, self.line, self.col))
                    else:
                        tokens.append(
                            Token(num[0], TokenType.INTEGER, self.line, self.col))
                elif self.peek() == '"':
                    tokens.append(Token(self.string(), TokenType.STRING, self.line, self.col))
                elif self.peek() == "'":
                    tokens.append(Token(self.char(), TokenType.CHAR, self.line, self.col))
                elif self.peek() == "\0":
                    tokens.append(Token("\0", TokenType.EOF, self.line, self.col))
                else:
                    print(self.peek())
                    errorcodes.ErrorCodes.printErrorMessage(errorcodes.ErrorCodes.LEXING_ERROR, [ self.line, self.col ], self.filename)

        return tokens
