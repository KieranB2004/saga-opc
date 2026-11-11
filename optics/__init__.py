"""
=================================================================================
AI ASSISTANCE DISCLOSURE - optics module
=================================================================================
This file was created with AI assistance. It provides scaffolding for Fourier-domain 
aerial image simulation in 193 nm DUV lithography.

Student verification required:
1. Read docstring explaining physical principles of scalar diffraction imaging
2. Implement FFT-based optical simulation computation
3. Verify results match known analytical cases (Airy pattern, uniform aperture)
4. Test with different NA and wavelength parameters

Date created: 2026-11-11
=================================================================================
"""

from optics.aerial_image import compute_aerial_image
from optics.frequency_response import get_frequency_response


__version__ = "0.1.0-dev"
