import numpy as np


def base_get_indices(X):
    return np.ones(len(X), dtype=bool)


base_params = {
    'objective': 'reg:linear',
    'silent': 1,
    'num_rounds': 1000,
    'gamma': 0.0,
    'eta': 0.02,
    'max_depth': 8,
    'min_child_weight': 6,
    'subsample': 0.7,
    'colsample_bytree': 0.6,
}


def supplier66_get_indices(X):
    return (X.supplier == 'S-0066')


supplier66_params = {
    'objective': 'reg:linear',
    'silent': 1,
    'num_rounds': 1000,
    'gamma': 0.0,
    'eta': 0.02,
    'max_depth': 8,
    'min_child_weight': 6,
    'subsample': 0.7,
    'colsample_bytree': 0.6,
}


def supplier41_get_indices(X):
    return (X.supplier == 'S-0041')


supplier41_params = {
    'objective': 'reg:linear',
    'silent': 1,
    'num_rounds': 1000,
    'gamma': 0.0,
    'eta': 0.02,
    'max_depth': 8,
    'min_child_weight': 6,
    'subsample': 0.7,
    'colsample_bytree': 0.6,
}


def supplier72_get_indices(X):
    return (X.supplier == 'S-0072')


supplier72_params = {
    'objective': 'reg:linear',
    'silent': 1,
    'num_rounds': 1000,
    'gamma': 0.0,
    'eta': 0.02,
    'max_depth': 8,
    'min_child_weight': 6,
    'subsample': 0.7,
    'colsample_bytree': 0.6,
}


def supplier54_get_indices(X):
    return (X.supplier == 'S-0054')


supplier54_params = {
    'objective': 'reg:linear',
    'silent': 1,
    'num_rounds': 1000,
    'gamma': 0.0,
    'eta': 0.02,
    'max_depth': 8,
    'min_child_weight': 6,
    'subsample': 0.7,
    'colsample_bytree': 0.6,
}


def supplier26_get_indices(X):
    return (X.supplier == 'S-0026')


supplier26_params = {
    'objective': 'reg:linear',
    'silent': 1,
    'num_rounds': 1000,
    'gamma': 0.0,
    'eta': 0.02,
    'max_depth': 8,
    'min_child_weight': 6,
    'subsample': 0.7,
    'colsample_bytree': 0.6,
}


def supplier13_get_indices(X):
    return (X.supplier == 'S-0013')


supplier13_params = {
    'objective': 'reg:linear',
    'silent': 1,
    'num_rounds': 1000,
    'gamma': 0.0,
    'eta': 0.02,
    'max_depth': 8,
    'min_child_weight': 6,
    'subsample': 0.7,
    'colsample_bytree': 0.6,
}


def supplier58_get_indices(X):
    return (X.supplier == 'S-0058')


supplier58_params = {
    'objective': 'reg:linear',
    'silent': 1,
    'num_rounds': 1000,
    'gamma': 0.0,
    'eta': 0.02,
    'max_depth': 8,
    'min_child_weight': 6,
    'subsample': 0.7,
    'colsample_bytree': 0.6,
}


def supplier64_get_indices(X):
    return (X.supplier == 'S-0064')


supplier64_params = {
    'objective': 'reg:linear',
    'silent': 1,
    'num_rounds': 1000,
    'gamma': 0.0,
    'eta': 0.02,
    'max_depth': 8,
    'min_child_weight': 6,
    'subsample': 0.7,
    'colsample_bytree': 0.6,
}


def supplier62_get_indices(X):
    return (X.supplier == 'S-0062')


supplier62_params = {
    'objective': 'reg:linear',
    'silent': 1,
    'num_rounds': 1000,
    'gamma': 0.0,
    'eta': 0.02,
    'max_depth': 8,
    'min_child_weight': 6,
    'subsample': 0.7,
    'colsample_bytree': 0.6,
}


common_suppliers_1 = [
    'S-0066',
    'S-0041',
    'S-0072',
    'S-0054',
]


def uncommon_suppliers_1_get_indices(X):
    return ~X.supplier.isin(common_suppliers_1)


uncommon_suppliers_1_params = {
    'objective': 'reg:linear',
    'silent': 1,
    'num_rounds': 1000,
    'gamma': 0.0,
    'eta': 0.02,
    'max_depth': 8,
    'min_child_weight': 6,
    'subsample': 0.7,
    'colsample_bytree': 0.6,
}


common_suppliers_2 = [
    'S-0066',
    'S-0041',
    'S-0072',
    'S-0054',
    'S-0026',
    'S-0013',
    'S-0058',
]


def uncommon_suppliers_2_get_indices(X):
    return ~X.supplier.isin(common_suppliers_2)


uncommon_suppliers_2_params = {
    'objective': 'reg:linear',
    'silent': 1,
    'num_rounds': 1000,
    'gamma': 0.0,
    'eta': 0.02,
    'max_depth': 8,
    'min_child_weight': 6,
    'subsample': 0.7,
    'colsample_bytree': 0.6,
}
