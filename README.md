# Telegram Bot Starter (Python + aiogram v3)

Два режима:
- **Polling (локально, без домена)** — `python app.py`
- **Webhook (прод, с публичным URL)** — контейнер/хостинг запускает `python webhook_app.py`

## 0) Подготовка локально
1. Установи Python 3.11+ и Git.
2. Склонируй репозиторий и зайди в папку.
3. Создай виртуальную среду и установи зависимости:
   ```bash
   python -m venv .venv
   # Mac/Linux:
   source .venv/bin/activate
   # Windows:
   # .venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. Скопируй `.env.example` в `.env` и впиши `BOT_TOKEN` из BotFather.

### Запуск локально (Polling)
```bash
python app.py
```
Напиши боту в Telegram — он ответит.

---

## Деплой бесплатно: Render.com (клики)
1. Залей код на GitHub: **New → Create a new repository → Upload existing files**.
2. Открой https://dashboard.render.com → **New +** → **Web Service**.
3. **Connect a repository** → выбери свой репозиторий → **Connect**.
4. Настройки:
   - **Name**: любое (например, `tg-bot-starter`)
   - **Region**: ближайший к тебе
   - **Runtime**: Docker
   - **Branch**: `main`
   - Остальное по умолчанию → **Create Web Service**
5. После билда открой вкладку **Environment** → **Add Environment Variable** и добавь:
   - `BOT_TOKEN` = токен от BotFather
   - `PUBLIC_URL` = адрес приложения Render (например, `https://tg-bot-starter.onrender.com`), появится на вкладке **Overview**
   - `WEBHOOK_SECRET` = длинная случайная строка (например, сгенерируй на https://www.random.org/strings/)
   - `PORT` = `10000` или оставь по умолчанию, если Render уже прокинул порт (у Render переменная `$PORT` прокидывается сама)
6. Нажми **Manual Deploy → Deploy latest commit**.
7. Проверь `https://<твоё-имя>.onrender.com/healthz` — должно вернуть `ok`.
8. Напиши боту в Telegram — он должен отвечать (вебхук ставится автоматически при старте).

---

## Деплой бесплатно: Railway.app (клики)
1. Залей код на GitHub (если ещё не).
2. Открой https://railway.app → **Login** → **New Project** → **Deploy from GitHub repo**.
3. Выбери репозиторий и подтверди.
4. Railway определит Dockerfile и соберёт образ.
5. В **Variables** добавь:
   - `BOT_TOKEN` = токен от BotFather
   - После первого деплоя смотри URL в **Settings → Domains**. Добавь:
     - `PUBLIC_URL` = `https://<domain-from-railway>`
   - `WEBHOOK_SECRET` = длинная случайная строка
   - (При необходимости) `PORT` = `8080` (или используй тот, который выдаёт Railway — он прокидывает `$PORT`)
6. Нажми **Deploy** или **Redeploy**.
7. Зайди на `https://<domain-from-railway>/healthz` — ответ `ok`.
8. Напиши боту в Telegram.

---

## Tips
- Если хочешь начать с Polling и без Docker: в Render создавай **Background Worker** и команду запуска `python app.py`. Но webhook надёжнее.
- Секреты храни только в переменных окружения (не коммить `.env`).
- Если бот не отвечает — смотри логи на вкладке **Logs** (и проверь, что `PUBLIC_URL` корректный).
