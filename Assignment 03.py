import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# -------------------------------
# 1. LOAD IMAGE
# -------------------------------

img = Image.open("your_image.jpg").convert("RGB")
img_array = np.array(img)

height, width = img_array.shape[:2]


# -------------------------------
# 2. TRANSFORMATION MATRICES
# -------------------------------

A1 = np.array([[2, 0],
               [0, 0.5]])      # Scaling

A2 = np.array([[0, -1],
               [1,  0]])       # 90 degree rotation

A3 = np.array([[1, 1],
               [0, 1]])        # Horizontal shear

A4 = np.array([[-1, 0],
               [ 0, 1]])       # Reflection in y-axis

A5 = np.array([[1, 0],
               [0, 0]])        # Projection onto x-axis


matrices = {
    "A1: Scaling": A1,
    "A2: 90° Rotation": A2,
    "A3: Horizontal Shear": A3,
    "A4: Reflection in y-axis": A4,
    "A5: Projection onto x-axis": A5
}


# -------------------------------
# 3. BASIS VECTORS
# -------------------------------

e1 = np.array([1, 0])
e2 = np.array([0, 1])


# -------------------------------
# 4. FUNCTION TO TRANSFORM IMAGE
# -------------------------------

def transform_image(image, A):

    h, w = image.shape[:2]

    # Create empty output image
    output = np.zeros_like(image)

    # Image centre
    cx = w / 2
    cy = h / 2

    # Inverse matrix
    A_inv = np.linalg.inv(A)

    for row in range(h):
        for col in range(w):

            # Output pixel coordinates relative to centre
            x = col - cx
            y = cy - row

            point = np.array([x, y])

            # Find corresponding original point
            original_point = A_inv @ point

            ox = original_point[0]
            oy = original_point[1]

            # Convert back to image coordinates
            original_col = int(round(ox + cx))
            original_row = int(round(cy - oy))

            # Check boundaries
            if 0 <= original_row < h and 0 <= original_col < w:
                output[row, col] = image[original_row, original_col]

    return output


# -------------------------------
# 5. APPLY TRANSFORMATIONS
# -------------------------------

transformed_images = {}

for name, A in matrices.items():

    print("\n-------------------------")
    print(name)
    print("-------------------------")

    # T(e1) and T(e2)
    print("T(e1) =", A @ e1)
    print("T(e2) =", A @ e2)

    # Rank
    rank = np.linalg.matrix_rank(A)
    print("rank(A) =", rank)

    # Information loss
    if rank < 2:
        print("Information lost: YES")
    else:
        print("Information lost: NO")

    # A5 is singular, so use small y-scale only for visualization
    if name == "A5: Projection onto x-axis":

        A_visual = np.array([
            [1, 0],
            [0, 0.02]
        ])

        transformed_images[name] = transform_image(img_array, A_visual)

        print("True matrix A5 =")
        print(A)
        print("Visualization uses y-scale = 0.02")

    else:
        transformed_images[name] = transform_image(img_array, A)


# -------------------------------
# 6. DISPLAY RESULTS
# -------------------------------

fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Original image
axes[0, 0].imshow(img_array)
axes[0, 0].set_title("Original Image")
axes[0, 0].axis("off")

# Transformed images
positions = [
    (0, 1),
    (0, 2),
    (1, 0),
    (1, 1),
    (1, 2)
]

for (name, image), position in zip(transformed_images.items(), positions):

    row, col = position

    axes[row, col].imshow(image)
    axes[row, col].set_title(name)
    axes[row, col].axis("off")

plt.tight_layout()
plt.show()


# -------------------------------
# 7. COLUMN INTERPRETATION
# -------------------------------

print("\nCOLUMN INTERPRETATION:")

for name, A in matrices.items():

    print("\n", name)

    print("Column 1 =", A[:, 0], " = T(e1)")
    print("Column 2 =", A[:, 1], " = T(e2)")

    if np.linalg.matrix_rank(A) == 2:
        print("Both columns provide two independent directions.")
    else:
        print("Columns are dependent, so one dimension is lost.")