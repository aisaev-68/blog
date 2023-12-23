var mix = {
    methods: {
        loginUser() {
            const csrfToken = this.getCookie('csrftoken');
            const username = this.username;
            const password = this.password;
            fetch('/api/user/login/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log('Login successful');
                    window.location.href = '/';  // Redirect to the homepage
                } else {
                    console.error('Login failed:', data.message);
                    document.getElementById('errorMessage').innerText = data.message;
                    document.getElementById('errorContainer').style.display = 'block';
                }
            })
            .catch(error => {
                console.error('Error during login:', error);
            });
        },
        getUserInfo() {
            const csrfToken = this.getCookie('csrftoken');

            // Получение информации о текущем пользователе
            this.getData('/api/user/current_user/', {
                headers: { 'X-CSRFToken': csrfToken }
            })
            .then((userData) => {
                console.log('Информация о пользователе:', userData);

                this.username = userData.username;
            })
            .catch((error) => {
                console.error('Ошибка при получении информации о пользователе:', error);
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
    },
   data() {
     return {
        username: '',
        password: ''
      }
    },
};