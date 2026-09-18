from PIL import Image

path = input("Enter image file path (e.g., image.jpg): ")
img = Image.open(path)
original_img = img.copy()

while True:
    img.show()  # Opens image in default viewer
    
    print("\nOptions: rotate | resize | flip | shear | custom | reset | exit")
    choice = input("Select operation: ").strip().lower()

    w, h = img.size

    if choice == 'rotate':
        angle = float(input("Enter rotation angle (degrees): "))
        img = img.rotate(-angle, expand=True)

    elif choice == 'resize':
        factor = float(input("Enter scale factor (e.g., 0.5 or 2.0): "))
        img = img.resize((int(w * factor), int(h * factor)))

    elif choice == 'flip':
        direction = input("Flip direction ('h' for horizontal, 'v' for vertical): ").strip().lower()
        if direction == 'h':
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif direction == 'v':
            img = img.transpose(Image.FLIP_TOP_BOTTOM)

    elif choice == 'shear':
        sx = float(input("X shear factor (e.g., 0.2): "))
        sy = float(input("Y shear factor (e.g., 0.2): "))
        img = img.transform((w, h), Image.AFFINE, (1, -sx, 0, -sy, 1, 0))

    elif choice == 'custom':
        print("Enter 6 matrix coefficients for affine transform (a, b, c, d, e, f):")
        a = float(input("a (X scale): "))
        b = float(input("b (X shear): "))
        c = float(input("c (X shift): "))
        d = float(input("d (Y shear): "))
        e = float(input("e (Y scale): "))
        f = float(input("f (Y shift): "))
        img = img.transform((w, h), Image.AFFINE, (a, b, c, d, e, f))

    elif choice == 'reset':
        img = original_img.copy()

    elif choice == 'exit':
        break