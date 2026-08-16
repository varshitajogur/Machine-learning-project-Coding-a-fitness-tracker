# Machine Learning for the Quantified Self (ML4QS)

An end-to-end machine-learning project exploring how wearable sensor and Quantified Self data can be transformed into features for activity recognition, regression and clustering.

The project combines **Python and R** for preprocessing, statistical analysis, feature engineering, modelling and visualisation.

## Project Workflow

```text
Raw Sensor Data
      ↓
Data Cleaning & Validation
      ↓
Time-Series Segmentation
      ↓
Feature Engineering
      ↓
Exploratory & Statistical Analysis
      ↓
Train / Validation / Test Strategy
      ↓
Classification | Regression | Clustering
      ↓
Model Comparison
      ↓
Evaluation & Error Analysis
      ↓
Predictions & Insights
```

## Current Repository

The original repository contains Python3/PythonCode/RCode implementations covering sensor preprocessing, visualisation, classification, regression and related analysis. The PythonCode directory includes chapter-specific scripts for visualisation, crowdsignals processing, classification and regression. 

This upgrade adds the missing **results, methodology, reproducibility, model-comparison and validation layer** around that existing work.

## Key Questions

1. Which engineered sensor features are most informative for activity recognition?
2. Which classification algorithm performs best on unseen sensor data?
3. How does the choice of train/test strategy affect reported performance?
4. Which features explain regression performance?
5. Can unsupervised clustering recover meaningful activity structure?
6. What are the main sources of model error?

## Machine Learning Tasks

### Classification
Activity recognition from engineered sensor features.

### Regression
Prediction of continuous target variables where supported by the existing notebooks.

### Clustering
Unsupervised exploration of sensor/activity patterns.

## Model Evaluation

The project should report actual results in:

```text
results/
├── classification_metrics.csv
├── regression_metrics.csv
├── clustering_metrics.csv
├── model_comparison.csv
├── feature_importance.csv
└── error_analysis.csv
```

Do not enter invented metrics. Generate them by running the existing models and the evaluation scripts/notebooks.

## Important Time-Series / Sensor Validation

Randomly splitting adjacent windows can cause leakage when windows from the same participant/session appear in both training and test data.

Where participant/session identifiers are available, the preferred evaluation is:

**Group-aware train/test split or GroupKFold**, using participant/session as the grouping variable.

If those identifiers are unavailable, document the limitation explicitly.

## Reproducibility

Record:

- Python version
- R version
- package versions
- dataset version/source
- random seed
- train/test strategy
- feature count
- sample count
- model hyperparameters

The project includes:

```text
config/
├── environment.yml
└── requirements.txt
```

and:

```text
docs/
├── dataset.md
├── methodology.md
├── feature_engineering.md
├── model_selection.md
├── leakage_and_validation.md
└── limitations.md
```

## Results

### Classification

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Baseline | [RUN] | [RUN] | [RUN] | [RUN] | [RUN] |
| Logistic Regression | [RUN] | [RUN] | [RUN] | [RUN] | [RUN] |
| Random Forest | [RUN] | [RUN] | [RUN] | [RUN] | [RUN] |
| [Other existing model] | [RUN] | [RUN] | [RUN] | [RUN] | [RUN] |

### Regression

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Baseline | [RUN] | [RUN] | [RUN] |
| [Existing model] | [RUN] | [RUN] | [RUN] |

### Clustering

| Method | Number of clusters | Silhouette | Davies-Bouldin |
|---|---:|---:|---:|
| K-Means | [RUN] | [RUN] | [RUN] |
| [Existing method] | [RUN] | [RUN] | [RUN] |

## Model Selection

The final model should be selected using validation performance, not test-set performance.

The test set should be used once for final unbiased evaluation.

## Feature Importance

Report the most influential features for the selected model in:

`results/feature_importance.csv`

For tree-based models, report feature importance. For linear models, report standardised coefficients where appropriate.

## Error Analysis

Model evaluation should go beyond a single accuracy number.

Report:

- Confusion matrix
- Per-class precision/recall/F1
- Most confused activity pairs
- Regression residuals
- Outlier/error examples
- Performance by participant/session where possible

## Statistical Analysis

The project uses R/SciPy-based statistical analysis where appropriate.

Statistical tests should report:

- Test statistic
- p-value
- Effect size
- Confidence interval where applicable

A statistically significant p-value should not be interpreted as evidence of causality.

## Results Interpretation

Only claim that one model is better when the measured evaluation supports that conclusion.

Avoid statements such as:

> "Random Forest is the best model."

until the model comparison table has been generated.

Prefer:

> "Random Forest achieved the highest held-out F1 score of X among the evaluated models."

## Limitations

1. Wearable sensor data can contain participant-specific patterns.
2. Adjacent time-series windows can create leakage if the split strategy is not group-aware.
3. Sensor placement and device differences can affect generalisation.
4. A model trained on a limited participant population may not generalise to unseen users.
5. Activity classes may be imbalanced.
6. Regression performance depends on the quality and range of the target variable.
7. Clustering quality does not necessarily imply meaningful real-world activity categories.

## Future Work

- Group-aware cross-validation across participants
- Hyperparameter optimisation
- Automated feature selection
- Deep learning for sequential sensor data
- Real-time wearable inference
- Explainable AI
- Interactive activity dashboard
- External validation on an independent dataset

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and machine learning |
| R | Statistical analysis |
| Pandas | Data manipulation |
| NumPy | Numerical computing |
| SciPy | Statistical/scientific computing |
| Scikit-learn | Machine learning |
| Matplotlib | Visualisation |
| Jupyter | Interactive analysis |
| Docker | Reproducible environment |

## Academic Positioning

This project demonstrates a complete ML workflow for sensor-based behavioural data:

**Time-Series Data → Feature Engineering → Statistical Analysis → Supervised/Unsupervised Learning → Model Validation → Error Analysis**

The strongest Master's-level contribution is not the number of algorithms used, but the quality of the **experimental design, validation strategy, model comparison and interpretation**.

## Repository Structure

```text
.
├── Python3/
├── PythonCode/
├── RCode/
├── results/
├── docs/
├── notebooks/
├── tests/
├── figures/
├── config/
└── README.md
```
