# Model Selection

## Candidate models

List only models actually implemented.

| Model | Task | Reason for inclusion |
|---|---|---|
| [Model] | Classification | [Reason] |
| [Model] | Regression | [Reason] |
| [Model] | Clustering | [Reason] |

## Selection rule

Select the final supervised model using validation performance.

For classification, prefer the metric that matches the class-balance/business objective, such as macro-F1 or ROC-AUC.

For regression, report MAE, RMSE and R².

For clustering, report silhouette score and interpretability.

## Test-set discipline

Do not use the test set for model selection or hyperparameter tuning.
