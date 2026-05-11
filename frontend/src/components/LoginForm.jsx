import React, { useState } from 'react';

export default function AuthPage() {
    const [mode, setMode] = useState('login');
    const [form, setForm] = useState({
        name: '',
        email: '',
        password: '',
        confirmPassword: '',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setForm((prev) => ({ ...prev, [name]: value }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        if (mode === 'register' && form.password !== form.confirmPassword) {
            alert('Пароли не совпадают');
            return;
        }

        console.log(mode === 'login' ? 'Авторизация:' : 'Регистрация:', form);
    };

    const isLogin = mode === 'login';

    return (
        <div>
            <h1>{isLogin ? 'Вход' : 'Регистрация'}</h1>

            <div>
                <button type="button" onClick={() => setMode('login')}>
                    Войти
                </button>
                <button type="button" onClick={() => setMode('register')}>
                    Зарегистрироваться
                </button>
            </div>

            <form onSubmit={handleSubmit}>
                {!isLogin && (
                    <div>
                        <label>Имя</label>
                        <input
                            type="text"
                            name="name"
                            value={form.name}
                            onChange={handleChange}
                            required
                        />
                    </div>
                )}

                <div>
                    <label>Email</label>
                    <input
                        type="email"
                        name="email"
                        value={form.email}
                        onChange={handleChange}
                        required
                    />
                </div>

                <div>
                    <label>Пароль</label>
                    <input
                        type="password"
                        name="password"
                        value={form.password}
                        onChange={handleChange}
                        required
                    />
                </div>

                {!isLogin && (
                    <div>
                        <label>Повторите пароль</label>
                        <input
                            type="password"
                            name="confirmPassword"
                            value={form.confirmPassword}
                            onChange={handleChange}
                            required
                        />
                    </div>
                )}

                <button type="submit">
                    {isLogin ? 'Войти' : 'Создать аккаунт'}
                </button>
            </form>
        </div>
    );
}
