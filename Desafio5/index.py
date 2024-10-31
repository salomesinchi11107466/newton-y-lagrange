from math import log10


def M_w(M_0):
    return (2 / 3) * log10(M_0) - 10.7



def M_0(M_w):
    return pow(10, (3 / 2) * (M_w + 10.7))


def error(M_w, E_m_w):
    return abs(3.45387 * pow(10, (3 / 2) * (M_w + 10.7))) * E_m_w


M_chile = 9.5
M_alaska = 8.7
E = 0.15

print(f"M0 de chile VALOR = {M_0(M_chile)}")
print(f"M0 de chile ERROR = {error(M_chile, E)}")

print(f"M0 de chile VALOR = {M_0(M_alaska)}")
print(f"M0 de chile ERROR = {error(M_alaska, E)}")
