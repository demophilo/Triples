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


from math import acos
from math import degrees
from math import gcd
from pprint import pprint


def angel_by_cos_law(*triangle, opposite_edge=0):
    """
    calculates the angle opposite to a given edge
    :param triangle: triple of positive numbers
    :param opposite_edge: 0 to 2 defines the angle to calculate
    :return: angle in degrees
    """
    if opposite_edge == 1:
        triangle[1], triangle[0] = triangle[0], triangle[1]
    elif opposite_edge == 2:
        triangle[2], triangle[0] = triangle[0], triangle[2]

    _angle = degrees(acos((triangle[1] ** 2 + triangle[2] ** 2 - triangle[0] ** 2) /
                          (2 * triangle[1] * triangle[2])))
    return _angle


def gen_trojan_triple(big_num, small_num):
    """
    Trojan triple calculated by development point (-1, -1)
    :param big_num:
    :param small_num: absolute value of small_int must be smaller than big_int
    :return: sorted tuple of trojan triple
    """
    _edge0 = abs(2 * big_num * small_num - big_num ** 2)
    _edge1 = abs(2 * big_num * small_num - small_num ** 2)
    _edge2 = big_num ** 2 + small_num ** 2 - big_num * small_num

    if _edge0 != 0 and _edge1 != 0 and _edge2 != 0:
        divisor = gcd(_edge0, _edge1, _edge2)
        _edge0 = int(_edge0 / divisor)
        _edge1 = int(_edge1 / divisor)
        _edge2 = int(_edge2 / divisor)

    _triple = sorted([_edge0, _edge1, _edge2], reverse=True)

    if _triple[1] ** 2 == _triple[0] ** 2 + _triple[2] ** 2 - _triple[0] * _triple[2]:
        _triple[0], _triple[1] = _triple[1], _triple[0]

    return tuple(_triple)


def generate_trojan_tripples(limit_number):
    trojan_triples = []
    for p in range(-limit_number, limit_number + 1):
        if p == 0:
            continue
        for q in range(-abs(p) + 1, abs(p)):
            trojan_triple = gen_trojan_triple(p, q)
            if trojan_triple[2] != 0:
                trojan_triples.append(trojan_triple)

    trojan_triples = list(set(trojan_triples))
    trojan_triples.sort()
    return trojan_triples

if __name__ == "__main__":
    trojan_triples = generate_trojan_tripples(200)


# Dictionary initialisieren
tuples_count_dict = {}

# Durch die Liste von Tupeln iterieren
for triple in trojan_triples:
    # Das erste Element des Tupels als Key verwenden
    key = triple[0]

    # Wenn der Key bereits im Dictionary existiert, die Anzahl erhöhen, ansonsten den Key hinzufügen
    if key in tuples_count_dict:
        tuples_count_dict[key] += 1
    else:
        tuples_count_dict[key] = 1

# Das resultierende Dictionary ausgeben
pprint(tuples_count_dict)


