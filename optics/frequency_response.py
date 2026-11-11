"""
=================================================================================
AI ASSISTANCE DISCLOSURE - optics/frequency_response.py
=================================================================================
This file was created with AI assistance. It provides a scaffold for computing 
the optical transfer function (OTF) frequency response for the imaging system.

Student verification required:
1. Read docstring explaining OTF mathematical formulation
2. Implement circular frequency cutoff calculation
3. Verify output matches expected OTF shape in frequency domain
4. Test with different NA and wavelength combinations

Date created: 2026-11-11
=================================================================================
"""

import numpy as np
from typing import Tuple


# ================================================================================
# FUNCTION: get_frequency_response
# ================================================================================

def get_frequency_response(
    numerical_aperture: float = 0.93,
    coherence_factor_sigma: float = 0.75,
    wavelength_nm: float = 0.193,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute optical transfer function (OTF) frequency response.
    
    Physical model explanation:
      
      The optical transfer function OTF describes which spatial frequencies 
      can pass through the imaging system and how they're attenuated. For 
      a diffraction-limited coherent system, the OTF is an ideal circular 
      low-pass filter.
      
      Mathematical formulation:
        
        Maximum transmissible frequency (cutoff):
          f_cutoff = NA / λ
        
        where:
          NA = numerical aperture (0.93)
          λ = wavelength in same units as frequency array
            
        In practice, for FFT implementation:
          We represent OTF on discrete frequency grid matching simulation dimensions
          
      Frequency unit convention:
        - Can be expressed as cycles per micron (physical units)
        - Or cycles per pixel (dimensionless)
        - This function returns both if needed
        
    Physical interpretation of parameters:
      numerical_aperture: Lens NA determines maximum passband frequency
      coherence_factor_sigma: Affects OTF shape (ignored in simplified model)
      wavelength_nm: Exposure wavelength sets diffraction scale
      
    Parameters:
      numerical_aperture (float, default=0.93): Lens NA value  
      coherence_factor_sigma (float, default=0.75): Partial coherence factor
      wavelength_nm (float, default=0.193): DUV exposure wavelength in nm
      
    Returns:
      Tuple of two arrays:
        freq_grid: 2D array of spatial frequencies
                   shape matches optical simulation grid dimensions
                   
        otf_values: OTF magnitude at each frequency point
                    values are 1.0 within passband, 0.0 outside
                      
    Expected output characteristics:
      - freq_grid ranges from negative to positive in both dimensions
      - Maximum absolute frequency equals f_cutoff = NA / wavelength  
      - otf_values is circular mask with radius at cutoff frequency
      
    TODO-frequency-response-implementation-steps: 
      After implementing, verify against analytical results:
      
      For a 2D Fourier grid of size (Ny, Nx) pixels with resolution px_per_um:
      
      1. Compute physical frequency limits:
         f_max = NA / wavelength_in_microns
        
      2. Map to discrete frequency indices:
         freq_range = np.fft.fftfreq(Ny, d=1/px_per_um)  # for y-axis
         same for x-axis
            
      3. Create OTF mask:
         freq_mag = sqrt(fx² + fy²)
         otf = (freq_mag <= f_max) * 1.0
      
    Raises:
      ValueError: If numerical_aperture non-positive or wavelength invalid
    
    Implementation after TODO marker below...
    """
    # TODO-frequency-response-student-implementation-start
    
    student_code_here
    
    raise NotImplementedError(
        "Student must implement OTF frequency response computation."
    )
