var mix = {
    data() {
        return {
            username: '',
            email: '',
            first_name: '',
            last_name: '',
            password: '',
            password_confirm: '',
            errorMessage: '',
            errorContainer: false,
        };
    },
    methods: {
        registerUser() {
            const csrfToken = this.getCookie('csrftoken');
            const payload = {
                username: this.username,
                email: this.email,
                first_name: this.first_name,
                last_name: this.last_name,
                password: this.password,
                password_confirm: this.password_confirm
            };


            fetch('/api/user/register/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            })
            .then(response => response.json())
            .then(data => {
                if (!data.success) {
                    let errorMessage = '';
                    if (data.message.hasOwnProperty('non_field_errors')) {
                        errorMessage = data.message.non_field_errors[0];
                    } else if (data.message.hasOwnProperty('email')) {
                        errorMessage = data.message.email[0];
                     } else if (data.message.hasOwnProperty('username')) {
                        errorMessage = data.message.username[0];
                    } else {
                        errorMessage = 'Unknown error occurred';
                    }

                    console.error('Register failed:', errorMessage);
                    this.errorMessage = errorMessage;
                    this.errorContainer = true;
                } else {
                    console.log('Register successful');
                    window.location.href = '/login/';
                }
            })
            .catch(error => {
                console.error('Ошибка при регистрации:', error);
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



