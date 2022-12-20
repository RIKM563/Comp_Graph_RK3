import math


# Task1
def rotation_matrix(x, y, alpha):
    disp_matrix = [[1, 0, 0], [0, 1, 0], [-x, -y, 1]]
    r_matrix = [[math.cos(alpha), -math.sin(alpha)], [math.sin(alpha), math.cos(alpha)], [0, 0, 1]]
    s = 0
    t = []
    C = []
    r1 = len(disp_matrix)
    c1 = len(disp_matrix[0])
    c2 = len(r_matrix[0])
    for z in range(0, r1):
        for j in range(0, c2):
            for i in range(0, c1):
                s = s + disp_matrix[z][i] * r_matrix[i][j]
            t.append(s)
            s = 0
        C.append(t)
        t = []
    for i in range(0, 2):
        disp_matrix[2][i] *= -1
    s = 0
    t = []
    final = []
    r1 = len(C)
    c1 = len(C[0])
    c2 = len(disp_matrix[0])
    for z in range(0, r1):
        for j in range(0, c2):
            for i in range(0, c1):
                s = s + C[z][i] * disp_matrix[i][j]
            t.append(s)
            s = 0
        final.append(t)
        t = []
    return final


# Task2
def normal_definition(xa, ya, za, xb, yb, zb, xc, yc, zc):
    vx1 = xa - xb
    vy1 = ya - yb
    vz1 = za - zb
    vx2 = xb - xc
    vy2 = yb - yc
    vz2 = zb - zc
    N_x = (vy1 * vz2) - (vz1 * vy2)
    N_y = (vz1 * vx2) - (vx1 * vz2)
    N_z = (vx1 * vy2) - (vy1 * vx2)
    wrki = math.sqrt(N_x ** 2 + N_y ** 2 + N_z ** 2)
    N_x /= wrki
    N_y /= wrki
    N_z /= wrki
    return N_x, N_y, N_z


# Task3
def point_check(xa, ya, za, xb, yb, zb, xc, yc, zc, x, y):
    s1 = (xa - x) * (yb - ya) - (xb - xa) * (ya - y)
    s2 = (xb - x) * (yc - yb) - (xc - xb) * (yb - y)
    s3 = (xc - x) * (ya - yc) - (xa - xc) * (yc - y)
    if (s1 <= 0 and s2 <= 0 and s3 <= 0) or (s1 >= 0 and s2 >= 0 and s3 >= 0):
        return True
    else:
        return False
