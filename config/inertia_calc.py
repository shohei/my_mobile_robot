# Boxの計算
def calculate_box_inertia(m, w, d, h):
    Iw = (m / 12.0) * (pow(d, 2) + pow(h, 2))
    Id = (m / 12.0) * (pow(w, 2) + pow(h, 2))
    Ih = (m / 12.0) * (pow(w, 2) + pow(d, 2))
    print('BOX ixx="' + '{:.5f}'.format(Iw) + '" iyy="' + '{:.5f}'.format(Id) +
        '" izz="' + '{:.5f}'.format(Ih) + '" ixy="0.0" ixz="0.0" iyz="0.0"')


# Sphereの計算
def calculate_sphere_inertia(m, r):
    I = (2 * m * pow(r, 2)) / 5.0
    print('SPHERE ixx="' + '{:.5f}'.format(I) + '" iyy="' + '{:.5f}'.format(I) +
        '" izz="' + '{:.5f}'.format(I) + '" ixy="0.0" ixz="0.0" iyz="0.0"')


# Cylinderの計算
def calculate_cylinder_inertia(m, r, h):
    Ix = (m / 12.0) * (3 * pow(r, 2) + pow(h, 2))
    Iy = Ix
    Iz = (m * pow(r, 2)) / 2.0
    print('Cylinder ixx="' + '{:.5f}'.format(Ix) + '" iyy="' + '{:.5f}'.format(Iy) +
        '" izz="' + '{:.5f}'.format(Iz) + '" ixy="0.0" ixz="0.0" iyz="0.0"')


# Inertia計算機
selection = "START"
while selection.upper() != "Q":
    # メニューの表示
    print("====================")
    print("Geometryを選択してください:")
    print("[1] Box width(x-axis)*depth(y-axis)*height(z-axis)")
    print("[2] Sphere radius(r)")
    print("[3] Cylinder radius(r)*height(h)")
    print("[Q] 終了")

    # メニュー項目の入力
    selection = input(">>")

    # パラメータの入力と計算
    if selection == "1":
        mass = float(input("mass>>"))
        width = float(input("x-axis length>>"))
        depth = float(input("y-axis length>>"))
        height = float(input("z-axis length>>"))
        calculate_box_inertia(m=mass, w=width, d=depth, h=height)
    elif selection == "2":
        mass = float(input("mass>>"))
        radius = float(input("radius>>"))
        calculate_sphere_inertia(m=mass, r=radius)
    elif selection == "3":
        mass = float(input("mass>>"))
        radius = float(input("radius>>"))
        height = float(input("height>>"))
        calculate_cylinder_inertia(m=mass, r=radius, h=height)
