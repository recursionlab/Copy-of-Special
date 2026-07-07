import numpy as np
from scipy.linalg import expm
from halira_kernel.utils.env import HAS_SAGE

def antisym_matrix(d1, d2):
    """
    Creates an antisymmetric matrix from two vectors.
    """
    # Ensure d1 and d2 are 1D arrays
    d1 = np.asarray(d1).flatten()
    d2 = np.asarray(d2).flatten()
    
    # Outer product to a skew matrix
    return 0.5 * (np.outer(d1, d2) - np.outer(d2, d1))

def transport_matrix(v_i, v_j, alpha=1.0):
    """
    Transport operator T_ij from embedding difference vectors.
    v_i, v_j are numpy arrays (embeddings).
    """
    d_ij = v_j - v_i
    d_ji = -d_ij
    A = antisym_matrix(d_ij, d_ji)
    return expm(alpha * A)

def loop_torsion(loop_indices, embeddings, alpha=1.0):
    """
    Compute torsion along a loop (sequence of vertex indices).
    Returns ||Prod(T_ij) - I||.
    """
    if not loop_indices or len(loop_indices) < 2:
        return 0.0

    dim = embeddings.shape[1] # Dimension of embedding space
    prod = np.eye(dim)

    # Iterate through the loop, creating edges (v_start, v_end)
    for k in range(len(loop_indices) - 1):
        v_start_idx = loop_indices[k]
        v_end_idx = loop_indices[k+1]
        
        v_start = embeddings[v_start_idx]
        v_end = embeddings[v_end_idx]
        
        prod = prod @ transport_matrix(v_start, v_end, alpha=alpha)

    return np.linalg.norm(prod - np.eye(dim))

def smith_normal_form_torsion(boundary_matrix):
    """
    Computes rank and torsion invariants from a Sage integer matrix.
    """
    if not HAS_SAGE:
        # Euclidean Fallback: Compute rank via SVD, ignore integer torsion.
        if boundary_matrix.size == 0:
            return 0, []
        rank = int(np.linalg.matrix_rank(boundary_matrix))
        return rank, []

    from sage.all import Matrix, ZZ
    if boundary_matrix.nrows() == 0 or boundary_matrix.ncols() == 0:
        return 0, []
    
    # Ensure it's a Sage Matrix over ZZ
    if not isinstance(boundary_matrix, Matrix) or boundary_matrix.base_ring() != ZZ:
        boundary_matrix = Matrix(ZZ, boundary_matrix)

    S, U, V = boundary_matrix.smith_form()
    diag = S.diagonal()
    
    # Torsion invariants are elements > 1 on the diagonal
    torsion = [d for d in diag if d != 0 and d != 1]
    rank = sum(1 for d in diag if d == 0) # Free rank is number of zeros on diagonal for homology
    
    return rank, torsion

def homology_torsion(boundary_n, boundary_n_plus_1):
    """
    Computes homology group H_n = ker(∂_n) / im(∂_{n+1}) and its torsion.
    boundary_n: Sage Matrix for ∂_n
    boundary_n_plus_1: Sage Matrix for ∂_{n+1}
    Returns (free_rank, torsion_invariants)
    """
    # H_n = ker(∂_n) / im(∂_{n+1})
    # Rank of H_n = rank(ker ∂_n) - rank(im ∂_{n+1})
    # Torsion of H_n = torsion(ker ∂_n) + torsion(im ∂_{n+1}) (simplified)

    if not HAS_SAGE:
        # Approximate rank-based homology calculation for standard environments
        rank_im_next = int(np.linalg.matrix_rank(boundary_n_plus_1))
        rank_ker_curr = boundary_n.shape[1] - int(np.linalg.matrix_rank(boundary_n))
        return max(0, rank_ker_curr - rank_im_next), []

    from sage.all import Matrix, ZZ
    # Ensure matrices are Sage integer matrices
    if not isinstance(boundary_n, Matrix) or boundary_n.base_ring() != ZZ:
        boundary_n = Matrix(ZZ, boundary_n)
    if not isinstance(boundary_n_plus_1, Matrix) or boundary_n_plus_1.base_ring() != ZZ:
        boundary_n_plus_1 = Matrix(ZZ, boundary_n_plus_1)

    # Rank-nullity theorem: rank(A) + nullity(A) = ncols(A)
    # rank(im ∂_{n+1}) = rank(∂_{n+1})
    # rank(ker ∂_n) = ncols(∂_n) - rank(∂_n)

    rank_im_n_plus_1 = boundary_n_plus_1.rank()
    rank_ker_n = boundary_n.ncols() - boundary_n.rank()

    free_rank = rank_ker_n - rank_im_n_plus_1
    
    # For torsion, we need to compute the Smith Normal Form of the homology matrix
    # This is a simplification; full computation involves exact sequences.
    # For now, we'll just return a placeholder for torsion based on the boundaries.
    _, torsion_n = smith_normal_form_torsion(boundary_n)
    _, torsion_n_plus_1 = smith_normal_form_torsion(boundary_n_plus_1)
    
    # Combine torsion (this is a heuristic, not a rigorous algebraic sum)
    combined_torsion = sorted(list(set(torsion_n + torsion_n_plus_1)))

    return free_rank, combined_torsion

def tau_from_barcode(barcode, loops, embeddings, alpha=1.0, kappa=1.0):
    """
    Computes tau from barcodes + loops + embeddings.
    barcode: list of (birth, death) intervals
    loops: list of loops (vertex indices) corresponding to barcodes
    embeddings: numpy array of point embeddings
    alpha: scaling for transport matrix
    kappa: bias toward longevity for persistence
    """
    total = 0.0
    for i, (b, d) in enumerate(barcode):
        if i >= len(loops): # Safety check
            continue
        
        loop = loops[i]
        length = (d - b) if d < np.inf else 1.0 # Persistence lifetime
        
        if not loop: # Skip empty loops
            continue

        torsion_val = loop_torsion(loop, embeddings, alpha=alpha)
        total += (length ** kappa) * torsion_val
    return total