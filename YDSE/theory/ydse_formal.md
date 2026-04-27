# Young's Double Slit Experiment (Formal Theory)

## Setup

Consider two slits separated by distance $d$, with a screen placed at distance $D$ from the slits. Let the wavelength of the light be $\lambda$. For a point on the screen at transverse position $y$, the two waves travel slightly different distances before meeting.

## Path Difference

For small angles,

$$
\Delta x = \frac{d y}{D}
$$

## Phase Difference

The corresponding phase difference is

$$
\Delta \phi = \frac{2\pi}{\lambda}\,\Delta x
$$

## Conditions for Interference

### Constructive Interference

Bright fringes occur when

$$
\Delta x = n\lambda
$$

where $n = 0, \pm 1, \pm 2, \dots$

### Destructive Interference

Dark fringes occur when

$$
\Delta x = \left(n + \frac{1}{2}\right)\lambda
$$

## Fringe Width

The fringe width is

$$
\beta = \frac{\lambda D}{d}
$$

## Intensity Distribution

The observed intensity is computed from the superposed fields:

$$
I \propto |E_1 + E_2|^2
$$

For equal amplitudes, this becomes

$$
I = I_0 \cos^2\left(\frac{\Delta \phi}{2}\right)
$$

## Notes

- The interference pattern is symmetric about the central bright fringe.
- Larger $\lambda$ increases fringe spacing.
- Larger $D$ increases fringe spacing.
- Larger $d$ decreases fringe spacing.

## Connection to Simulation

The simulations use the same basic principle: the fields from the two slits are added first, and intensity is then computed using

$$
I \propto |E_1 + E_2|^2
$$

This is what produces the bright and dark fringe structure numerically.
