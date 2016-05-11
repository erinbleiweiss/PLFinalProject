
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '872583E741B287574CB7080343974BF6'
    
_lr_action_items = {'EQUALS':([14,],[19,]),'$end':([1,2,3,4,5,6,7,9,10,12,13,20,21,22,23,24,25,26,27,28,],[-3,-7,0,-1,-2,-9,-18,-8,-5,-6,-4,-13,-12,-17,-16,-15,-14,-10,-11,-19,]),'TEXT':([8,],[14,]),'MINUS':([11,21,],[15,15,]),'DIV':([11,23,],[16,16,]),'MULT':([11,25,],[17,17,]),'LET':([0,],[8,]),'INTEGER':([0,1,2,4,6,9,10,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,],[11,-3,-7,11,-9,-8,-5,-6,-4,21,23,25,26,28,-13,-12,-17,-16,-15,-14,-10,-11,]),'PLUS':([11,26,],[18,18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,4,],[1,13,]),'subtraction':([0,4,15,],[2,2,20,]),'program':([0,],[3,]),'expressions':([0,],[4,]),'declaration':([0,],[5,]),'division':([0,4,16,],[6,6,22,]),'let':([0,],[7,]),'multiplication':([0,4,17,],[9,9,24,]),'operation':([0,4,],[10,10,]),'addition':([0,4,18,],[12,12,27,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> expressions','program',1,'p_program','yacc.py',19),
  ('program -> declaration','program',1,'p_program','yacc.py',20),
  ('expressions -> expression','expressions',1,'p_expressions','yacc.py',27),
  ('expressions -> expressions expression','expressions',2,'p_expressions','yacc.py',28),
  ('expression -> operation','expression',1,'p_expression','yacc.py',32),
  ('operation -> addition','operation',1,'p_operation','yacc.py',38),
  ('operation -> subtraction','operation',1,'p_operation','yacc.py',39),
  ('operation -> multiplication','operation',1,'p_operation','yacc.py',40),
  ('operation -> division','operation',1,'p_operation','yacc.py',41),
  ('addition -> INTEGER PLUS INTEGER','addition',3,'p_addition','yacc.py',45),
  ('addition -> INTEGER PLUS addition','addition',3,'p_addition','yacc.py',46),
  ('subtraction -> INTEGER MINUS INTEGER','subtraction',3,'p_subtraction','yacc.py',50),
  ('subtraction -> INTEGER MINUS subtraction','subtraction',3,'p_subtraction','yacc.py',51),
  ('multiplication -> INTEGER MULT INTEGER','multiplication',3,'p_multiplication','yacc.py',55),
  ('multiplication -> INTEGER MULT multiplication','multiplication',3,'p_multiplication','yacc.py',56),
  ('division -> INTEGER DIV INTEGER','division',3,'p_division','yacc.py',60),
  ('division -> INTEGER DIV division','division',3,'p_division','yacc.py',61),
  ('declaration -> let','declaration',1,'p_declaration','yacc.py',69),
  ('let -> LET TEXT EQUALS INTEGER','let',4,'p_let','yacc.py',73),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',82),
]
