var mix = {
    methods: {
        logoutUser() {
            const csrfToken = this.getCookie('csrftoken');

            this.postData('/api/user/logout/', {}, {
                headers: { 'X-CSRFToken': csrfToken }
            })
            .then(() => {
                console.log('Пользователь вышел из системы');
                window.location.href = '/';
            })
            .catch((error) => {
                console.error('Ошибка при выходе из системы:', error);
            });
        },
        getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === name + '=') {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        },
    }
};
