# LiuD Lesson Eleven

from LiuD_Main_Gen import Gen_All


LiuD_syntax = '''option.prefix = LiuD
states.skip = space
main = (stmt1 NEWLINE)*
stmt1 := options | stmt | inline
inline = NAME ':=' stmt_value
options := option1 | state1 | basic1
    option1 = 'option.prefix' '=' NAME
    state1 = 'states.skip' '=' NAME
    basic1 = 'basic.' NAME '=' STRING
stmt = NAME '=' stmt_value
stmt_value := multiop | values_or | string_or | jiap | jiad | series
    values_or = NAME ^+ '|'
    string_or = STRING ^+ '|'
    series = value*
    jiap = NAME '^+' STRING
    jiad = NAME '^*' STRING
    multiop = NAME ',' '(,' opstr* ')' NAME
        opstr := litstring | enclosedstrs
        enclosedstrs = '(' STRING* ')'

litname = NAME
litstring = STRING
value1 := litname | litstring | enclosed
    enclosed = '(' stmt_value ')'
value := itemd | itemq | value1
    itemd = value1 '*'
    itemq = value1 '?'
'''
def func1():
    s = Gen_All(liud_syntax)
    print s


syntax_CPP = r'''option.prefix = CPP
    states.skip = crlf
    basic.CSTR = '"[^"\\]*(?:\\.[^"\\]*)*"'

    main = gstmt*

    gstmt := funcdef | declare
        funcdef = datatype NAME '(' params? ')' '{' stmt* '}'
        params = param ^* ','
        param = datatype NAME

    declare0 = datatype newvars
        newvars = declvar ^* ','
    declare = declare0 ';'
    declvar := declvar_array | declvar_assign | litname
        declvar_array = NAME '[' NUMBER ']'
        declvar_assign = NAME '=' value

    stmt_0 := declare0 | assign | augassign | vpp | value
        augassign = dest ('+=' | '-=' | '/=' | '*=') value
        assign = dest '=' value
        dest := dest_array | litname
            dest_array = NAME '[' value ']'
        vpp = NAME ('++' | '--')
    stmt_2 = stmt_0? ';'
    stmt := if_stmt | while_stmt | for_stmt | stmt_2 | return_stmt
        if_stmt = 'if' '(' value ')' block else_part?
            else_part = 'else' block
        while_stmt = 'while' '(' value ')' block
        for_stmt = 'for' '(' stmt_0? ';' value? ';' stmt_0? ')' block
        return_stmt = 'return' value ';'

    block := stmt | enclosedblock
        enclosedblock = '{' stmt* '}'

    datatype = 'int' | 'long'

    value0 = NUMBER | NAME | CSTR
    value1 := enclosed | funccall | array_index | value0
        enclosed = '(' value ')'
        funccall = NAME '(' args? ')'
            args = value ^* ','
        array_index = NAME '[' value ']'
    value2 := signed | value1
        signed = ('-' | '+') value1
    binvalue = value2, (, ('*' '/') ('+' '-') '%' ('>=' '>' '<=' '<' '==' '!=')) value1
    value := binvalue

    litname = NAME
    '''

# stmt* can be 0
# declvar ^* ',' can only one var without ','

sample_CPP = r'''
int main()
{
    int c=2800,f[2801];
    for (int b = 0; b < c; b++)
        f[b] = 10000 / 5;
    f[c] = 0;
    int e = 0;
    while (c != 0) {
        int d = 0;
        int b = c;
        while (1) {
            d += f[b] * 10000;
            f[b] = d % (b * 2 - 1);
            d /= (b * 2 - 1);
            b--;
            if (b == 0)
                break;
            d *= b;
        }
        c -= 14;
        printf("%.4d", e + d / 10000);
        e = d % 10000;
    }
    printf("\n");
    return 0;
}
'''

def func3():
    s = Gen_All(syntax_CPP)
    print s

syntax_Py = r'''option.prefix = PY
    states.skip = no
    stmts = (IDENT stmt)*
    deepstmts = IDENTIN stmts IDENTOUT

    states.skip = space

    main = stmts

    stmt := if_stmt | while_stmt | return_stmt | print_stmt | funcdef | assign | augassign | value
        if_stmt = 'if' value ':' deepstmts else_part?
            else_part = IDENT 'else' ':' deepstmts
        while_stmt = 'while' value ':' deepstmts else_part?
        return_stmt = 'return' value
        funcdef = 'def' NAME '(' params? ')' ':' deepstmts
            params = NAME ^* ','
        augassign = dest ('+=' | '-=' | '/=' | '*=') value
        assign = dest '=' value
        dest := dest_array | litname
            dest_array = NAME '[' value ']'
        print_stmt = 'print' args? ','?
            args = value ^* ','

    value_bool = 'True' | 'False'
    value0 = NUMBER | NAME | STRING
    value1 := enclosed | funccall | array_index | value_bool | value0
        enclosed = '(' value ')'
        funccall = NAME '(' args? ')'
        array_index = NAME '[' value ']'
    value2 := signed | array | value1
        signed = ('-' | '+') value1
        array = '[' args? ','? ']'
    binvalue = value2, (, ('*' '/') ('+' '-') '%' ('>=' '>' '<=' '<' '==' '!=')) value1
    value := binvalue

    litname = NAME
    '''
sample_Python = '''
def main():
    c = 2800
    f = [10000 / 5] * 2801
    f[c] = 0
    e = 0
    while c != 0:
        d = 0
        b = c
        while True:
            d += f[b] * 10000
            f[b] = d % (b * 2 - 1)
            d /= (b * 2 - 1)
            b -= 1
            if b == 0:
                break
            d *= b

        c -= 14
        print '%04d' % (e + d / 10000),
        e = d % 10000

    print

main()
'''

def func5():
    s = Gen_All(syntax_Py)
    print s
    #open('Ast_Py2.py', 'w').write(s)

import unittest
class Test(unittest.TestCase):
    def test1(self):
        s = Gen_All(LiuD_syntax)

        #open('Ast_LiuD2.py', 'w').write(s)
        s2 = open('Ast_LiuD.py').read()
        self.assertEqual(s, s2)

    def test2(self):
        s = Gen_All(syntax_CPP)
        #open('Ast_CPP2.py', 'w').write(s)
        s2 = open('Ast_CPP.py').read()
        self.assertEqual(s, s2)

    def test3(self):
        import Ast_LiuD
        the = Ast_LiuD.LiuD_Parser(LiuD_syntax)
        mod = the.handle_main()

        outp = Ast_LiuD.OutP()
        the2 = Ast_LiuD.LiuD_output(outp)
        mod.walkabout(the2)
        txt = outp.txt
        #print '<%s>' % txt
        txt2 = '''option.prefix = LiuD
states.skip = space
main = ( stmt1 NEWLINE ) *
stmt1 := options | stmt | inline
inline = NAME ':=' stmt_value
options := option1 | state1 | basic1
option1 = 'option.prefix' '=' NAME
state1 = 'states.skip' '=' NAME
basic1 = 'basic.' NAME '=' STRING
stmt = NAME '=' stmt_value
stmt_value := multiop | values_or | string_or | jiap | jiad | series
values_or = NAME ^+ '|'
string_or = STRING ^+ '|'
series = value *
jiap = NAME '^+' STRING
jiad = NAME '^*' STRING
multiop = NAME ',' '(,' opstr * ')' NAME
opstr := litstring | enclosedstrs
enclosedstrs = '(' STRING * ')'
litname = NAME
litstring = STRING
value1 := litname | litstring | enclosed
enclosed = '(' stmt_value ')'
value := itemd | itemq | value1
itemd = value1 '*'
itemq = value1 '?'
'''
        #print '<%s>' % txt2
        #print txt == txt2
        self.assertEqual(txt, txt2)

    def test4(self):
        import Ast_CPP
        the = Ast_CPP.CPP_Parser(sample_CPP)
        the.skipspacecrlf()
        mod = the.handle_main()

        outp = Ast_CPP.OutP()
        the2 = Ast_CPP.CPP_output(outp)
        mod.walkabout(the2)
        txt = outp.txt
        print '<%s>' % txt
        txt2 = r'''int main ( ) { int c = 2800 , f [ 2801 ] ; for ( int b = 0 ; b < c ; b ++ ) f [ b ] = 10000 / 5 ; f [ c ] = 0 ; int e = 0 ; while ( c != 0 ) { int d = 0 ; int b = c ; while ( 1 ) { d += f [ b ] * 10000 ; f [ b ] = d % ( b * 2 - 1 ) ; d /= ( b * 2 - 1 ) ; b -- ; if ( b == 0 ) break ; d *= b ; } c -= 14 ; printf ( "%.4d" , e + d / 10000 ) ; e = d % 10000 ; } printf ( "\n" ) ; return 0 ; }'''
        self.assertEqual(txt, txt2)

    def test5(self):
        s = Gen_All(syntax_Py, True)
        #open('Ast_Py2.py', 'w').write(s)
        s2 = open('Ast_Py.py').read()
        self.assertEqual(s, s2)
        #return

        import Ast_Py
        the = Ast_Py.PY_Parser(sample_Python)
        the.deep()
        mod = the.handle_main()
        last = the.SerialOut()

        stand = [[['main', [], [[[['c', 1], [[[['2800', 0], 4], 2]]], 5], [[['f', 1], [[[[[[[[[['10000', 0], 4], 2]], '/', [[['5', 0], 4]]]], 0], 1]], '*', [[['2801', 0], 4]]]], 5], [[[['f', [[[['c', 1], 4], 2]]], 0], [[[['0', 0], 4], 2]]], 5], [[['e', 1], [[[['0', 0], 4], 2]]], 5], [[[[[[['c', 1], 4], 2]], '!=', [[['0', 0], 4]]], [[[['d', 1], [[[['0', 0], 4], 2]]], 5], [[['b', 1], [[[['c', 1], 4], 2]]], 5], [[[[[0, 3], 2]], [[[['d', 1], 0, [[[[['f', [[[['b', 1], 4], 2]]], 2], 2]], '*', [[['10000', 0], 4]]]], 6], [[[['f', [[[['b', 1], 4], 2]]], 0], [[[[['d', 1], 4], 2]], '%', [[[[[[[['b', 1], 4], 2]], '*', [[['2', 0], 4]]], '-', [[['1', 0], 4]]], 0]]]], 5], [[['d', 1], 2, [[[[[[[[['b', 1], 4], 2]], '*', [[['2', 0], 4]]], '-', [[['1', 0], 4]]], 0], 2]]], 6], [[['b', 1], 1, [[[['1', 0], 4], 2]]], 6], [[[[[[['b', 1], 4], 2]], '==', [[['0', 0], 4]]], [[[[[['break', 1], 4], 2]], 7]], []], 0], [[['d', 1], 3, [[[['b', 1], 4], 2]]], 6]], []], 1], [[['c', 1], 1, [[[['14', 0], 4], 2]]], 6], [[[[[[[["'%04d'", 2], 4], 2]], '%', [[[[[[['e', 1], 4], 2]], '+', [[[['d', 1], 4]], '/', [[['10000', 0], 4]]]], 0]]]], 1], 3], [[['e', 1], [[[[['d', 1], 4], 2]], '%', [[['10000', 0], 4]]]], 5]], []], 1], [[[], 0], 3]]], 4], [[[[['main', []], 1], 2]], 7]]
        if last != stand:
            print last
        self.assertEqual(last, stand)

        the2 = Ast_Py.PY_SerialIn()
        mod2 = the2.handle_main(stand)

        outp = Ast_Py.OutP()
        the2 = Ast_Py.PY_output(outp)
        mod.walkabout(the2)
        txt = outp.txt
        #print '<%s>' % txt
        print txt
        txt2 = '''
def main ( ) :
     c = 2800
     f = [ 10000 / 5 ] * 2801
     f [ c ] = 0
     e = 0
     while c != 0 :
         d = 0
         b = c
         while True :
             d += f [ b ] * 10000
             f [ b ] = d % ( b * 2 - 1 )
             d /= ( b * 2 - 1 )
             b -= 1
             if b == 0 :
                 break
             d *= b
         c -= 14
         print '%04d' % ( e + d / 10000 ) ,
         e = d % 10000
     print
main ( )'''
        self.assertEqual(txt, txt2)

        outp = Ast_Py.OutP()
        the2 = Ast_Py.PY_output(outp)
        mod2.walkabout(the2)
        txt = outp.txt
        self.assertEqual(txt, txt2)

    def test6(self):
        s = Gen_All(syntax_Py, False)
        #open('Ast_Py2.py', 'w').write(s)
        s2 = open('Ast_Py_noserial.py').read()
        self.assertEqual(s, s2)

        s = Gen_All(syntax_Py, True)
        #open('Ast_Py.py', 'w').write(s)
        s2 = open('Ast_Py.py').read()
        self.assertEqual(s, s2)

if __name__ == '__main__':
    #print 'good'
    #func5()
    the = Test(methodName='test2')
    the.test2()
