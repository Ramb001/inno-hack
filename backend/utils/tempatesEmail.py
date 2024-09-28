def create_task_notification(title, description, deadline):
    return f"""
    Здравствуйте!

    Вы получили новую задачу:

    Заголовок: {title}
    Описание: {description}
    Дедлайн: {deadline}

    Пожалуйста, выполните задачу в срок.

    С уважением,
    Ваша команда.
    """

def delete_user_from_task_notification(task_title, user_name):
    return f"""
    Здравствуйте!

    Пользователь {user_name} был удален из задачи "{task_title}".

    Если у вас есть вопросы, пожалуйста, свяжитесь с администратором.

    С уважением,
    Ваша команда.
    """

def delete_user_from_organization_notification(user_name, organization_name):
    return f"""
    Здравствуйте!

    Пользователь {user_name} был удален из организации "{organization_name}".

    Если у вас есть вопросы, пожалуйста, свяжитесь с администратором.

    С уважением,
    Ваша команда.
    """

def update_task_status_notification(task_title, new_status):
    return f"""
    Здравствуйте!

    Статус задачи "{task_title}" был изменен на "{new_status}".

    Если у вас есть вопросы, пожалуйста, свяжитесь с администратором.

    С уважением,
    Ваша команда.
    """
