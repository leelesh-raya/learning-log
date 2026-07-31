"""
lab_utils_common.py
====================
Production-grade ML utility library for Andrew Ng Deep Learning Specialisation labs.

Provides:
- Numerically stable sigmoid and log-sum-exp implementations
- Vectorized logistic and linear cost/gradient functions with L2 regularisation
- Batch gradient descent with adaptive learning rate decay
- Z-score feature normalisation
- Common plotting routines for logistic and tumor classification data
- Interactive checkbox button manager for Jupyter/Matplotlib widgets

All public function signatures are preserved for drop-in compatibility.
"""

from __future__ import annotations

import copy
import math
from typing import Callable, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
from matplotlib.widgets import CheckButtons

# ---------------------------------------------------------------------------
# Global display configuration
# ---------------------------------------------------------------------------

np.set_printoptions(precision=2)
plt.style.use('./deeplearning.mplstyle')

# Colour palette
dlblue    = '#0096ff'
dlorange  = '#FF9300'
dldarkred = '#C00000'
dlmagenta = '#FF40FF'
dlpurple  = '#7030A0'
dldarkblue = '#0D5BDC'

dlc = dict(
    dlblue=dlblue, dlorange=dlorange, dldarkred=dldarkred,
    dlmagenta=dlmagenta, dlpurple=dlpurple, dldarkblue=dldarkblue,
)
dlcolors = [dlblue, dlorange, dldarkred, dlmagenta, dlpurple]

# Numerical stability constants
_SIGMOID_CLIP = 500.0   # clips z before exp to prevent overflow
_LOG_EPS      = 1e-15   # lower bound for log arguments


# ---------------------------------------------------------------------------
# Core mathematical primitives
# ---------------------------------------------------------------------------

def sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Element-wise sigmoid with overflow protection.

    Clips input to [-500, 500] before exponentiation so that very large
    negative or positive values do not produce inf/nan.

    Parameters
    ----------
    z : array_like
        Scalar or array of any shape.

    Returns
    -------
    np.ndarray
        sigmoid(z), same shape as input, values in (0, 1).
    """
    z = np.clip(np.asarray(z, dtype=float), -_SIGMOID_CLIP, _SIGMOID_CLIP)
    return 1.0 / (1.0 + np.exp(-z))


def log_1pexp(x: np.ndarray) -> np.ndarray:
    """
    Numerically stable approximation of log(1 + exp(x)).

    Uses the standard identity:
        log(1 + exp(x)) = max(x, 0) + log(1 + exp(-|x|))

    This matches the implementation used by PyTorch (F.softplus) and
    avoids overflow for large positive x and underflow for large negative x.

    Parameters
    ----------
    x : array_like
        Input array of any shape.

    Returns
    -------
    np.ndarray
        Approximation of log(1 + exp(x)), same shape as input.
    """
    x = np.asarray(x, dtype=float)
    return np.maximum(x, 0.0) + np.log1p(np.exp(-np.abs(x)))


# ---------------------------------------------------------------------------
# Prediction
# ---------------------------------------------------------------------------

def predict_logistic(X: np.ndarray, w: np.ndarray, b: float) -> np.ndarray:
    """
    Logistic regression prediction P(y=1 | X, w, b).

    Parameters
    ----------
    X : np.ndarray, shape (m, n)
    w : np.ndarray, shape (n,) or (n, 1)
    b : float

    Returns
    -------
    np.ndarray, shape (m,)
        Predicted probabilities.
    """
    return sigmoid(X @ w + b)


def predict_linear(X: np.ndarray, w: np.ndarray, b: float) -> np.ndarray:
    """
    Linear regression prediction f(X) = X @ w + b.

    Parameters
    ----------
    X : np.ndarray, shape (m, n)
    w : np.ndarray, shape (n,) or (n, 1)
    b : float

    Returns
    -------
    np.ndarray, shape (m,)
        Predicted values.
    """
    return X @ w + b


# ---------------------------------------------------------------------------
# Cost functions
# ---------------------------------------------------------------------------

def compute_cost_logistic(
    X: np.ndarray,
    y: np.ndarray,
    w: np.ndarray,
    b: float,
    lambda_: float = 0.0,
    safe: bool = False,
) -> float:
    """
    Vectorized binary cross-entropy cost with optional L2 regularisation.

    Replaces the original loop-based implementation with full matrix
    vectorisation while preserving the identical function signature.

    Parameters
    ----------
    X       : np.ndarray, shape (m, n)   Feature matrix.
    y       : np.ndarray, shape (m,)     Binary target labels.
    w       : np.ndarray, shape (n,)     Weight vector.
    b       : float                      Bias scalar.
    lambda_ : float                      L2 regularisation strength (0 = none).
    safe    : bool                       Use log-sum-exp formulation if True.

    Returns
    -------
    float
        Scalar total cost.
    """
    m = X.shape[0]
    y = np.asarray(y, dtype=float).reshape(-1, 1)
    w = np.asarray(w, dtype=float).reshape(-1, 1)

    z = X @ w + b  # (m, 1)

    if safe:
        cost = np.sum(-(y * z) + log_1pexp(z)) / m
    else:
        f_wb = np.clip(sigmoid(z), _LOG_EPS, 1.0 - _LOG_EPS)
        cost = -np.sum(y * np.log(f_wb) + (1.0 - y) * np.log(1.0 - f_wb)) / m

    reg_cost = (lambda_ / (2.0 * m)) * np.sum(w ** 2) if lambda_ != 0 else 0.0

    return float(cost + reg_cost)


def compute_cost_matrix(
    X: np.ndarray,
    y: np.ndarray,
    w: np.ndarray,
    b: float,
    logistic: bool = False,
    lambda_: float = 0.0,
    safe: bool = True,
) -> float:
    """
    Unified cost function for linear and logistic regression.

    Selects MSE (linear) or binary cross-entropy (logistic) based on the
    `logistic` flag. L2 regularisation is applied when lambda_ != 0.

    Parameters
    ----------
    X        : np.ndarray, shape (m, n)
    y        : np.ndarray, shape (m,) or (m, 1)
    w        : np.ndarray, shape (n,) or (n, 1)
    b        : float
    logistic : bool    True → binary cross-entropy, False → MSE.
    lambda_  : float   L2 regularisation coefficient.
    safe     : bool    Use numerically stable log-sum-exp path for logistic.

    Returns
    -------
    float
        Scalar total cost.
    """
    m = X.shape[0]
    y = np.asarray(y, dtype=float).reshape(-1, 1)
    w = np.asarray(w, dtype=float).reshape(-1, 1)

    z = X @ w + b  # (m, 1)

    if logistic:
        if safe:
            cost = np.sum(-(y * z) + log_1pexp(z)) / m
        else:
            f_wb = np.clip(sigmoid(z), _LOG_EPS, 1.0 - _LOG_EPS)
            cost = float(
                -(y.T @ np.log(f_wb) + (1.0 - y).T @ np.log(1.0 - f_wb)) / m
            )
    else:
        cost = float(np.sum((z - y) ** 2) / (2.0 * m))

    reg_cost = (lambda_ / (2.0 * m)) * float(np.sum(w ** 2))

    return float(cost + reg_cost)


# ---------------------------------------------------------------------------
# Gradient
# ---------------------------------------------------------------------------

def compute_gradient_matrix(
    X: np.ndarray,
    y: np.ndarray,
    w: np.ndarray,
    b: float,
    logistic: bool = False,
    lambda_: float = 0.0,
) -> Tuple[float, np.ndarray]:
    """
    Vectorized gradient of the cost w.r.t. w and b.

    Parameters
    ----------
    X        : np.ndarray, shape (m, n)
    y        : np.ndarray, shape (m,) or (m, 1)
    w        : np.ndarray, shape (n,) or (n, 1)
    b        : float
    logistic : bool    True → logistic gradient, False → linear gradient.
    lambda_  : float   L2 regularisation coefficient.

    Returns
    -------
    dj_db : float          Gradient w.r.t. bias.
    dj_dw : np.ndarray     Gradient w.r.t. weights, shape (n, 1).
    """
    m = X.shape[0]
    y = np.asarray(y, dtype=float).reshape(-1, 1)
    w = np.asarray(w, dtype=float).reshape(-1, 1)

    f_wb  = sigmoid(X @ w + b) if logistic else X @ w + b  # (m, 1)
    error = f_wb - y                                        # (m, 1)

    dj_dw = (X.T @ error) / m                              # (n, 1)
    dj_db = float(np.sum(error) / m)

    if lambda_ != 0:
        dj_dw += (lambda_ / m) * w

    return dj_db, dj_dw


# ---------------------------------------------------------------------------
# Optimisation
# ---------------------------------------------------------------------------

def gradient_descent(
    X: np.ndarray,
    y: np.ndarray,
    w_in: np.ndarray,
    b_in: float,
    alpha: float,
    num_iters: int,
    logistic: bool = False,
    lambda_: float = 0.0,
    verbose: bool = True,
    Trace: bool = True,
) -> Tuple[np.ndarray, float, list]:
    """
    Batch gradient descent with adaptive learning rate decay.

    When the cost stops decreasing between print intervals the learning rate
    is divided by 10 to help escape flat regions without diverging.

    Parameters
    ----------
    X         : np.ndarray, shape (m, n)    Feature matrix.
    y         : np.ndarray, shape (m,)      Target values.
    w_in      : np.ndarray, shape (n,)      Initial weights.
    b_in      : float                       Initial bias.
    alpha     : float                       Initial learning rate.
    num_iters : int                         Number of gradient steps.
    logistic  : bool                        Linear if False, logistic if True.
    lambda_   : float                       L2 regularisation strength.
    verbose   : bool or int                 True → print cost; 2 → also print gradients.
    Trace     : bool                        Record cost history if True.

    Returns
    -------
    w         : np.ndarray, shape matches w_in   Final weight vector.
    b         : float                            Final bias.
    J_history : list[float]                      Cost at each recorded iteration.
    """
    J_history: list = []
    w = copy.deepcopy(w_in).reshape(-1, 1).astype(float)
    y = np.asarray(y, dtype=float).reshape(-1, 1)
    b = float(b_in)
    last_cost = np.inf

    print_interval = math.ceil(num_iters / 10)

    for i in range(num_iters):
        dj_db, dj_dw = compute_gradient_matrix(X, y, w, b, logistic, lambda_)

        w -= alpha * dj_dw
        b -= alpha * dj_db

        ccost = compute_cost_matrix(X, y, w, b, logistic, lambda_)

        if Trace and i < 100_000:
            J_history.append(ccost)

        if i % print_interval == 0:
            if verbose:
                print(f"Iteration {i:4d}: Cost {ccost:<12.6f}")
            if verbose == 2:
                print(f"  dj_db={dj_db:0.3f}  dj_dw={np.squeeze(dj_dw)}")

            # Adaptive decay: halve alpha if cost has stalled
            if np.isclose(ccost, last_cost, atol=1e-12, rtol=1e-12):
                alpha /= 10.0
                print(f"  ↓ alpha decayed → {alpha:.2e}")
            last_cost = ccost

    return w.reshape(w_in.shape), b, J_history


# ---------------------------------------------------------------------------
# Feature engineering
# ---------------------------------------------------------------------------

def zscore_normalize_features(
    X: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Z-score normalises each feature column to zero mean and unit variance.

    Parameters
    ----------
    X : np.ndarray, shape (m, n)    Raw feature matrix.

    Returns
    -------
    X_norm : np.ndarray, shape (m, n)   Normalised feature matrix.
    mu     : np.ndarray, shape (n,)     Column means.
    sigma  : np.ndarray, shape (n,)     Column standard deviations.

    Notes
    -----
    If a feature has zero variance (constant column) sigma is set to 1
    to avoid division by zero, leaving that column unchanged after mean
    subtraction.
    """
    mu    = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)
    sigma = np.where(sigma == 0, 1.0, sigma)  # guard against constant features
    return (X - mu) / sigma, mu, sigma


# ---------------------------------------------------------------------------
# Plotting utilities
# ---------------------------------------------------------------------------

def _hide_toolbar(ax: plt.Axes) -> None:
    """Suppresses Jupyter canvas toolbar/header/footer widgets if present."""
    canvas = ax.figure.canvas
    for attr in ('toolbar_visible', 'header_visible', 'footer_visible'):
        if hasattr(canvas, attr):
            setattr(canvas, attr, False)


def plot_data(
    X: np.ndarray,
    y: np.ndarray,
    ax: plt.Axes,
    pos_label: str = "y=1",
    neg_label: str = "y=0",
    s: int = 80,
    loc: str = 'best',
) -> None:
    """
    Scatter plot for two-feature logistic classification data.

    Positive examples (y=1) are drawn as red crosses;
    negative examples (y=0) as blue open circles.

    Parameters
    ----------
    X         : np.ndarray, shape (m, 2)
    y         : np.ndarray, shape (m,)
    ax        : matplotlib Axes
    pos_label : legend label for positive class
    neg_label : legend label for negative class
    s         : marker size
    loc       : legend location string
    """
    y = np.asarray(y).ravel()
    pos, neg = y == 1, y == 0

    ax.scatter(X[pos, 0], X[pos, 1], marker='x', s=s, c='red',  label=pos_label)
    ax.scatter(X[neg, 0], X[neg, 1], marker='o', s=s, label=neg_label,
               facecolors='none', edgecolors=dlblue, lw=3)
    ax.legend(loc=loc)
    _hide_toolbar(ax)


def plt_tumor_data(x: np.ndarray, y: np.ndarray, ax: plt.Axes) -> None:
    """
    1-D scatter plot for single-feature tumor classification data.

    Malignant examples (y=1) → red crosses.
    Benign examples    (y=0) → blue open circles.

    Parameters
    ----------
    x  : np.ndarray, shape (m,)   Tumor size feature.
    y  : np.ndarray, shape (m,)   Binary labels.
    ax : matplotlib Axes
    """
    y = np.asarray(y).ravel()
    pos, neg = y == 1, y == 0

    ax.scatter(x[pos], y[pos], marker='x', s=80,  c='red',   label="malignant")
    ax.scatter(x[neg], y[neg], marker='o', s=100, label="benign",
               facecolors='none', edgecolors=dlblue, lw=3)
    ax.set_ylim(-0.175, 1.1)
    ax.set_ylabel('y')
    ax.set_xlabel('Tumor Size')
    ax.set_title("Logistic Regression on Categorical Data")
    _hide_toolbar(ax)


def draw_vthresh(ax: plt.Axes, x: float) -> None:
    """
    Annotates a decision threshold at x on a 1-D logistic regression plot.

    Shades the region where z >= 0 in red and z < 0 in blue, and draws
    directional arrows with labels.

    Parameters
    ----------
    ax : matplotlib Axes
    x  : float   x-coordinate of the decision boundary (z = 0 location).
    """
    ylim = ax.get_ylim()
    xlim = ax.get_xlim()

    ax.fill_between([xlim[0], x], [ylim[1], ylim[1]], alpha=0.2, color=dlblue)
    ax.fill_between([x, xlim[1]], [ylim[1], ylim[1]], alpha=0.2, color=dldarkred)

    ax.annotate("z >= 0", xy=(x, 0.5), xycoords='data',
                xytext=(30, 5), textcoords='offset points')
    ax.add_artist(FancyArrowPatch(
        posA=(x, 0.5), posB=(x + 3, 0.5), color=dldarkred,
        arrowstyle='simple, head_width=5, head_length=10, tail_width=0.0',
    ))

    ax.annotate("z < 0", xy=(x, 0.5), xycoords='data',
                xytext=(-50, 5), textcoords='offset points', ha='left')
    ax.add_artist(FancyArrowPatch(
        posA=(x, 0.5), posB=(x - 3, 0.5), color=dlblue,
        arrowstyle='simple, head_width=5, head_length=10, tail_width=0.0',
    ))


# ---------------------------------------------------------------------------
# Interactive widget
# ---------------------------------------------------------------------------

class button_manager:
    """
    Mutually exclusive (one-on) CheckButton manager for Matplotlib/Jupyter.

    Wraps a matplotlib CheckButtons widget to enforce a single active
    selection at all times — clicking the active button re-enables it
    rather than leaving all buttons unchecked.

    Parameters
    ----------
    fig           : matplotlib Figure
    dim           : list[float]   [left, bottom, width, height] in figure coords.
    labels        : list[str]     Button label strings.
    init          : list[bool]    Initial checked state; exactly one must be True.
    call_on_click : callable      Called with (active_index, firsttime=False) on change.
    """

    def __init__(
        self,
        fig: plt.Figure,
        dim: list,
        labels: list,
        init: list,
        call_on_click: Callable,
    ) -> None:
        self.fig           = fig
        self.ax            = plt.axes(dim)
        self.init_state    = list(init)
        self.call_on_click = call_on_click

        self.button = CheckButtons(self.ax, labels, init)
        self.button.on_clicked(self._button_click)
        self.status = list(self.button.get_status())

        # Fire initial callback so the display reflects the default selection
        self.call_on_click(self.status.index(True), firsttime=True)

    def reinit(self) -> None:
        """Resets button state to the initial configuration."""
        self.status = list(self.init_state)
        self.button.set_active(self.status.index(True))

    def _button_click(self, event: str) -> None:
        """
        Enforces one-on state on every click.

        If the currently active button is clicked again it is re-enabled.
        If a different button is clicked the previously active one is turned off.
        """
        self.button.eventson = False
        new_status   = list(self.button.get_status())
        changed_idx  = [o ^ n for o, n in zip(self.status, new_status)].index(True)
        old_active   = self.status.index(True)

        if changed_idx == old_active:
            # Re-enable the only active button — prevent empty state
            self.button.set_active(changed_idx)
        else:
            # Deactivate the old selection and activate the new one
            self.button.set_active(old_active)

        self.button.eventson = True
        self.status = list(self.button.get_status())
        self.call_on_click(self.status.index(True))