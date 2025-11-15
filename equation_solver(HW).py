import re
import numpy as np

equation = "5x^3+4x^2+3x = 6"

def parse_side(s):
    s = s.replace(' ', '')
    terms = re.findall(r'[+-]?[^+-]+', s)
    coeffs = {}
    for t in terms:
        if t in ('', '+', '-'): continue
        m = re.fullmatch(r'([+-]?)(\d*\.?\d*)?([a-zA-Z]?)(?:\^(\d+))?', t)
        if not m: raise ValueError("Can't parse term: "+t)
        sign, num, var, power = m.groups()
        sign = -1 if sign == '-' else 1
        if var == '':
            c = float(num) if num not in (None, '') else 0.0
            deg = 0
        else:
            deg = int(power) if power else 1
            c = float(num) if num not in (None, '') and num != '' else 1.0
        coeffs[deg] = coeffs.get(deg, 0.0) + sign * c
    return coeffs

def combine_sides(left, right):
    all_degs = set(left) | set(right)
    res = {d: left.get(d, 0.0) - right.get(d, 0.0) for d in all_degs}
    return {d: v for d, v in res.items() if abs(v) > 1e-12}

def coeffs_dict_to_list(d):
    if not d: return [0.0]
    maxdeg = max(d)
    return [d.get(i, 0.0) for i in range(maxdeg, -1, -1)]

def solve_equation_from_string(eq_str):
    if '=' not in eq_str: raise ValueError("Equation must contain '='")
    left_s, right_s = eq_str.split('=', 1)
    left = parse_side(left_s)
    right = parse_side(right_s)
    poly = combine_sides(left, right)
    coeff_list = coeffs_dict_to_list(poly)
    if all(abs(c) < 1e-12 for c in coeff_list):
        return coeff_list, "No solution or infinite solutions."
    roots = np.roots(coeff_list)
    clean = []
    for r in roots:
        if abs(r.imag) < 1e-10:
            clean.append(round(r.real, 12))
        else:
            clean.append(complex(round(r.real,12), round(r.imag,12)))
    return coeff_list, clean

if __name__ == "__main__":
    coeffs, roots = solve_equation_from_string(equation)
    print("Equation:", equation)
    print("Coefficients (highest->lowest):", coeffs)
    print("Roots:", roots)
