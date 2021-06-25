import logging

from aiogram.utils.exceptions import (Unauthorized, InvalidUserId, TelegramAPIError,
                                      CantDemoteChatCreator, MessageNotModified, MessageToDeleteNotFound,
                                      MessageTextIsEmpty, RetryAfter,
                                      CantParseEntities, MessageCantBeDeleted, NetworkError)


from loader import dp


@dp.errors_handler()
async def error_handler(update, exception):
    if isinstance(exception, CantDemoteChatCreator):
        logging.exception("Can't demote chat creator")
        return True

    if isinstance(exception, MessageCantBeDeleted):
        logging.exception("Message can't be deleted")
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logging.exception("Message to delete not found")
        return True

    if isinstance(exception, MessageNotModified):
        logging.exception("Message not modified")
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.exception("Message text is empty")
        return True

    if isinstance(exception, Unauthorized):
        logging.exception(f'Unauthorized: {exception}')
        return True

    if isinstance(exception, InvalidUserId):
        logging.exception(f'InvalidUserId: {exception} \nUpdate {update}')
        return True

    if isinstance(exception, TelegramAPIError):
        logging.exception(f'TelegramAPIError: {exception} \nUpdate {update}')
        return True

    if isinstance(exception, RetryAfter):
        logging.exception(f'RetryAfter: {exception} \nUpdate {update}')
        return True

    if isinstance(exception, CantParseEntities):
        logging.exception(f'CantParseEntities: {exception} \nUpdate {update}')
        return True

    logging.exception(f'Update: {update} \n{exception}')


