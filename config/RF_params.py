
# RF_processing

RF_params = {
    'n_estimators': 100,
    'min_samples_split': 2,
    'criterion': 'squared_error',
    'max_features': 'sqrt',
    'min_samples_leaf': 1,
    'random_state': 42
}


RF_predict = {
    "dataset": "utils/example_dataset_predict.xlsx",
    "features": ['logpre','logvpd',	'chi', 'logppfd', 'gtmp', 'AI', 'loggpp', 'soc', 'logtp','logtn'],
    "target": 'fapar',
    "normalize": True,
    "min_max_values": None
}
