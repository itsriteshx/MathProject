"""
Mathematical Verification Script for M3 Animation Project
Independently validates every equation, eigenpair, orthogonality relation,
and diagonalization power identity presented in the video.
"""
import numpy as np


def verify_all():
    A = np.array([[2.0, 1.0], [1.0, 2.0]])
    lambda1, lambda2 = 3.0, 1.0
    v1 = np.array([1.0, 1.0])
    v2 = np.array([-1.0, 1.0])
    u_generic = np.array([1.0, 0.0])

    # 1. Generic non-eigenvector check: u = [1, 0]^T -> Au = [2, 1]^T
    Au = A @ u_generic
    assert np.allclose(Au, [2.0, 1.0]), f"Unexpected Au: {Au}"
    cos_theta = np.dot(u_generic, Au) / (np.linalg.norm(u_generic) * np.linalg.norm(Au))
    angle_deg = np.degrees(np.arccos(cos_theta))
    assert abs(angle_deg - 26.565) < 0.05, f"Unexpected tilt angle: {angle_deg}"

    # 2. Characteristic polynomial roots: det(A - lambda I) = (2 - lambda)^2 - 1 = 0
    for lam in (lambda1, lambda2):
        det_val = np.linalg.det(A - lam * np.eye(2))
        assert np.isclose(det_val, 0.0), f"det(A - {lam}I) != 0: {det_val}"

    # 3. Eigenvalue equation A v = lambda v
    assert np.allclose(A @ v1, lambda1 * v1), "Failed A v1 = 3 v1"
    assert np.allclose(A @ v2, lambda2 * v2), "Failed A v2 = 1 v2"

    # 4. Symmetry & Orthogonality: v1 . v2 = 0
    assert np.allclose(A, A.T), "Matrix A should be symmetric"
    assert np.isclose(np.dot(v1, v2), 0.0), "Eigenvectors are not orthogonal"

    # 5. Diagonalization: A = P D P^-1
    P = np.column_stack([v1, v2])
    D = np.diag([lambda1, lambda2])
    P_inv = np.linalg.inv(P)
    assert np.allclose(P @ D @ P_inv, A), "Failed A = P D P^-1"

    # 6. Matrix Powers (check k=12 cleanly in IEEE-754 float64 precision)
    k = 12
    A_pow_direct = np.linalg.matrix_power(A, k)
    D_pow = np.diag([lambda1 ** k, lambda2 ** k])
    A_pow_diag = P @ D_pow @ P_inv
    assert np.allclose(A_pow_direct, A_pow_diag), f"Failed A^{k} = P D^{k} P^-1"

    # 7. Asymptotic 3^100 scale sanity check for Scene 5
    val_3_100 = float(3 ** 100)
    assert abs(val_3_100 / 5.153775e47 - 1.0) < 1e-4, f"Unexpected 3^100: {val_3_100}"

    print("All 7 mathematical verifications passed cleanly!")
    print(f"  - Generic vector tilt: {angle_deg:.2f} deg")
    print(f"  - Eigenvalues: lambda1={lambda1}, lambda2={lambda2}")
    print(f"  - Eigenbasis orthogonality: v1 . v2 = {np.dot(v1, v2):.1f}")
    print(f"  - Diagonalization A = P D P^-1 verified")
    print(f"  - Power scaling 3^100 ~= {val_3_100:.2e}")


if __name__ == "__main__":
    verify_all()
