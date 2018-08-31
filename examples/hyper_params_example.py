from dsutils.utils import hyper_parameters as hp

class MyHPHolder(hp.HyperParametersHolder):
    def __init__(self):
        paramscls_dict = self._get_paramscls_dict()
        super().__init__(paramscls_dict)

    def _get_paramscls_dict(self):
        paramscls_dict = {}
        paramscls_dict["preprocess"] = ["normalized", "delete_nan"]
        paramscls_dict["model1"] = ["alpha", "tol"]
        paramscls_dict["model2"] = ["depth"]
        return paramscls_dict

    def set_preprocess_params(self, normalized: bool, delete_nan: bool):
        self.set_params(paramscls_key="preprocess",\
                                normalized=normalized,\
                                delete_nan=delete_nan)

    def set_model1_params(self, alpha: float, tol: float):
        self.set_params(paramscls_key="model1",\
                                alpha=alpha, tol=tol)

    def set_model2_params(self, depth: int):
        self.set_params(paramscls_key="model2", depth=depth)


hpholder = MyHPHolder()
hpholder.alpha = 10.

hpholder.set_preprocess_params(normalized=True, delete_nan=False)
hpholder.set_model1_params(alpha=10, tol=0.0001)
hpholder.set_model2_params(depth=5)

hpholder
hpholder.preprocess
