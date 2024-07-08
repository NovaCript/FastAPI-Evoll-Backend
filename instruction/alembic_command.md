# Alemdic

Что бы миграции по новым таблицам прошли, из необходимо поместить\
в файл по пути:

```
core.models.__init__.py

__all__ = (
    "db_helper",
    "Base",
    "User",
    
    "Имя новой таблицы"
)

from .db_helper import db_helper
from .base import Base
from users.models import User

from модуль import Имя новой таблицы
```

Пример с таблицей user.

---
Command:

- После создания или изменения таблицы, выполняем команду:
```
alembic revision --autogenerate -m "пишем что конкретно сделали"
```
- Обновить базу данных до актуального состояния:
```
alembic upgrade head
```
- Обновить базу данных до нужной версии:
```
alembic upgrade d715f2b032a5
```
- Откатиться до нужной версии:
```
alembic downgrade d715f2b032a5
```

### ps. Всегда проверяем что в файле версии после команды --autogenerate, так как он может дропать столбцы, что может привести к потере данных.
