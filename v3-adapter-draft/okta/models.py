import inspect

from swagger_client import models as swagger_models
from .helpers import to_snake_case


def init_adapter(self, config=None):
    if config is None:
        config = {}
    else:
        config = {to_snake_case(key): config[key] for key in config}
    super(self.__class__, self).__init__(**config)


@classmethod
def from_kwargs(cls, **kwargs):
    return cls(config=kwargs)


swagger_models = inspect.getmembers(swagger_models, predicate=inspect.isclass)

for model_name, model_class in swagger_models:
    model = type(model_name, (model_class,), {'__init__': init_adapter, 'from_kwargs': from_kwargs})
    globals()[model.__name__] = model

