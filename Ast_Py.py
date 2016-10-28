# auto generated

# LiuD syntax :

# option.prefix = PY
#     states.skip = no
#     stmts = (IDENT stmt)*
#     deepstmts = IDENTIN stmts IDENTOUT
# 
#     states.skip = space
# 
#     main = stmts
# 
#     stmt := if_stmt | while_stmt | return_stmt | print_stmt | funcdef | assign | augassign | value
#         if_stmt = 'if' value ':' deepstmts else_part?
#             else_part = IDENT 'else' ':' deepstmts
#         while_stmt = 'while' value ':' deepstmts else_part?
#         return_stmt = 'return' value
#         funcdef = 'def' NAME '(' params? ')' ':' deepstmts
#             params = NAME ^* ','
#         augassign = dest ('+=' | '-=' | '/=' | '*=') value
#         assign = dest '=' value
#         dest := dest_array | litname
#             dest_array = NAME '[' value ']'
#         print_stmt = 'print' args? ','?
#             args = value ^* ','
# 
#     value_bool = 'True' | 'False'
#     value0 = NUMBER | NAME | STRING
#     value1 := enclosed | funccall | array_index | value_bool | value0
#         enclosed = '(' value ')'
#         funccall = NAME '(' args? ')'
#         array_index = NAME '[' value ']'
#     value2 := signed | array | value1
#         signed = ('-' | '+') value1
#         array = '[' args? ','? ']'
#     binvalue = value2, (, ('*' '/') ('+' '-') '%' ('>=' '>' '<=' '<' '==' '!=')) value1
#     value := binvalue
# 
#     litname = NAME
#     

from GDL_common import *

class PY_stmts:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_stmts(self)

class PY_deepstmts:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_deepstmts(self)

class PY_main:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_main(self)

class PY_if_stmt:
    def __init__(self, v1, v2, vq):
        self.v1 = v1
        self.v2 = v2
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_if_stmt(self)

class PY_else_part:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_else_part(self)

class PY_while_stmt:
    def __init__(self, v1, v2, vq):
        self.v1 = v1
        self.v2 = v2
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_while_stmt(self)

class PY_return_stmt:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_return_stmt(self)

class PY_funcdef:
    def __init__(self, s, vq, v):
        self.s = s
        self.vq = vq
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_funcdef(self)

class PY_params:
    def __init__(self, slst):
        self.slst = slst
    def walkabout(self, visitor):
        return visitor.visit_params(self)

class PY_augassign:
    def __init__(self, v1, s, v2):
        self.v1 = v1
        self.s = s
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_augassign(self)

class PY_assign:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_assign(self)

class PY_dest_array:
    def __init__(self, s, v):
        self.s = s
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_dest_array(self)

class PY_print_stmt:
    def __init__(self, vq, sq):
        self.vq = vq
        self.sq = sq
    def walkabout(self, visitor):
        return visitor.visit_print_stmt(self)

class PY_args:
    def __init__(self, vlst):
        self.vlst = vlst
    def walkabout(self, visitor):
        return visitor.visit_args(self)

class PY_value_bool:
    def __init__(self, s):
        self.s = s
    def walkabout(self, visitor):
        return visitor.visit_value_bool(self)

class PY_value0:
    def __init__(self, s):
        self.s = s
    def walkabout(self, visitor):
        return visitor.visit_value0(self)

class PY_enclosed:
    def __init__(self, v):
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_enclosed(self)

class PY_funccall:
    def __init__(self, s, vq):
        self.s = s
        self.vq = vq
    def walkabout(self, visitor):
        return visitor.visit_funccall(self)

class PY_array_index:
    def __init__(self, s, v):
        self.s = s
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_array_index(self)

class PY_signed:
    def __init__(self, s, v):
        self.s = s
        self.v = v
    def walkabout(self, visitor):
        return visitor.visit_signed(self)

class PY_array:
    def __init__(self, vq, sq):
        self.vq = vq
        self.sq = sq
    def walkabout(self, visitor):
        return visitor.visit_array(self)

class PY_binvalue:
    def __init__(self, v1, s, v2):
        self.v1 = v1
        self.s = s
        self.v2 = v2
    def walkabout(self, visitor):
        return visitor.visit_binvalue(self)

class PY_litname:
    def __init__(self, s):
        self.s = s
    def walkabout(self, visitor):
        return visitor.visit_litname(self)

class PY_Parser(Parser00, Serial00):
    def __init__(self, txt):
        Parser00.__init__(self, txt)
        Serial00.__init__(self)
    def handle_NUMBER(self):
        s = Parser00.handle_NUMBER(self)
        if s:
            self.last.append(s)
        return s
    def handle_NAME(self):
        s = Parser00.handle_NAME(self)
        if s:
            self.last.append(s)
        return s
    def handle_STRING(self):
        s = Parser00.handle_STRING(self)
        if s:
            self.last.append(s)
        return s

    def handle_stmts(self):
        vlst = []
        savpos = self.pos
        self.deep()
        while True:
            if not self.handle_IDENT():
                break
            v = self.hdl_stmt()
            if not v:
                break
            vlst.append(v)
            savpos = self.pos
        self.restorepos(savpos)
        if not vlst:
            self.upfail()
            return None
        self.up()
        return PY_stmts(vlst)

    def handle_deepstmts(self):
        savpos = self.pos
        if not self.handle_IDENTIN():
            return None
        v = self.handle_stmts()
        if not v:
            return self.restorepos(savpos)
        if not self.handle_IDENTOUT():
            return self.restorepos(savpos)
        return PY_deepstmts(v)

    def handle_main(self):
        v = self.handle_stmts()
        if not v:
            return None
        return PY_main(v)

    def hdl_stmt(self):
        self.deep()
        no_ = 0
        v = self.handle_if_stmt()
        if not v:
            no_ += 1
            v = self.handle_while_stmt()
        if not v:
            no_ += 1
            v = self.handle_return_stmt()
        if not v:
            no_ += 1
            v = self.handle_print_stmt()
        if not v:
            no_ += 1
            v = self.handle_funcdef()
        if not v:
            no_ += 1
            v = self.handle_assign()
        if not v:
            no_ += 1
            v = self.handle_augassign()
        if not v:
            no_ += 1
            v = self.hdl_value()
        if not v:
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        return v

    def handle_if_stmt(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('if'):
            self.upfail()
            return None
        self.skipspace()
        v1 = self.hdl_value()
        if not v1:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(':'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v2 = self.handle_deepstmts()
        if not v2:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        vq = self.handle_else_part()
        if not vq:
            self.last.append([])
        self.upn(3)
        return PY_if_stmt(v1, v2, vq)

    def handle_else_part(self):
        savpos = self.pos
        if not self.handle_IDENT():
            return None
        self.skipspace()
        if not self.handle_str('else'):
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(':'):
            return self.restorepos(savpos)
        self.skipspace()
        v = self.handle_deepstmts()
        if not v:
            return self.restorepos(savpos)
        return PY_else_part(v)

    def handle_while_stmt(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('while'):
            self.upfail()
            return None
        self.skipspace()
        v1 = self.hdl_value()
        if not v1:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(':'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v2 = self.handle_deepstmts()
        if not v2:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        vq = self.handle_else_part()
        if not vq:
            self.last.append([])
        self.upn(3)
        return PY_while_stmt(v1, v2, vq)

    def handle_return_stmt(self):
        savpos = self.pos
        if not self.handle_str('return'):
            return None
        self.skipspace()
        v = self.hdl_value()
        if not v:
            return self.restorepos(savpos)
        return PY_return_stmt(v)

    def handle_funcdef(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('def'):
            self.upfail()
            return None
        self.skipspace()
        s = self.handle_NAME()
        if not s:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str('('):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        vq = self.handle_params()
        if not vq:
            self.last.append([])
        self.skipspace()
        if not self.handle_str(')'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(':'):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v = self.handle_deepstmts()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.upn(3)
        return PY_funcdef(s, vq, v)

    def handle_params(self):
        self.deep()
        s = self.handle_NAME()
        if not s:
            self.upfail()
            return None
        savpos = self.pos
        slst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.handle_NAME()
            if not s:
                break
            slst.append(s)
            savpos = self.pos
        self.up()
        self.restorepos(savpos)
        return PY_params(slst)

    def handle_augassign(self):
        self.deep()
        savpos = self.pos
        v1 = self.hdl_dest()
        if not v1:
            self.upfail()
            return None
        self.skipspace()
        no_ = 0
        s = self.handle_str('+=')
        if not s:
            no_ += 1
            s = self.handle_str('-=')
        if not s:
            no_ += 1
            s = self.handle_str('/=')
        if not s:
            no_ += 1
            s = self.handle_str('*=')
        if not s:
            self.upfail()
            return self.restorepos(savpos)
        self.last.append(no_)
        self.skipspace()
        v2 = self.hdl_value()
        if not v2:
            self.upfail()
            return self.restorepos(savpos)
        self.upn(3)
        return PY_augassign(v1, s, v2)

    def handle_assign(self):
        self.deep()
        savpos = self.pos
        v1 = self.hdl_dest()
        if not v1:
            self.upfail()
            return None
        self.skipspace()
        if not self.handle_str('='):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v2 = self.hdl_value()
        if not v2:
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_assign(v1, v2)

    def hdl_dest(self):
        self.deep()
        no_ = 0
        v = self.handle_dest_array()
        if not v:
            no_ += 1
            v = self.handle_litname()
        if not v:
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        return v

    def handle_dest_array(self):
        self.deep()
        savpos = self.pos
        s = self.handle_NAME()
        if not s:
            self.upfail()
            return None
        self.skipspace()
        if not self.handle_str('['):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v = self.hdl_value()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(']'):
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_dest_array(s, v)

    def handle_print_stmt(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('print'):
            self.upfail()
            return None
        self.skipspace()
        vq = self.handle_args()
        if not vq:
            self.last.append([])
        self.skipspace()
        sq = self.handle_str(',')
        self.last.append(1 if sq else 0)
        self.upn(2)
        return PY_print_stmt(vq, sq)

    def handle_args(self):
        self.deep()
        s = self.hdl_value()
        if not s:
            self.upfail()
            return None
        savpos = self.pos
        vlst = [s]
        while True:
            self.skipspace()
            if not self.handle_str(','):
                break
            self.skipspace()
            s = self.hdl_value()
            if not s:
                break
            vlst.append(s)
            savpos = self.pos
        self.up()
        self.restorepos(savpos)
        return PY_args(vlst)

    def handle_value_bool(self):
        no_ = 0
        s = self.handle_str('True')
        if not s:
            no_ += 1
            s = self.handle_str('False')
        if not s:
            return None
        self.last.append(no_)
        return PY_value_bool(s)

    def handle_value0(self):
        self.deep()
        no_ = 0
        s = self.handle_NUMBER()
        if not s:
            no_ += 1
            s = self.handle_NAME()
        if not s:
            no_ += 1
            s = self.handle_STRING()
        if not s:
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        return PY_value0(s)

    def hdl_value1(self):
        self.deep()
        no_ = 0
        v = self.handle_enclosed()
        if not v:
            no_ += 1
            v = self.handle_funccall()
        if not v:
            no_ += 1
            v = self.handle_array_index()
        if not v:
            no_ += 1
            v = self.handle_value_bool()
        if not v:
            no_ += 1
            v = self.handle_value0()
        if not v:
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        return v

    def handle_enclosed(self):
        savpos = self.pos
        if not self.handle_str('('):
            return None
        self.skipspace()
        v = self.hdl_value()
        if not v:
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(')'):
            return self.restorepos(savpos)
        return PY_enclosed(v)

    def handle_funccall(self):
        self.deep()
        savpos = self.pos
        s = self.handle_NAME()
        if not s:
            self.upfail()
            return None
        self.skipspace()
        if not self.handle_str('('):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        vq = self.handle_args()
        if not vq:
            self.last.append([])
        self.skipspace()
        if not self.handle_str(')'):
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_funccall(s, vq)

    def handle_array_index(self):
        self.deep()
        savpos = self.pos
        s = self.handle_NAME()
        if not s:
            self.upfail()
            return None
        self.skipspace()
        if not self.handle_str('['):
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        v = self.hdl_value()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.skipspace()
        if not self.handle_str(']'):
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_array_index(s, v)

    def hdl_value2(self):
        self.deep()
        no_ = 0
        v = self.handle_signed()
        if not v:
            no_ += 1
            v = self.handle_array()
        if not v:
            no_ += 1
            v = self.hdl_value1()
        if not v:
            self.upfail()
            return None
        self.last.append(no_)
        self.upn(2)
        return v

    def handle_signed(self):
        self.deep()
        savpos = self.pos
        no_ = 0
        s = self.handle_str('-')
        if not s:
            no_ += 1
            s = self.handle_str('+')
        if not s:
            self.upfail()
            return None
        self.last.append(no_)
        self.skipspace()
        v = self.hdl_value1()
        if not v:
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_signed(s, v)

    def handle_array(self):
        self.deep()
        savpos = self.pos
        if not self.handle_str('['):
            self.upfail()
            return None
        self.skipspace()
        vq = self.handle_args()
        if not vq:
            self.last.append([])
        self.skipspace()
        sq = self.handle_str(',')
        self.last.append(1 if sq else 0)
        self.skipspace()
        if not self.handle_str(']'):
            self.upfail()
            return self.restorepos(savpos)
        self.upn(2)
        return PY_array(vq, sq)

    def handle_binvalue(self):
        self.deep()
        v1 = self.hdl_value2()
        if not v1:
            self.upfail()
            return None
        self.upn(1)
        def multiop1(v1):
            while True:
                self.deep1()
                savpos = self.pos
                self.skipspace()
                for s in ['*', '/']:
                    if self.handle_str(s):
                        break
                else:
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.last.append(s)
                self.skipspace()
                self.deep()
                v2 = self.hdl_value1()
                if not v2:
                    self.upfail()
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.upn(1)
                self.upn(3)
                v1 = PY_binvalue(v1, s, v2)
        def multiop2(v1):
            v1 = multiop1(v1)
            while True:
                self.deep1()
                savpos = self.pos
                self.skipspace()
                for s in ['+', '-']:
                    if self.handle_str(s):
                        break
                else:
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.last.append(s)
                self.skipspace()
                self.deep()
                v2 = self.hdl_value1()
                if not v2:
                    self.upfail()
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.upn(1)
                v2 = multiop1(v2)
                self.upn(3)
                v1 = PY_binvalue(v1, s, v2)
        def multiop3(v1):
            v1 = multiop2(v1)
            while True:
                self.deep1()
                savpos = self.pos
                self.skipspace()
                for s in ['%']:
                    if self.handle_str(s):
                        break
                else:
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.last.append(s)
                self.skipspace()
                self.deep()
                v2 = self.hdl_value1()
                if not v2:
                    self.upfail()
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.upn(1)
                v2 = multiop2(v2)
                self.upn(3)
                v1 = PY_binvalue(v1, s, v2)
        def multiop4(v1):
            v1 = multiop3(v1)
            while True:
                self.deep1()
                savpos = self.pos
                self.skipspace()
                for s in ['>=', '>', '<=', '<', '==', '!=']:
                    if self.handle_str(s):
                        break
                else:
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.last.append(s)
                self.skipspace()
                self.deep()
                v2 = self.hdl_value1()
                if not v2:
                    self.upfail()
                    self.upfail()
                    self.restorepos(savpos)
                    return v1
                self.upn(1)
                v2 = multiop3(v2)
                self.upn(3)
                v1 = PY_binvalue(v1, s, v2)
        return multiop4(v1)

    def hdl_value(self):
        v = self.handle_binvalue()
        if not v:
            return None
        return v

    def handle_litname(self):
        s = self.handle_NAME()
        if not s:
            return None
        return PY_litname(s)

class PY_output:
    def __init__(self, outp):
        self.outp = outp
    def visit_stmts(self, node):
        for v in node.vlst:
            self.outp.ident()
            v.walkabout(self)
    def visit_deepstmts(self, node):
        self.outp.identin()
        node.v.walkabout(self)
        self.outp.identout()
    def visit_main(self, node):
        node.v.walkabout(self)
    def visit_stmt(self, node):
        node.v.walkabout(self)
    def visit_if_stmt(self, node):
        self.outp.puts('if')
        node.v1.walkabout(self)
        self.outp.puts(':')
        node.v2.walkabout(self)
        if node.vq:
            node.vq.walkabout(self)
    def visit_else_part(self, node):
        self.outp.ident()
        self.outp.puts('else')
        self.outp.puts(':')
        node.v.walkabout(self)
    def visit_while_stmt(self, node):
        self.outp.puts('while')
        node.v1.walkabout(self)
        self.outp.puts(':')
        node.v2.walkabout(self)
        if node.vq:
            node.vq.walkabout(self)
    def visit_return_stmt(self, node):
        self.outp.puts('return')
        node.v.walkabout(self)
    def visit_funcdef(self, node):
        self.outp.puts('def')
        self.outp.puts(node.s)
        self.outp.puts('(')
        if node.vq:
            node.vq.walkabout(self)
        self.outp.puts(')')
        self.outp.puts(':')
        node.v.walkabout(self)
    def visit_params(self, node):
        self.outp.puts(node.slst[0])
        for s_ in node.slst[1:]:
            self.outp.puts(',')
            self.outp.puts(s_)
    def visit_augassign(self, node):
        node.v1.walkabout(self)
        self.outp.puts(node.s)
        node.v2.walkabout(self)
    def visit_assign(self, node):
        node.v1.walkabout(self)
        self.outp.puts('=')
        node.v2.walkabout(self)
    def visit_dest(self, node):
        node.v.walkabout(self)
    def visit_dest_array(self, node):
        self.outp.puts(node.s)
        self.outp.puts('[')
        node.v.walkabout(self)
        self.outp.puts(']')
    def visit_print_stmt(self, node):
        self.outp.puts('print')
        if node.vq:
            node.vq.walkabout(self)
        if node.sq:
            self.outp.puts(node.sq)
    def visit_args(self, node):
        node.vlst[0].walkabout(self)
        for v in node.vlst[1:]:
            self.outp.puts(',')
            v.walkabout(self)
    def visit_value_bool(self, node):
        self.outp.puts(node.s)
    def visit_value0(self, node):
        self.outp.puts(node.s)
    def visit_value1(self, node):
        node.v.walkabout(self)
    def visit_enclosed(self, node):
        self.outp.puts('(')
        node.v.walkabout(self)
        self.outp.puts(')')
    def visit_funccall(self, node):
        self.outp.puts(node.s)
        self.outp.puts('(')
        if node.vq:
            node.vq.walkabout(self)
        self.outp.puts(')')
    def visit_array_index(self, node):
        self.outp.puts(node.s)
        self.outp.puts('[')
        node.v.walkabout(self)
        self.outp.puts(']')
    def visit_value2(self, node):
        node.v.walkabout(self)
    def visit_signed(self, node):
        self.outp.puts(node.s)
        node.v.walkabout(self)
    def visit_array(self, node):
        self.outp.puts('[')
        if node.vq:
            node.vq.walkabout(self)
        if node.sq:
            self.outp.puts(node.sq)
        self.outp.puts(']')
    def visit_binvalue(self, node):
        node.v1.walkabout(self)
        self.outp.puts(node.s)
        node.v2.walkabout(self)
    def visit_value(self, node):
        node.v.walkabout(self)
    def visit_litname(self, node):
        self.outp.puts(node.s)

class PY_SerialIn:
    def handle_stmts(self, lst):
        lst_vlst = lst
        vlst = []
        for l_ in lst_vlst:
            v = self.hdl_stmt(l_)
            vlst.append(v)
        return PY_stmts(vlst)
    def handle_deepstmts(self, lst):
        lst_v = lst
        v = self.handle_stmts(lst_v)
        return PY_deepstmts(v)
    def handle_main(self, lst):
        lst_v = lst
        v = self.handle_stmts(lst_v)
        return PY_main(v)
    def hdl_stmt(self, lst):
        lst_v = lst
        (l_,no_) = lst_v
        if no_ == 0:
            v = self.handle_if_stmt(l_)
        elif no_ == 1:
            v = self.handle_while_stmt(l_)
        elif no_ == 2:
            v = self.handle_return_stmt(l_)
        elif no_ == 3:
            v = self.handle_print_stmt(l_)
        elif no_ == 4:
            v = self.handle_funcdef(l_)
        elif no_ == 5:
            v = self.handle_assign(l_)
        elif no_ == 6:
            v = self.handle_augassign(l_)
        elif no_ == 7:
            v = self.hdl_value(l_)
        else:
            assert False
        return v
    def handle_if_stmt(self, lst):
        lst_v1, lst_v2, lst_vq = lst
        v1 = self.hdl_value(lst_v1)
        v2 = self.handle_deepstmts(lst_v2)
        vq = None
        if lst_vq:
            vq = self.handle_else_part(lst_vq)
        return PY_if_stmt(v1, v2, vq)
    def handle_else_part(self, lst):
        lst_v = lst
        v = self.handle_deepstmts(lst_v)
        return PY_else_part(v)
    def handle_while_stmt(self, lst):
        lst_v1, lst_v2, lst_vq = lst
        v1 = self.hdl_value(lst_v1)
        v2 = self.handle_deepstmts(lst_v2)
        vq = None
        if lst_vq:
            vq = self.handle_else_part(lst_vq)
        return PY_while_stmt(v1, v2, vq)
    def handle_return_stmt(self, lst):
        lst_v = lst
        v = self.hdl_value(lst_v)
        return PY_return_stmt(v)
    def handle_funcdef(self, lst):
        lst_s, lst_vq, lst_v = lst
        s = lst_s
        vq = None
        if lst_vq:
            vq = self.handle_params(lst_vq)
        v = self.handle_deepstmts(lst_v)
        return PY_funcdef(s, vq, v)
    def handle_params(self, lst):
        lst_slst = lst
        slst = []
        for l2 in lst_slst:
            s = self.handle_NAME(l2)
            slst.append(s)
        return PY_params(slst)
    def handle_augassign(self, lst):
        lst_v1, lst_s, lst_v2 = lst
        v1 = self.hdl_dest(lst_v1)
        no_ = lst_s
        if no_ == 0:
            s = '+='
        elif no_ == 1:
            s = '-='
        elif no_ == 2:
            s = '/='
        elif no_ == 3:
            s = '*='
        else:
            assert False
        v2 = self.hdl_value(lst_v2)
        return PY_augassign(v1, s, v2)
    def handle_assign(self, lst):
        lst_v1, lst_v2 = lst
        v1 = self.hdl_dest(lst_v1)
        v2 = self.hdl_value(lst_v2)
        return PY_assign(v1, v2)
    def hdl_dest(self, lst):
        lst_v = lst
        (l_,no_) = lst_v
        if no_ == 0:
            v = self.handle_dest_array(l_)
        elif no_ == 1:
            v = self.handle_litname(l_)
        else:
            assert False
        return v
    def handle_dest_array(self, lst):
        lst_s, lst_v = lst
        s = lst_s
        v = self.hdl_value(lst_v)
        return PY_dest_array(s, v)
    def handle_print_stmt(self, lst):
        lst_vq, lst_sq = lst
        vq = None
        if lst_vq:
            vq = self.handle_args(lst_vq)
        sq = ""
        if lst_sq != 0:
            sq = ','
        return PY_print_stmt(vq, sq)
    def handle_args(self, lst):
        lst_vlst = lst
        vlst = []
        for l2 in lst_vlst:
            s = self.hdl_value(l2)
            vlst.append(s)
        return PY_args(vlst)
    def handle_value_bool(self, lst):
        lst_s = lst
        no_ = lst_s
        if no_ == 0:
            s = 'True'
        elif no_ == 1:
            s = 'False'
        else:
            assert False
        return PY_value_bool(s)
    def handle_value0(self, lst):
        lst_s = lst
        (l_,no_) = lst_s
        if no_ == 0:
            s = l_
        elif no_ == 1:
            s = l_
        elif no_ == 2:
            s = l_
        else:
            assert False
        return PY_value0(s)
    def hdl_value1(self, lst):
        lst_v = lst
        (l_,no_) = lst_v
        if no_ == 0:
            v = self.handle_enclosed(l_)
        elif no_ == 1:
            v = self.handle_funccall(l_)
        elif no_ == 2:
            v = self.handle_array_index(l_)
        elif no_ == 3:
            v = self.handle_value_bool(l_)
        elif no_ == 4:
            v = self.handle_value0(l_)
        else:
            assert False
        return v
    def handle_enclosed(self, lst):
        lst_v = lst
        v = self.hdl_value(lst_v)
        return PY_enclosed(v)
    def handle_funccall(self, lst):
        lst_s, lst_vq = lst
        s = lst_s
        vq = None
        if lst_vq:
            vq = self.handle_args(lst_vq)
        return PY_funccall(s, vq)
    def handle_array_index(self, lst):
        lst_s, lst_v = lst
        s = lst_s
        v = self.hdl_value(lst_v)
        return PY_array_index(s, v)
    def hdl_value2(self, lst):
        lst_v = lst
        (l_,no_) = lst_v
        if no_ == 0:
            v = self.handle_signed(l_)
        elif no_ == 1:
            v = self.handle_array(l_)
        elif no_ == 2:
            v = self.hdl_value1(l_)
        else:
            assert False
        return v
    def handle_signed(self, lst):
        lst_s, lst_v = lst
        no_ = lst_s
        if no_ == 0:
            s = '-'
        elif no_ == 1:
            s = '+'
        else:
            assert False
        v = self.hdl_value1(lst_v)
        return PY_signed(s, v)
    def handle_array(self, lst):
        lst_vq, lst_sq = lst
        vq = None
        if lst_vq:
            vq = self.handle_args(lst_vq)
        sq = ""
        if lst_sq != 0:
            sq = ','
        return PY_array(vq, sq)
    def handle_binvalue(self, lst):
        if len(lst) == 1:
            return self.hdl_value2(lst[0])
        def func1(lst2):
            if len(lst2) == 1:
                return self.hdl_value1(lst2[0])
            lst_v1, s, lst_v2 = lst2
            v1 = func1(lst_v1)
            v2 = func1(lst_v2)
            return PY_binvalue(v1, s, v2)
        lst_v1, s, lst_v2 = lst
        v1 = self.handle_binvalue(lst_v1)
        v2 = func1(lst_v2)
        return PY_binvalue(v1, s, v2)
    def hdl_value(self, lst):
        lst_v = lst
        v = self.handle_binvalue(lst_v)
        return v
    def handle_litname(self, lst):
        lst_s = lst
        s = lst_s
        return PY_litname(s)
