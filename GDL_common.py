import re

class Parser00:
    def __init__(self, txt):
        self.txt = txt
        self.pos = 0
        self.identstr = []
    def handle_basic(self, pattn):
        pattn_compiled = re.compile(pattn)
        m = pattn_compiled.match(self.txt, self.pos)
        if m:
            content = m.group()
            self.pos = m.end()
            return content
        return ''
    def handle_NAME(self):
        pattn = '[A-Za-z_][A-Za-z0-9_]*'
        return self.handle_basic(pattn)
    def handle_NUMBER(self):
        pattn = r'0|[1-9]\d*'
        return self.handle_basic(pattn)
    def handle_STRING(self):
        pattn = r"'[^'\\]*(?:\\.[^'\\]*)*'"
        return self.handle_basic(pattn)
    def handle_NEWLINE(self):
        pattn = r"\n[\n \t]*"
        pattn_compiled = re.compile(pattn)
        m = pattn_compiled.match(self.txt, self.pos)
        if m:
            content = m.group()
            self.pos = m.end()
            return content
        return None
    def skip_ident_str(self):
        s = ''
        while self.pos < len(self.txt):
            c = self.txt[self.pos]
            if c in ' \t':
                self.pos += 1
                s += c
            else:
                break
        return s
    def handle_IDENT(self):
        txt = self.txt[self.pos:self.pos+10]
        savepos = self.pos
        havenl = False
        while True:
            s = self.skip_ident_str()
            if self.pos < len(self.txt) and self.txt[self.pos] == '\n':
                self.pos += 1
                havenl = True
                continue
            break
        if savepos > 0 and not havenl:
            self.restorepos(savepos)
            return False

        if not s:
            if self.identstr:
                self.restorepos(savepos)
                return False
            return True
        if not self.identstr:
            self.restorepos(savepos)
            return False
        if s == self.identstr[-1]:
            return True
        self.restorepos(savepos)
        return False
    def handle_IDENTIN(self):
        txt = self.txt[self.pos:self.pos+10]
        savepos = self.pos
        sav2 = -1
        while True:
            s = self.skip_ident_str()
            if self.pos < len(self.txt) and self.txt[self.pos] == '\n':
                sav2 = self.pos
                self.pos += 1
                continue
            break
        if sav2 == -1:
            self.restorepos(savepos)
            return False
        self.restorepos(sav2)
        if not s:
            self.restorepos(savepos)
            return False
        if not self.identstr:
            self.identstr.append(s)
            return True
        last = self.identstr[-1]
        if len(s) > len(last) and s.startswith(last):
            self.identstr.append(s)
            return True
        self.restorepos(savepos)
        return False
    def handle_IDENTOUT(self):
        txt = self.txt[self.pos:self.pos+20]
        if not self.identstr:
            return False
        savepos = self.pos
        sav2 = -1
        while True:
            s = self.skip_ident_str()
            if self.pos < len(self.txt) and self.txt[self.pos] == '\n':
                sav2 = self.pos
                self.pos += 1
                continue
            break
        if sav2 == -1:
            self.restorepos(savepos)
            return False
        self.restorepos(sav2)
        if not s:
            self.identstr.pop()
            return True
        for last in self.identstr[:-1]:
            if last == s:
                self.identstr.pop()
                return True
        self.restorepos(savepos)
        return False
    def handle_str(self, s):
        if self.txt[self.pos:].startswith(s):
            self.pos += len(s)
            return s
        return ''
    def restorepos(self, pos):
        self.pos = pos
    def skipspace(self):
        while self.pos < len(self.txt) and self.txt[self.pos] in ' \t':
            self.pos += 1
    def skipspacecrlf(self):
        while self.pos < len(self.txt) and self.txt[self.pos] in ' \n':
            self.pos += 1

class OutP:
    def __init__(self):
        self.txt = ''
        self.ntab = 0
    def puts(self, s):
        #print s,
        if self.txt != '' and self.txt[-1] != '\n':
            self.txt += ' '
        self.txt += s
    def newline(self):
        #print
        self.txt += '\n'
    def ident(self):
        self.newline()
        self.txt += '    ' * self.ntab
    def identin(self):
        self.ntab += 1
    def identout(self):
        self.ntab -= 1

class Serial00:
    def __init__(self):
        self.last = []
        self.levels = []
    def SerialOut(self):
        return self.last[0]
    def deep(self):
        v = self.last
        self.last = []
        v.append(self.last)
        self.levels.append(self.last)
    def deep1(self):
        v = self.last
        v1 = v.pop()
        self.last = [777, v1]
        v.append(self.last)
        self.levels.append(self.last)
    def up(self):
        last = self.levels.pop()
        for v in last:
            assert v is not None
        self.last = self.levels[-1]
        if last and last[0] == 777:
            last.pop(0)
    def upn(self, n):
        last = self.levels.pop()
        for v in last:
            assert v is not None
        self.last = self.levels[-1]
        if last and last[0] == 777:
            last.pop(0)
        assert n == len(last)
    def upfail(self):
        last = self.levels.pop()
        self.last = self.levels[-1]
        last1 = self.last.pop()
        assert last is last1
        if last and last[0] == 777:
            self.last.append(last[1])

class DbgTrace:
    def __init__(self):
        self.lst = []
    def deepin(self, s):
        print '  ' * len(self.lst) + s + '->'
        self.lst.append(s)
    def errorout(self):
        s = self.lst.pop()
        print '  ' * len(self.lst) + s + '<-error'
    def success(self):
        s = self.lst.pop()
        print '  ' * len(self.lst) + s + '<-'

