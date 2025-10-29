# -*- coding: utf-8 -*-
"""
Lab 6 – Beräkningsverktyg
Converted from annotated-LAB6.py.pdf
Authors in source: Erik Redmo & Emrik Rehnberg Gr3
"""

import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

sp.init_printing()
x = sp.symbols('x')

# ============================================================
# Warmup expr from the notebook top (not part of questions)
# ============================================================
expr_example = sp.sin(sp.pi * x**2) / (x**2 - 1)

# ============================================================
# Lab 6 Fråga 1
# ============================================================

def n_decimals_pi(n):
    """
    Count digit frequencies 0..9 in π up to n decimals.
    Returns a list [count0, count1, ..., count9]
    """
    # "Exact" pi with n+1 significant digits -> enough to get n decimals
    pi_n_string = str(sp.pi.evalf(n + 1))

    # Build list of digits only
    pi_n_list = [int(ch) for ch in pi_n_string if ch.isdigit()]

    # Remove the leading '3' from '3.1415...'
    if len(pi_n_list) > 0:
        del pi_n_list[0]

    # Count digits 0-9
    bar_list = []
    for i in range(10):
        bar_list.append(pi_n_list.count(i))

    return bar_list


def plot_pi_distribution(n):
    number_list = ['0','1','2','3','4','5','6','7','8','9']
    plt.title(f'Amount of digits 0–9 in π with {n} decimals')
    plt.ylabel('Amount')
    plt.xlabel('Digit')
    plt.bar(number_list, n_decimals_pi(n))
    plt.show()


# Plots for different precisions
plot_pi_distribution(10)
plot_pi_distribution(100)
plot_pi_distribution(1000)
plot_pi_distribution(10000)
plot_pi_distribution(100000)


# ============================================================
# Lab 6 Fråga 2
# ============================================================

# We'll reuse sympy here
sp.init_printing()
x = sp.symbols('x')
u = sp.symbols('u')  # In the notebook they did u = x**pi then overwrote it.

def limits(expr, var, lim):
    """Return limit of expr as var -> lim."""
    return sp.limit(expr, var, lim)

def derivative(expr, var):
    """Return simplified derivative d/d(var) expr."""
    return sp.simplify(sp.diff(expr, var))

def Taylor(expr, var, x_surr, degree):
    """
    Return Taylor/Maclaurin series expansion of expr around x_surr,
    up to (degree-1)th order term. Uses sympy .series().
    """
    return expr.series(var, x_surr, degree)

# 3.25 Gränsvärden
expr25a = (3*x + 4) / (4*x + 3)**x
expr25b = (1 + 3*x)**(1/(8*x))
expr25c = (x - sp.sin(x)) / (x - sp.tan(x))
expr25d = (sp.sin(u))**2 / (1 - sp.cos(2*u))

# 4.6 Derivatan
expr46a = (sp.exp(3*x)) / x
expr46b = sp.asin((2*x + 1)/5)
expr46c = sp.exp(2*x) * sp.log(2*x)  # log == natural log in sympy
expr46d = sp.cos(2*x) - (sp.sin(x))**2

# 5.21 Taylorutveckling
expr521a = sp.exp(-3*x)        # around x = 1
expr521b = sp.sin(2*x)         # around x = pi
expr521c = (sp.sin(x))**2      # around x = -pi/2
expr521d = (x + 1)/(x**2)      # around x = -2

print('3.25')
print(
    'a)', limits(expr25a, x, sp.oo),
    '\n',
    'b)', limits(expr25b, x, 0),
    '\n',
    'c)', limits(expr25c, x, 0),
    '\n',
    'd)', limits(expr25d, u, 0)
)

print('4.6')
print(
    'a)', derivative(expr46a, x),
    '\n',
    'b)', derivative(expr46b, x),
    '\n',
    'c)', derivative(expr46c, x),
    '\n',
    'd)', derivative(expr46d, x)
)

print('5.21')
print(
    'a)', Taylor(expr521a, x, 1, 6),
    '\n',
    'b)', Taylor(expr521b, x, sp.pi, 6),
    '\n',
    'c)', Taylor(expr521c, x, -sp.pi/2, 6),
    '\n',
    'd)', Taylor(expr521d, x, -2, 6)
)

# ============================================================
# Lab 6 Fråga 3a)
# ============================================================

sp.init_printing()
x = sp.symbols('x')

def stationary(expr, var):
    """
    Find stationary points (critical points): solve f'(x)=0 over Reals.
    Returns the solution set from solveset.
    """
    expr_diff = sp.diff(expr, var)
    solvedstat = sp.solveset(expr_diff, var, domain=sp.S.Reals)
    sp.pprint(solvedstat)
    return solvedstat

# Uppgift 413
expr413a = x + sp.cos(x)
expr413b = 100*x + 200*sp.sin(x)
expr413c = sp.sqrt(3)*x + 2*sp.sin(x)
expr413d = sp.exp(-x)*sp.sin(2*x)

stat413a = stationary(expr413a, x)
stat413b = stationary(expr413b, x)
stat413c = stationary(expr413c, x)
stat413d = stationary(expr413d, x)

# ============================================================
# Lab 6 Fråga 3b)
# ============================================================

sp.init_printing()
x = sp.symbols('x')

def inflex(expr, var):
    """
    Approximate inflection points by solving f''(x) = 0.
    Tries to evaluate y-values at those x-values.
    Handles different Sympy set types like Union, Complement, FiniteSet.
    Returns (x_candidates_set, y_values_list or message).
    """
    expr_second_diff = sp.diff(expr, var, var)
    solved_inflex = sp.solveset(expr_second_diff, var, domain=sp.S.Reals)

    # Narrow / normalize solution set into a usable list of x candidates
    if isinstance(solved_inflex, sp.sets.Union):
        # For complicated periodic solutions, clip to [0, 2π]
        solved_inflex_list = list(
            solved_inflex.intersect(sp.Interval(0, 2*sp.pi))
        )
        print('The given function has been narrowed to the interval [0, 2π]')
    elif isinstance(solved_inflex, sp.sets.Complement):
        # Complement often means "all reals except ..." which is not isolated
        solved_inflex_list = []
    elif isinstance(solved_inflex, sp.sets.FiniteSet):
        solved_inflex_list = list(solved_inflex)
    else:
        # fallback: just try to iterate it
        try:
            solved_inflex_list = list(solved_inflex)
        except Exception:
            solved_inflex_list = []

    # Compute y-values using limits to be safe
    y_values = []
    try:
        for val in solved_inflex_list:
            y_values.append(sp.limit(expr, var, val))
    except Exception:
        print(expr, 'Something went wrong while evaluating y-values')
    if y_values == []:
        y_values = 'Solveset could not find y-values'

    print('The x-value(s) for the inflection point(s) of', expr, 'are:')
    sp.pprint(sp.simplify(solved_inflex))
    print('The y-value(s) for the inflection point(s) are:')
    sp.pprint(y_values)
    print('---')

    return (solved_inflex, y_values)

# Uppgift 414
expr414a = x**3 - x**2
expr414b = x**4 - x**2
expr414c = sp.sin(2*x)
expr414d = sp.sin(sp.log(x))

infl414a = inflex(expr414a, x)
infl414b = inflex(expr414b, x)
infl414c = inflex(expr414c, x)
infl414d = inflex(expr414d, x)

# ============================================================
# Lab 6 Fråga 4
# ============================================================

sp.init_printing()
x = sp.symbols('x')

def maxmin(expr, var, start, slut):
    """
    Find xmin, ymin, xmax, ymax of expr on [start, slut].
    Uses derivative to test stationary points + endpoints.
    Returns (x_min, y_min, x_max, y_max) where x_min/x_max may be sets.
    """
    start_r = sp.Rational(start)
    slut_r = sp.Rational(slut)

    # Endpoint values (use limit to be robust if expr not defined exactly there)
    y_start = sp.limit(expr, var, start_r)
    y_slut = sp.limit(expr, var, slut_r)

    # Initialize guess
    if y_start > y_slut:
        ymax = y_start
        ymin = y_slut
        xmax = start_r
        xmin = slut_r
    else:
        ymax = y_slut
        ymin = y_start
        xmax = slut_r
        xmin = start_r

    try:
        expr_diff = sp.diff(expr, var)
        # All real stationary points
        xzero_points = sp.solveset(expr_diff, var, domain=sp.S.Reals)

        # Restrict them to the interval
        xzero_points_interval = list(
            xzero_points.intersect(sp.Interval(start_r, slut_r))
        )

        # Evaluate y at those stationary points
        y_values = []
        for xv in xzero_points_interval:
            y_values.append(sp.limit(expr, var, xv))

        # Update min/max if interior extrema beat endpoints
        if len(y_values) > 0:
            if max(y_values) > ymax:
                ymax_final = max(y_values)
            else:
                ymax_final = ymax

            if min(y_values) < ymin:
                ymin_final = min(y_values)
            else:
                ymin_final = ymin
        else:
            ymax_final = ymax
            ymin_final = ymin

        # Solve expr == ymax_final / ymin_final in interval to get x locations
        x_values_for_ymax = sp.solveset(
            expr - ymax_final,
            var,
            sp.Interval(start_r, slut_r)
        )
        x_values_for_ymin = sp.solveset(
            expr - ymin_final,
            var,
            sp.Interval(start_r, slut_r)
        )

    except Exception:
        # If something failed, fall back to endpoints only
        x_values_for_ymin = xmin
        x_values_for_ymax = xmax
        ymin_final = ymin
        ymax_final = ymax

    return (x_values_for_ymin, ymin_final, x_values_for_ymax, ymax_final)


expr411a = x * (1 - x)
expr411b = x**2 * (1 - x)**2
# expr411c = 3*pi*x + 6*sin(pi*x)  # commented out in source
expr411d = sp.simplify((x + 2)/(x + 1))
expr_extra = x**3 - x**2
expr_exempel = x**2

maxmin411a = maxmin(expr411a, x, 0, 1)
maxmin411b = maxmin(expr411b, x, 0, 1)
# maxmin411c = maxmin(expr411c, x, 0, 1)
maxmin411d = maxmin(expr411d, x, 0, 1)
maxmin_extra = maxmin(expr_extra, x, -sp.Rational(1, 3), 1)
maxmin_exempel = maxmin(expr_exempel, x, -1, 1)

print('xmin, ymin, xmax, ymax for', expr411a, 'on [0,1]')
sp.pprint(maxmin411a)
print('xmin, ymin, xmax, ymax for', expr411b, 'on [0,1]')
sp.pprint(maxmin411b)
print('xmin, ymin, xmax, ymax for', expr411d, 'on [0,1]')
sp.pprint(maxmin411d)
print('xmin, ymin, xmax, ymax for', expr_extra, 'on [-1/3,1]')
sp.pprint(maxmin_extra)
print('xmin, ymin, xmax, ymax for', expr_exempel, 'on [-1,1]')
sp.pprint(maxmin_exempel)

# ============================================================
# Lab 6 Fråga 5
# ============================================================

sp.init_printing()
x = sp.symbols('x')

def largest_power_with_limit_at_zero(expr, var):
    """
    For a function f(x), find the largest integer a such that
    limit( f(x) / x^a, x->0 ) is finite (not infinite).
    If f diverges at 0 to begin with, return nan.
    If it never diverges up to a=100, return oo.
    """
    # First check if f itself diverges
    if sp.Abs(sp.limit(expr, var, 0)) == sp.oo:
        a = sp.nan
    else:
        a = 0
        # Increase a until dividing by x**a causes divergence
        while sp.Abs(sp.limit(sp.simplify(expr / (var**a)), var, 0)) < sp.oo:
            a += 1
            if a > 100:
                break

        if a > 100:
            a = sp.oo
        else:
            # We went one step too far (the first divergent power),
            # so subtract 1 to get the last convergent one
            a -= 1
    return a

print(largest_power_with_limit_at_zero(sp.sqrt(x), x))
print(largest_power_with_limit_at_zero(1/x, x))
print(largest_power_with_limit_at_zero(sp.sin(x), x))
print(largest_power_with_limit_at_zero(
    (1 - sp.cos(x)) + (sp.log(1 - x**2))/2,
    x
))
print(largest_power_with_limit_at_zero(sp.exp(-1/x), x))

# Optional: show plots if running interactively
if __name__ == "__main__":
    plt.show()
