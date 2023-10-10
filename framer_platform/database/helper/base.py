from .. import AsyncSession
from .. import BASE as ModelBase


class BaseHelper:
    @classmethod
    def create_one(
        cls, async_session: AsyncSession, model_inistrance: ModelBase
    ) -> None:
        ...
