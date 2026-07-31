"""
lab_coffee_utils.py
====================
Plotting and data generation utilities for the Coffee Roasting neural network lab.

Provides:
- Coffee roasting dataset generator (vectorized)
- Decision boundary and probability field visualizations
- Per-unit hidden layer activation plots
- Network probability and decision boundary comparison plots
- 3-D output unit weight visualization

All public function signatures are preserved for drop-in compatibility.
"""

from __future__ import annotations

from typing import Callable

import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# ---------------------------------------------------------------------------
# Colour palette — graceful fallback if lab_utils_common is unavailable
# ---------------------------------------------------------------------------

try:
    from lab_utils_common import dlc
except ImportError:
    dlc = {
        "dldarkblue": "#002060",
        "dlpurple":   "#7030A0",
    }

# Decision boundary line slope (derived from roasting domain constraints)
_BOUNDARY_SLOPE     = -3.0 / (260.0 - 175.0)  # -3/85
_BOUNDARY_INTERCEPT = 21.0


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """Numerically stable element-wise sigmoid."""
    z = np.clip(np.asarray(z, dtype=float), -500.0, 500.0)
    return 1.0 / (1.0 + np.exp(-z))


def _boundary_line(t: np.ndarray) -> np.ndarray:
    """Evaluates the diagonal roasting quality boundary at temperatures t."""
    return _BOUNDARY_SLOPE * t + _BOUNDARY_INTERCEPT


def _draw_decision_lines(ax: plt.Axes, X: np.ndarray) -> None:
    """
    Overlays the three roasting quality boundary lines on an axes.

    Parameters
    ----------
    ax : matplotlib Axes
    X  : np.ndarray, shape (m, 2)   Raw (unnormalized) feature matrix.
    """
    t_range = np.linspace(175.0, 260.0, 50)
    ax.plot(t_range, _boundary_line(t_range), color=dlc["dlpurple"], linewidth=1)
    ax.axhline(y=12.0,  color=dlc["dlpurple"], linewidth=1)
    ax.axvline(x=175.0, color=dlc["dlpurple"], linewidth=1)


def truncate_colormap(
    cmap: colors.Colormap,
    minval: float = 0.0,
    maxval: float = 1.0,
    n: int = 100,
) -> colors.LinearSegmentedColormap:
    """
    Returns a new colormap spanning only [minval, maxval] of the source map.

    Parameters
    ----------
    cmap    : matplotlib Colormap   Source colormap.
    minval  : float                 Lower fraction of the source range to keep.
    maxval  : float                 Upper fraction of the source range to keep.
    n       : int                   Number of colour samples.

    Returns
    -------
    matplotlib.colors.LinearSegmentedColormap
    """
    return colors.LinearSegmentedColormap.from_list(
        f'trunc({cmap.name},{minval:.2f},{maxval:.2f})',
        cmap(np.linspace(minval, maxval, n)),
    )


# ---------------------------------------------------------------------------
# Data generation
# ---------------------------------------------------------------------------

def load_coffee_data() -> tuple[np.ndarray, np.ndarray]:
    """
    Generates a synthetic coffee roasting classification dataset.

    Samples 200 (temperature, duration) pairs uniformly at random and
    labels each as a good roast (1) or bad roast (0) based on three
    domain constraints:
        - Temperature ∈ (175, 260) °C
        - Duration    ∈ (12,  15)  minutes
        - Duration    ≤ -3/85 * Temperature + 21  (diagonal quality boundary)

    Returns
    -------
    X : np.ndarray, shape (200, 2)
        Columns: [Temperature (°C), Duration (minutes)].
    Y : np.ndarray, shape (200, 1)
        Binary labels — 1 = good roast, 0 = bad roast.
    """
    rng = np.random.default_rng(2)
    X   = rng.random((200, 2))

    X[:, 0] = X[:, 0] * (285.0 - 150.0) + 150.0   # Temperature: [150, 285] °C
    X[:, 1] = X[:, 1] * 4.0 + 11.5                 # Duration:    [11.5, 15.5] min

    t, d = X[:, 0], X[:, 1]
    good = (t > 175.0) & (t < 260.0) & (d > 12.0) & (d < 15.0) & (d <= _boundary_line(t))
    Y    = good.astype(int).reshape(-1, 1)

    return X, Y


# ---------------------------------------------------------------------------
# Probability field renderer
# ---------------------------------------------------------------------------

def plt_prob(ax: plt.Axes, fwb: Callable) -> None:
    """
    Shades the axes background with predicted probabilities from a model.

    Evaluates `fwb` on a 40×40 grid spanning the feature space and renders
    the result as a pcolormesh, providing a continuous confidence heatmap.

    Parameters
    ----------
    ax  : matplotlib Axes
    fwb : callable   Accepts (m, 2) array of raw features, returns (m,) probabilities.
    """
    t_space = np.linspace(150.0, 285.0, 40)
    d_space = np.linspace(11.5,  15.5,  40)
    T, D    = np.meshgrid(t_space, d_space)

    points  = np.c_[T.ravel(), D.ravel()]           # (1600, 2)
    z       = np.asarray(fwb(points)).reshape(T.shape)

    cmap = truncate_colormap(plt.get_cmap('Blues'), 0.0, 0.5)
    pcm  = ax.pcolormesh(
        T, D, z,
        norm=colors.Normalize(vmin=0.0, vmax=1.0),
        cmap=cmap, shading='nearest', alpha=0.9,
    )
    ax.figure.colorbar(pcm, ax=ax)


# ---------------------------------------------------------------------------
# Main plot functions
# ---------------------------------------------------------------------------

def plt_roast(X: np.ndarray, Y: np.ndarray) -> None:
    """
    Scatter plot of the raw coffee roasting dataset with decision boundaries.

    Parameters
    ----------
    X : np.ndarray, shape (m, 2)   Feature matrix [Temperature, Duration].
    Y : np.ndarray, shape (m,) or (m, 1)   Binary labels.
    """
    Y   = np.asarray(Y).ravel()
    fig, ax = plt.subplots(1, 1, figsize=(6, 5))

    ax.scatter(X[Y == 1, 0], X[Y == 1, 1], s=70,  marker='x', c='red',
               label="Good Roast")
    ax.scatter(X[Y == 0, 0], X[Y == 0, 1], s=100, marker='o',
               facecolors='none', edgecolors=dlc["dldarkblue"],
               linewidth=1, label="Bad Roast")

    _draw_decision_lines(ax, X)

    ax.set_title("Coffee Roasting", size=16)
    ax.set_xlabel("Temperature\n(Celsius)", size=12)
    ax.set_ylabel("Duration\n(minutes)", size=12)
    ax.legend(loc='upper right')
    plt.show()


def plt_layer(
    X:      np.ndarray,
    Y:      np.ndarray,
    W1:     np.ndarray,
    b1:     np.ndarray,
    norm_l: tf.keras.layers.Layer,
) -> None:
    """
    Plots the activation probability field for each hidden layer unit.

    One subplot is created per neuron in layer 1. Each subplot shows the
    region where that neuron fires (P > 0.5) overlaid on the training data.

    Parameters
    ----------
    X      : np.ndarray, shape (m, 2)         Raw (unnormalized) features.
    Y      : np.ndarray, shape (m,) or (m, 1) Binary labels.
    W1     : np.ndarray, shape (2, n_units)    Layer 1 weight matrix.
    b1     : np.ndarray, shape (n_units,)      Layer 1 bias vector.
    norm_l : tf.keras.layers.Normalization     Fitted normalization layer.
    """
    Y         = np.asarray(Y).ravel()
    n_units   = W1.shape[1]
    fig, axes = plt.subplots(1, n_units, figsize=(5 * n_units, 4))

    if n_units == 1:
        axes = [axes]

    for i, ax in enumerate(axes):
        # Evaluate unit i independently across the feature space
        unit_fn = lambda x, i=i: _sigmoid(
            np.dot(norm_l(x).numpy(), W1[:, i]) + b1[i]
        )
        plt_prob(ax, unit_fn)

        ax.scatter(X[Y == 1, 0], X[Y == 1, 1], s=70,  marker='x', c='red',
                   label="Good Roast")
        ax.scatter(X[Y == 0, 0], X[Y == 0, 1], s=100, marker='o',
                   facecolors='none', edgecolors=dlc["dldarkblue"],
                   linewidth=1, label="Bad Roast")

        _draw_decision_lines(ax, X)
        ax.set_title(f"Unit {i}")
        ax.set_xlabel("Temperature")
        ax.set_ylabel("Duration")

    plt.tight_layout()
    plt.show()


def plt_network(X: np.ndarray, Y: np.ndarray, netf: Callable) -> None:
    """
    Side-by-side comparison of network probability field and hard decisions.

    Left panel  — continuous P(good roast) heatmap across feature space.
    Right panel — binary predictions (threshold at 0.5) on training data.

    Parameters
    ----------
    X    : np.ndarray, shape (m, 2)           Raw (unnormalized) features.
    Y    : np.ndarray, shape (m,) or (m, 1)   True binary labels.
    netf : callable   Accepts (m, 2) raw features, returns (m,) probabilities.
    """
    Y       = np.asarray(Y).ravel()
    fig, ax = plt.subplots(1, 2, figsize=(16, 4))

    # Left: continuous probability heatmap
    plt_prob(ax[0], netf)
    ax[0].scatter(X[Y == 1, 0], X[Y == 1, 1], s=70,  marker='x', c='red',
                  label="Good Roast")
    ax[0].scatter(X[Y == 0, 0], X[Y == 0, 1], s=100, marker='o',
                  facecolors='none', edgecolors=dlc["dldarkblue"],
                  linewidth=1, label="Bad Roast")
    ax[0].set_title("Network Probability")

    # Right: hard threshold decisions
    yhat = (np.asarray(netf(X)).ravel() >= 0.5).astype(int)
    ax[1].scatter(X[yhat == 1, 0], X[yhat == 1, 1], s=70,  marker='x', c='orange',
                  label="Predicted Good Roast")
    ax[1].scatter(X[yhat == 0, 0], X[yhat == 0, 1], s=100, marker='o',
                  facecolors='none', edgecolors=dlc["dldarkblue"],
                  linewidth=1, label="Predicted Bad Roast")
    ax[1].set_title("Network Decision")

    for a in ax:
        _draw_decision_lines(a, X)
        a.set_xlabel("Temperature\n(Celsius)", size=12)
        a.set_ylabel("Duration\n(minutes)", size=12)
        a.legend(loc='upper right')

    plt.tight_layout()
    plt.show()


def plt_output_unit(W: np.ndarray, b: np.ndarray) -> None:
    """
    3-D scatter visualization of the output unit's activation across
    the three-dimensional hidden layer activation space.

    Samples a 10×10×10 grid of (unit0, unit1, unit2) activations and
    shades each point by the output unit's predicted probability.

    Parameters
    ----------
    W : np.ndarray, shape (3, 1)   Output layer weight matrix.
    b : np.ndarray, shape (1,)     Output layer bias.
    """
    steps   = 10
    coords  = np.linspace(0.0, 1.0, steps)
    x, y, z = np.meshgrid(coords, coords, coords, indexing='ij')

    grid   = np.c_[x.ravel(), y.ravel(), z.ravel()]   # (1000, 3)
    logits = np.dot(grid, W[:, 0]) + b
    d      = tf.keras.activations.sigmoid(logits).numpy()

    fig = plt.figure()
    ax  = fig.add_subplot(projection='3d')

    pcm = ax.scatter(x.ravel(), y.ravel(), z.ravel(),
                     c=d, cmap='Blues', alpha=0.8)

    ax.set_xlabel("Unit 0")
    ax.set_ylabel("Unit 1")
    ax.set_zlabel("Unit 2")
    ax.set_title("Layer 2 — Output Unit")
    ax.view_init(elev=30, azim=-120)

    fig.colorbar(pcm, ax=ax, shrink=0.6)
    plt.show()