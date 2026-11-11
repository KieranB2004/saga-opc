# AI Usage Disclosure Document

## Purpose

This document records all AI-assisted development activities for the SAGA-OPC project to comply with University of Alberta Student Academic Integrity Policy.

---

## AI Tools Used

### OpenCode Platform (AI Assistance)

**Date Range:** November 9, 2026 – November 11, 2026  
**Purpose:**
- Generated initial scaffolding and code templates for each module
- Provided documentation string templates with TODO markers
- Explained mathematical formulations for optical simulation, GP regression, GA operators  
- Created test case specifications and edge case examples

**Specific Contributions by AI:**
1. **Planning Phase (Nov 9):**
   - Requirements analysis and scientific foundations
   - Architecture design proposals with Mermaid diagrams
   - Test case drafting with parameterization strategies
   
2. **Implementation Scaffolding (Nov 11):**
   - Created `requirements.txt` with dependency specifications  
   - Generated `config/parameters.yaml` with all configurable parameters
   - Produced API specification document for each module
   - Wrote templated code files with docstrings and TODO markers
   - Created `.gitignore` file for Python project conventions
   - Drafted README.md with complete project documentation

**Verification Required by Student:**
- [ ] Read each docstring and understand mathematical explanations
- [ ] Implement actual function logic marked with TODO comments
- [ ] Test each implemented function to ensure correctness
- [ ] Verify against analytical solutions where possible
- [ ] Document any deviations from AI-generated scaffolding

---

## Files Created with AI Assistance

All files below were created with OpenCode AI assistance as documented at the top of each file:

```
geometry/__init__.py
geometry/import_gds.py  
geometry/export_mask_as_polygons.py
geometry/convert_to_simulation_grid.py

optics/__init__.py
optics/aerial_image.py
optics/frequency_response.py

mask/__init__.py
mask/chromosome.py

optimization/ga/__init__.py
optimization/ga/population.py
optimization/ga/crossover.py
optimization/ga/mutation.py
optimization/ga/optimizer.py

surrogate/__init__.py
surrogate/gp_model.py

saga/__init__.py
saga/optimizer.py

visualization/__init__.py
visualization/progress_plotter.py
visualization/pattern_comparator.py

experiments/__init__.py
experiments/manager.py
experiments/comparison.py

tests/* (test directory structure and templates)

requirements.txt
config/parameters.yaml
.gitignore
README.md
```

---

## Verification Protocol

Before submitting any student code for evaluation:

### For Each File:
1. ✅ Verify the AI disclosure header is present at top of file
2. ✅ Read docstrings and understand what each function does
3. ✅ Implement logic in TODO-marked sections (if applicable)
4. ✅ Run tests to verify implementation correctness
5. ✅ Compare results against known analytical cases where possible

### Final Submission Checklist:
- [ ] All TODO markers either implemented or commented as "intentionally left"  
- [ ] Test suite passes without errors
- [ ] Code follows existing patterns in repository
- [ ] Documentation accurate for implemented functionality
- [ ] No credentials or secrets hardcoded

---

## Independent Verification Steps

To verify AI-generated explanations are correct:

### Optical Simulation Math:
1. Check that FFT-based implementation matches analytical Fourier transform
2. Verify frequency cutoff = NA / wavelength  
3. Test with uniform mask → should produce uniform aerial image

### Gaussian Process Regression:
1. Implement simple 1D GP and compare against sklearn reference
2. Verify mean prediction lies between training y-values (mostly)
3. Confirm variance is always non-negative

### Genetic Algorithm Operators:
1. Manually trace one generation of GA with paper/pencil  
2. Verify crossover produces correct number of children
3. Test mutation preserves population size exactly

---

## Academic Integrity Statement

By completing the verification steps above, the student certifies:

- All AI-generated code and explanations have been independently verified
- Understanding is sufficient to explain implementation decisions
- Implementation reflects personal learning and development effort  
- No confidential or proprietary information uploaded to external services
- Results accurately reported without fabrication of data or citations

---

## Questions?

Contact instructor if clarification needed on:
- What constitutes acceptable AI assistance
- How to properly verify complex mathematical implementations
- Edge cases in academic integrity policy

**Remember:** The goal is learning, not just code completion. Take time to understand each component before moving forward.
