# 📦 2FA Python Project

## 🛡️ Опис

Цей проєкт реалізує **двофакторну автентифікацію (2FA)** за допомогою **TOTP (Time-based One-Time Password)** та **HOTP (HMAC-based One-Time Password)**. Основна мета — створити OTP ключі, генерувати QR-коди для підключення до автентифікатор-додатків (наприклад, Google Authenticator), а також перевіряти правильність введених одноразових кодів.

## 📁 Структура проєкту

```
.
├── requirements.txt
├── for-authenticator-apps/
│   ├── check.py
│   └── make.py
├── hmac-based-one-time-password/
│   └── main.py
└── time-base-one-time-password/
    └── main.py
```

## 📦 Встановлення

Перед запуском, встановіть залежності:

```bash
pip install -r requirements.txt
```

## 🔧 Сценарії використання

### 🔐 `for-authenticator-apps/make.py`

Генерує TOTP-ключ, зберігає його у файл `2fa.txt`, та створює QR-код для додатку-автентифікатора:

```bash
python for-authenticator-apps/make.py
```

- Вивід:
  - 2FA ключ
  - QR-код збережено у `totp_qr.png`

### ✅ `for-authenticator-apps/check.py`

Зчитує ключ з `2fa.txt` та перевіряє OTP-код, введений користувачем:

```bash
python for-authenticator-apps/check.py
```

- Введіть код з додатку.
- Отримаєте повідомлення про успіх або невдачу автентифікації.

### 🔁 `hmac-based-one-time-password/main.py`

Приклад використання **HOTP (лічильник-залежних OTP)**:

```bash
python hmac-based-one-time-password/main.py
```

- Створює HOTP-коди з базового ключа.
- Перевіряє введені коди послідовно, збільшуючи лічильник.

### ⏳ `time-base-one-time-password/main.py`

Приклад використання **TOTP (час-залежних OTP)**:

```bash
python time-base-one-time-password/main.py
```

- Генерує OTP-код, дійсний протягом 30 секунд.
- Перевіряє правильність введеного користувачем коду.

## 🧪 Залежності

- [`pyotp`](https://pypi.org/project/pyotp/) — реалізація TOTP та HOTP
- [`qrcode`](https://pypi.org/project/qrcode/) — генерація QR-коду

## 📌 Примітки

- Для безпеки не зберігайте 2FA ключі у відкритому вигляді у продакшн-середовищі.
- QR-код можна сканувати через додатки як Google Authenticator, Microsoft Authenticator тощо.
- HOTP підходить для випадків, де клієнт і сервер синхронізуються через лічильник.
- TOTP зручний для мобільних додатків з підтримкою часової синхронізації.
