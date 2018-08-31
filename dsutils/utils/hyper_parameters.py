
class HyperParametersHolderBase(object):
    """
        Base Class
    """
    # This base class is to use super().__setattr__().
    pass

class HyperParametersHolder(HyperParametersHolderBase):
    """
    Ex.
        In [1]: from dsutils.utils import hyper_parameters as hp
           ...:
           ...: class MyHPHolder(hp.HyperParametersHolder):
           ...:     def __init__(self):
           ...:         paramscls_dict = self._get_paramscls_dict()
           ...:         super().__init__(paramscls_dict)
           ...:
           ...:     def _get_paramscls_dict(self):
           ...:         # set what kind of params we use.
           ...:         paramscls_dict = {}
           ...:         paramscls_dict["preprocess"] = ["normalized", "delete_nan"]
           ...:         paramscls_dict["model1"] = ["alpha", "tol"]
           ...:         paramscls_dict["model2"] = ["depth"]
           ...:         return paramscls_dict
           ...:
           ...:     def set_preprocess_params(self, normalized: bool, delete_nan: bool):
           ...:         # wrap self.set_params()
           ...:         self.set_params(paramscls_key="preprocess",\
           ...:                                 normalized=normalized,\
           ...:                                 delete_nan=delete_nan)
           ...:
           ...:     def set_model1_params(self, alpha: float, tol: float):
           ...:         self.set_params(paramscls_key="model1",\
           ...:                                 alpha=alpha, tol=tol)
           ...:
           ...:     def set_model2_params(self, depth: int):
           ...:         self.set_params(paramscls_key="model2", depth=depth)
           ...:

        In [2]: hpholder = MyHPHolder()
           ...:

        In [3]: hpholder
        Out[3]: {'normalized': None, 'delete_nan': None, 'alpha': None, 'tol': None, 'depth': None}

        In [4]: hpholder.alpha = 10.
           ...:

        In [5]: hpholder
        Out[5]: {'normalized': None, 'delete_nan': None, 'alpha': 10.0, 'tol': None, 'depth': None}

        In [6]: hpholder.set_preprocess_params(normalized=True, delete_nan=False)
           ...: hpholder.set_model1_params(alpha=10, tol=0.0001)
           ...: hpholder.set_model2_params(depth=5)
           ...:

        In [7]: hpholder
        Out[7]: {'normalized': True, 'delete_nan': False, 'alpha': 10, 'tol': 0.0001, 'depth': 5}

        In [8]: hpholder.preprocess
           ...:
        Out[8]: {'delete_nan': False, 'normalized': True}
    """
    # FIXME : add type check function
    def __init__(self, paramscls_dict: dict):
        super().__setattr__("paramscls_dict", paramscls_dict)

        _params = {}
        for paramscls_key, paramscls_val in paramscls_dict.items():
            if not isinstance(paramscls_val, list):
                raise ValueError(f"{paramscls_key} : {paramscls_val} is not list.")

            _params[paramscls_key] = self._init_params_dict(paramscls_val)
        super().__setattr__("_params", _params)

    def __setattr__(self, name, value):

        # FIXME : In case that same name exist in differents paramscls dict.
        for paramscls_key in self.paramscls_dict.keys():
            if name in self._params[paramscls_key].keys():
                self._params[paramscls_key][name] = value

    def __getattr__(self, name):
        # pickleで保存する時に何もattrが見つからなかった時にNoneが帰りこけるので，dunderのやつはオリジナルの__getattr__に投げる．
        if name.startswith('__') and name.endswith('__'):
            return super().__getattr__(name)

        if name in self._params.keys():
            name_dict = self._params[name]
            return name_dict

        for paramscls_key in self.paramscls_dict.keys():
            if name in self._params[paramscls_key].keys():
                value = self._params[paramscls_key][name]
                return value

    def set_params(self, paramscls_key: str, **args):
        if not paramscls_key in self._params.keys():
            raise ValueError(f"{paramscls_key} is not defined.")

        _param_keys = self._params[paramscls_key].keys()
        args_keys = args.keys()

        for param_key in _param_keys:
            if param_key in args_keys:
                self._params[paramscls_key][param_key] = args.pop(param_key)

        if len(args) != 0:
            raise ValueError(f"{list(args.keys())} is not defined.")

    def _init_params_dict(self, keys) -> dict:
        params_dict = {key: None for key in keys}
        return params_dict

    @property
    def params(self):
        params = {}

        for paramscls_key, params_dict in self._params.items():
            for key, val in params_dict.items():
                params[key] = val

        return params

    def __repr__(self):
        return repr(self.params)

if __name__ == "__main__":
    pass