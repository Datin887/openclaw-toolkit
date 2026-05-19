# 🛠️ OpenClaw Toolkit

> Модульный набор навыков, скриптов и конфигураций для [OpenClaw](https://github.com/openclaw/openclaw) — AI-агент платформы.

**[English](README.md)**

## 📦 Содержимое

### Навыки (Skills)

| Навык | Описание | Установка |
|-------|----------|-----------|
| **browser-cdp** | Headless браузер через CDP (Chrome DevTools Protocol). Навигация, скриншоты, JS-выполнение, клики, заполнение форм. Работает без GUI — идеально для серверов. | [Подробнее ↓](#browser-cdp) |
| **nemotron-vision** | Мультимодальный анализ изображений через Nemotron-Omni. Анализ скриншотов, графиков, фото, документов. Извлечение текста, описание визуалов. | [Подробнее ↓](#nemotron-vision) |

### Темы (Themes)

| Тема | Описание | Установка |
|------|----------|-----------|
| **Laguna** | Тёплый кремовый + фиолетовый (светлая) / глубокий чёрный + голубой (тёмная). Шрифт Inter, бруталистские тени. С [tweakcn.com](https://tweakcn.com/themes/cmpc347ze000204l580xtaqet). | [INSTALL.md](themes/laguna/INSTALL.md) |

---

## 🚀 Быстрая установка

### Вариант 1: Через агента (рекомендуется)

Попроси своего OpenClaw агента:

> «Клонируй `https://github.com/Datin887/openclaw-toolkit.git`, посмотри список навыков и установи нужные»

Агент сам разберётся что к чему.

### Вариант 2: Вручную

```bash
# 1. Клонируй репозиторий
git clone https://github.com/Datin887/openclaw-toolkit.git

# 2. Скопируй нужный навык в plugin-skills
cp -r openclaw-toolkit/skills/browser-cdp ~/.openclaw/plugin-skills/

# 3. Зарегистрируй навык в конфиге OpenClaw
# Добавь в skills.entries и skills.load.extraDirs (см. документацию навыка)

# 4. Перезапусти gateway
openclaw gateway restart
```

---

## 📋 Навыки

### browser-cdp

**Headless browser automation через Chrome DevTools Protocol.**

**Что умеет:**
- 🌐 Навигация по URL
- 📸 Скриншоты страниц
- ⚡ Выполнение JavaScript
- 🖱️ Клики по элементам
- ✏️ Заполнение форм
- 📄 Извлечение контента страницы
- 🔄 Управление вкладками

**Требования:**
- Chromium headless как systemd сервис (порт 9222)
- Python пакет: `websocket-client`

**Быстрый старт:**
```bash
# Запуск браузера
sudo systemctl start chromium-headless

# Навигация
python3 scripts/browser_cdp.py navigate "https://example.com"

# Скриншот
python3 scripts/browser_cdp.py screenshot /tmp/screenshot.png

# JS-выполнение
python3 scripts/browser_cdp.py evaluate "document.title"
```

**Полная документация:** [skills/browser-cdp/SKILL.md](skills/browser-cdp/SKILL.md)

### nemotron-vision

**Мультимодальный анализ изображений через Nemotron-Omni (бесплатно на OpenRouter).**

**Возможности:**
- 📊 Анализ графиков и диаграмм — извлечение значений, меток, трендов
- 📸 Описание фотографий — объекты, сцены, люди
- 📄 OCR документов — извлечение текста с сохранением структуры
- 🖥️ Анализ UI-скриншотов — описание лейаута и элементов

**Модель:** `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` (256K контекст)

**Быстрый старт:**
```bash
python3 scripts/nemotron_vision.py chart.png "Опиши этот график" --lang ru
```

**Полная документация:** [skills/nemotron-vision/SKILL.md](skills/nemotron-vision/SKILL.md)

---

## 🎨 Темы

### Laguna

Красивая тема с [tweakcn.com](https://tweakcn.com/themes/cmpc347ze000204l580xtaqet).

| Режим | Описание |
|-------|----------|
| Светлая | Тёплый кремовый фон, фиолетовый акцент, шрифт Inter |
| Тёмная | Глубокий чёрный фон, голубой акцент, бруталистские тени |

См. [INSTALL.md](themes/laguna/INSTALL.md).

---

## 📁 Структура

```
openclaw-toolkit/
├── README.md              ← English version
├── README.ru.md           ← Ты здесь (русский)
├── LICENSE                ← MIT License
│
├── skills/                ← Навыки для OpenClaw
│   ├── browser-cdp/       ← Headless браузер через CDP
│   │   ├── SKILL.md       ← Документация навыка
│   │   └── scripts/
│   │       └── browser_cdp.py   ← CDP-хелпер (навигация, скриншоты, JS)
│   └── nemotron-vision/   ← Мультимодальный анализ изображений
│       ├── SKILL.md       ← Документация навыка
│       └── scripts/
│           └── nemotron_vision.py  ← CLI для анализа изображений
│
├── themes/                ← Темы для Control UI
│   └── laguna/            ← Тема Laguna с tweakcn.com
│       ├── theme.json     ← Оригинальный payload tweakcn
│       ├── theme.css      ← CSS-переменные (светлая + тёмная)
│       └── INSTALL.md     ← Инструкция по установке
│
├── scripts/               ← Вспомогательные скрипты
├── configs/               ← Шаблоны конфигураций
└── docs/                  ← Дополнительная документация
```

### Описание директорий

| Директория | Назначение |
|------------|------------|
| `skills/` | Навыки для OpenClaw — каждая подпапка это самодостаточный навык с `SKILL.md` и скриптами |
| `themes/` | Темы для Control UI — JSON/CSS темы для веб-интерфейса OpenClaw |
| `scripts/` | Автономные скрипты (статус агента, сборщики логов, утилиты) |
| `configs/` | Шаблоны конфигураций и примеры настройки OpenClaw |
| `docs/` | Дополнительная документация, гайды и заметки |

## 📜 Лицензия

MIT — делай что хочешь. Подробности в [LICENSE](LICENSE).
