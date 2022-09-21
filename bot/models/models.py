from aiogram.fsm.state import State, StatesGroup


class InputForm(StatesGroup):
    method = State()
    query = State()
