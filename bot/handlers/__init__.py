from aiogram import Router


def setup_router():
    from . import default, executor

    router = Router()
    router.include_router(default.router)
    router.include_router(executor.router)

    return router
