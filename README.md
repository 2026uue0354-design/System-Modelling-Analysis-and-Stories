# Image Transformation Toolbox

## Overview

This project contains two Python programs related to image transformation using linear algebra and PIL/NumPy.

- `Assignment 03 q11.py` - An interactive image transformation toolbox.
- `Assignment 03.py` - Demonstrates image transformations using predefined transformation matrices and explains their linear algebra properties.

---

## 1. Interactive Image Transformation Toolbox

### File
`Assignment 03 q11.py`

This program allows the user to load an image and apply different geometric transformations through a simple text-based menu.

The program uses the Python Imaging Library (PIL).

### Requirements

Install Pillow if it is not already installed:

```bash
pip install pillow
```

### How to Run

Run:

```bash
python "Assignment 03 q11.py"
```

The program first asks for the path of an image:

```text
Enter image file path (e.g., image.jpg):
```

The image is then opened and the original copy is saved so that it can be restored using the Reset option.

### Available Operations

#### Rotate
Enter an angle in degrees.

Example:
```text
rotate
Enter rotation angle (degrees): 90
```

#### Resize
Enter a scale factor.

Examples:
- `0.5` = half the size
- `2.0` = double the size

#### Flip
Choose:
- `h` for horizontal flip
- `v` for vertical flip

#### Shear
Enter X and Y shear factors.

Example:
```text
X shear factor: 0.2
Y shear factor: 0.2
```

#### Custom Matrix
Enter six coefficients of an affine transformation:

```text
(a, b, c, d, e, f)
```

These values control scaling, shearing and shifting.

#### Reset
Restores the image to its original state.

#### Exit
Closes the program.

---

## 2. Linear Algebra Image Transformation Program

### File
`Assignment 03.py`

This program demonstrates how transformation matrices can be used to transform an image.

It uses:

- NumPy
- Matplotlib
- PIL

### Requirements

Install the required libraries if needed:

```bash
pip install numpy matplotlib pillow
```

### Input Image

Place an image named:

```text
your_image.jpg
```

in the same folder as the Python file.

The program loads the image and converts it into a NumPy array.

### Transformation Matrices

The program defines five matrices:

1. Scaling
2. 90° Rotation
3. Horizontal Shear
4. Reflection in the y-axis
5. Projection onto the x-axis

The matrices are stored in a dictionary and applied to the image.

### Basis Vectors

The standard basis vectors are:

```text
e1 = [1, 0]
e2 = [0, 1]
```

For every transformation matrix `A`, the program calculates:

```text
T(e1) = A @ e1
T(e2) = A @ e2
```

This shows how the transformation changes the two basic directions.

### Rank and Information Loss

The program calculates the rank of every transformation matrix.

If:

```text
rank(A) < 2
```

the program reports that information has been lost.

For the projection matrix, one dimension is lost because the transformation projects the image onto the x-axis.

### Image Transformation Method

The function `transform_image()`:

1. Finds the image centre.
2. Calculates the inverse transformation matrix.
3. Processes each output pixel.
4. Finds the corresponding original pixel.
5. Copies the pixel if it is inside the image boundaries.

This allows the transformation matrix to be applied to the image.

### Output

The program displays:

- Original image
- Scaled image
- Rotated image
- Sheared image
- Reflected image
- Projected image

It also prints:

- `T(e1)`
- `T(e2)`
- Matrix rank
- Whether information is lost
- Column interpretation

---

## Concepts Used

This project demonstrates the following concepts:

- Image processing
- Geometric transformations
- Transformation matrices
- Matrix multiplication
- Basis vectors
- Linear transformations
- Matrix rank
- Information loss
- Affine transformations
- NumPy arrays
- PIL image processing
- Matplotlib visualization

---

## Notes

For the interactive program, the image can be any supported image file such as JPG or PNG.

For the matrix-based program, the input filename is currently set to:

```text
your_image.jpg
```

The projection matrix is singular, so its true inverse does not exist. The program therefore uses a small y-scale only for visualization while still reporting the true projection matrix and its rank.

---

## Project Purpose

The main purpose of this project is to connect the concepts of linear algebra with practical image processing. Transformation matrices can be used to change the position, size, orientation and shape of an image.

