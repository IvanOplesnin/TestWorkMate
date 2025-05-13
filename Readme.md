# Payroll Report Generator

Проект на Python для чтения данных сотрудников из CSV-файлов и генерации различных отчетов (например, по выплатам). Код легко расширяется: добавление новых форматов отчётов сводится к написанию отдельного модуля-форматтера и регистрации в системе.

---

## 📁 Структура проекта

```
your_project/
├── src/
│   ├── __main__.py         # точка входа
│   ├── cli.py              # парсинг аргументов и запуск
│   ├── constants.py        # константы (REPLACEMENT_VALUES)
│   ├── models/
│   │   └── employee.py     # dataclass Employee
│   ├── utils/
│   │   └── casting.py      # replace_values, cast_names
│   ├── readers/
│   │   └── csv_reader.py   # чтение CSV и преобразование в Employee
│   ├── registry.py         # реестр и декоратор форматтеров
│   └── formatters/
│       └── payout.py       # форматтер отчёта payout
└── tests/                  # pytest-тесты для каждого модуля
```

### 🖼️ Как рисовать дерево проекта

1. **ASCII-дерево вручную**: оформляете его в Markdown с отступами и символами:

   ```
   your_project/
   ├── src/
   │   └── ...
   └── tests/
   ```
2. **Команда `tree`** (Linux/macOS) или `npm install -g tree-cli` (Windows):

   ```bash
   tree -L 2 your_project/
   ```
3. **Mermaid**: используйте диаграмму типа `tree` в Markdown-поддерживающем Mermaid:

   ```mermaid
   tree
     root your_project
     src [src]
     tests [tests]
   ```

Эти методы помогут быстро и наглядно отобразить иерархию проекта.

> Ниже приведена визуализация структуры проекта в синтаксисе Mermaid:

```mermaid
tree
  root your_project
  src [src]
  src --> mainpy("__main__.py")
  src --> clipy("cli.py")
  src --> constantspy("constants.py")
  src --> models
  models --> employeepy("employee.py")
  src --> utils
  utils --> castingpy("casting.py")
  src --> readers
  readers --> csvreaderpy("csv_reader.py")
  src --> registrypy("registry.py")
  src --> formatters
  formatters --> payoutpy("payout.py")
  root --> tests
  tests --> "test_*.py"
```

---

## 🏷️ Добавление алиасов колонок

Если вы хотите расширить список распознаваемых названий колонок для CSV, откройте файл `src/constants.py` и найдите словарь `REPLACEMENT_VALUES`. Добавьте или отредактируйте пары ключ: список\_алиасов, например:

```python
REPLACEMENT_VALUES = {
    # ...
    'rate': ['hourly_rate', 'salary', 'tariff'],
    'department': ['dept', 'division'],
}
```

Где ключ — каноническое имя поля, а список — альтернативные названия, которые будут автоматически распознаваться при чтении CSV.

---

## 🚀 Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/<your-username>/payroll-report-generator.git
   cd payroll-report-generator
   ```

2. Создайте и активируйте виртуальное окружение (рекомендуется):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate    # Linux/macOS
   .\.venv\Scripts\activate   # Windows
   ```

3. Установите зависимости для разработки и тестирования:

   ```bash
   pip install -U pytest pytest-cov
   ```

> Все остальные зависимости входят в стандартную библиотеку Python.

---

## 🎯 Использование

1. Подготовьте CSV-файлы с любыми именами колонок из набора `{id, email, name, department, hours_worked, rate}` (альясами будут `hourly_rate`, `salary` для ставки).
2. Запустите генерацию отчёта:

   ```bash
   python -m src --format payout data1.csv data2.csv --report output.txt
   ```
3. Готовый отчёт появится в `output.txt`, а также будет выведен в консоль.

### Параметры CLI

* `files` (обязательный): пути к CSV-файлам.
* `-f, --format` (по умолчанию `payout`): формат отчёта.
* `--report` (по умолчанию `output.txt`): имя выходного файла.

---

## ✨ Расширяемость: добавление нового формата отчёта

1. Создайте новый файл `src/formatters/<your_report>.py`.
2. Импортируйте `registry` и `Employee`:

   ```python
   from ..registry import registry
   from ..models.employee import Employee
   ```
3. Определите функцию-форматтер и зарегистрируйте её:

   ```python
   @registry.register("your_report")
   def format_report_your(employees: list[Employee]) -> str:
       """Описание вашего отчёта для `--help`."""
       # ваша логика...
       return output_str
   ```
4. Запустите скрипт с `--format your_report`.

> Благодаря реестру вам не нужно изменять код CLI или registry: новый формат автоматически появится в списке доступных.

---

## 🔍 Тестирование

В проекте используются `pytest` и `pytest-cov`.

```bash
pytest --cov=src
```

Цель покрытия — ≥ 80% по важным модулям. Папка `tests/` содержит тесты для:

* `models/employee.py`
* `utils/casting.py`
* `readers/csv_reader.py`
* `registry.py`
* `formatters/payout.py`

---

## 🛠️ Стиль и линтинг

* Код форматируется согласно PEP 8.
* Рекомендуется запускать линтер (например, `flake8`) перед коммитом.

---

## 📝 Лицензия

MIT License © 2025
