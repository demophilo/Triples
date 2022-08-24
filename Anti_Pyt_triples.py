#!/usr/bin/env python
# coding: utf-8




#  The functions calculate all possible, nontrivial triangles with three integer edges
#  and either 60, 90 or 120 degrees according to a given integer.
#  Output is a list of lists of triples and angles.
#  The first edge is opposite to the first angle and so on.
#  The function triple_60 calculates 60° and 120° triangles.
#  The argument switch has three different values.
#  switch = 60 calculates only 60° triangles.
#  switch = 120 calculates only 120° triangles.
#  switch = *any other value* calculates 60° and 120° triangles in one go.


import math
from operator import itemgetter


def triple_60(num, switch = 60):
    _n = int(math.ceil(num/2) + 1)
    _triple = []
    for _p in range(-_n + 1, _n):
        for _q in range(-_p + 1, _p):
            if _q == 0 or _p == 2*_q or _p == 0:
                continue
            _a = abs(2*_p*_q -_p**2)
            _b = abs(_q**2 - _p**2)
            _c = abs(_p**2 + _q**2 -_q*_p)
            
            if _a**2 + _b**2 - _c**2 < 0 and switch == 60:
                continue
                
            if _a**2 + _b**2 - _c**2 > 0 and switch == 120:
                continue
            
            if _b < _a:
                _a, _b = _b, _a
                       
            if num % _a == 0:
                __a = num
                __b = int(_b*num/_a)
                __c = int(_c*num/_a)
                _triple_i = [__a, __b, __c]
                if _triple_i not in _triple:
                    _triple.append(_triple_i)
                   
                    
            if num % _b == 0:
                __b = num
                __a = int(_a*num/_b)
                __c = int(_c*num/_b)
                _triple_i = [__a, __b, __c]
                if _triple_i not in _triple:
                    _triple.append(_triple_i)
                    
                    
            if num % _c == 0:
                __c = num
                __b = int(_b*num/_c)
                __a = int(_a*num/_c)
                _triple_i = [__a, __b, __c]
                if _triple_i not in _triple:
                    _triple.append(_triple_i)
    for _i in range(len(_triple)):
        _triple[_i].append(math.degrees(math.acos((_triple[_i][1]**2 + _triple[_i][2]**2 - _triple[_i][0]**2)/(2*_triple[_i][1]*_triple[_i][2]))))
        _triple[_i].append(math.degrees(math.acos((_triple[_i][0]**2 + _triple[_i][2]**2 - _triple[_i][1]**2)/(2*_triple[_i][0]*_triple[_i][2]))))
        _triple[_i].append(int(round(math.degrees(math.acos((_triple[_i][1]**2 + _triple[_i][0]**2 - _triple[_i][2]**2)/(2*_triple[_i][1]*_triple[_i][0]))))))
        
    _sorted_winkel = sorted(_triple, key = itemgetter(5, 3))
    return _sorted_winkel





def triple_90(num):
    _n = int(math.ceil(num/2) + 1)
    _triple = []
    for _p in range(2, _n):
        for _q in range(1, _p):           
            _a = 2*_p*_q
            _b =_p**2 - _q**2
            _c =_p**2 + _q**2
            if _b < _a:
                _a, _b = _b, _a
                       
            if num % _a == 0:
                __a = num
                __b = int(_b*num/_a)
                __c = int(_c*num/_a)
                _triple_i = [__a, __b, __c]
                if _triple_i not in _triple:
                    _triple.append(_triple_i)
                   
                    
            if num % _b == 0:
                __b = num
                __a = int(_a*num/_b)
                __c = int(_c*num/_b)
                _triple_i = [__a, __b, __c]
                if _triple_i not in _triple:
                    _triple.append(_triple_i)
                    
                    
            if num % _c == 0:
                __c = num
                __b = int(_b*num/_c)
                __a = int(_a*num/_c)
                _triple_i = [__a, __b, __c]
                if _triple_i not in _triple:
                    _triple.append(_triple_i)
    for _i in range(len(_triple)):
        _triple[_i].append(math.degrees(math.asin(_triple[_i][0]/_triple[_i][2])))
        _triple[_i].append(math.degrees(math.asin(_triple[_i][1]/_triple[_i][2])))
        _triple[_i].append(90)
    _sorted_winkel = sorted(_triple,key=itemgetter(3))
    return _sorted_winkel




for num in range(3,37):
    print(num,len(triple_90(num)))
    for i in range(len(triple_90(num))):
        print(triple_90(num)[i])



