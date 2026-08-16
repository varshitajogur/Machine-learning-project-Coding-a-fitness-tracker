# Methodology

## 1. Preprocessing

Document the exact cleaning operations already implemented in the repository.

## 2. Segmentation

Document:
- window length
- overlap
- sampling frequency
- session boundaries

## 3. Feature Engineering

Document every feature family:
- statistical
- temporal
- frequency-domain
- sensor-specific

## 4. Modelling

Document the existing classification, regression and clustering algorithms.

## 5. Validation

Preferred approach for participant-level sensor data:

- hold out participants/sessions where identifiers exist
- use GroupKFold for cross-validation
- tune hyperparameters only on training/validation data

## 6. Final Evaluation

Evaluate the selected model once on the held-out test set.
