# Leakage & Validation Strategy

Sensor datasets are particularly vulnerable to leakage because multiple windows may come from the same participant or recording session.

## Risk

If windows from one participant appear in both training and test sets, the model may learn participant-specific sensor signatures rather than general activity patterns.

## Preferred strategy

If participant/session IDs exist:

```python
from sklearn.model_selection import GroupKFold
```

Use participant/session as `groups`.

For a final holdout:

```text
Participants
├── Training participants
└── Unseen test participants
```

## If IDs are unavailable

Document that limitation and avoid claiming participant-independent generalisation.
