var mix = {
    methods: {
        createPost() {
            const csrfToken = this.getCookie('csrftoken');
            const payload = {
                title: this.post.title,
                content: this.post.content
            };

            this.postData('/api/posts/create/', payload, {
                headers: { 'X-CSRFToken': csrfToken }
            })
            .then((data) => {
                console.log('Пост создан:', data);
                // Перенаправление на страницу с созданным постом
                window.location.href = '/posts/' + data.id;
            })
            .catch((error) => {
                console.error('Ошибка при создании поста:', error);
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
        post: {
            title: '',
            content: ''
        }
      }
    },
};

