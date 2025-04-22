
# Документація Python проєкту з реалізацією 2FA

## Опис проєкту

Цей проєкт демонструє різні методи реалізації двофакторної утентифікації (2FA) у Python за допомогою біблотеки pyotp. Проєкт містить три основні компоненти:
1. Генерація та перевірка TOTP (Time-based One-Time Password) для автентифікаційних додатків
2. Реалізація HOTP (HMAC-based One-Time Password)
3. Базова реалізація TOTP

## Встановлення

1. Клонуйте репозиторій
   ```bash
   git clone https://github.com/hanashiko/2fa.git
   cd 2fa
   ```
   
2. Встановість необхідні залежності
   ```bash
   pip install -r requirements.txt
   ```

## Структура проєкту

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

## Деталі реалізації

1. Для автентифікаційних додатків (Google Authenticator тощо)

`make.py`
Генерує секретний ключ та QR-код для додавання до автентифікаційного додатку.

Функції:
- `generate_otp_key()`: Генерує випадковий
