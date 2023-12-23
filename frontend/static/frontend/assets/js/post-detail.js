var mix = {
  methods: {
    getPost() {
      const postId = location.pathname.startsWith('/posts/') ?
        Number(location.pathname.replace('/posts/', '').replace('/', '')) :
        null;
      this.getData(`/api/posts/${postId}/`)
        .then(data => {
          this.post = data.post;
          this.comments = data.comments;
        })
        .catch(() => {
          this.post = {};
          this.comments = [];
          console.warn('Ошибка при получении поста');
        });
    },
    submitComment() {
    const postId = location.pathname.startsWith('/posts/') ?
        Number(location.pathname.replace('/posts/', '').replace('/', '')) :
        null;
      const csrfToken = this.getCookie('csrftoken');
      const payload = {
        text: this.newComment,
      };

      this.postData(`/api/posts/${postId}/comments/create/`, payload, {
        headers: { 'X-CSRFToken': csrfToken }
      })
        .then(() => {
          this.newComment = '';
          this.getPost();
        })
        .catch((error) => {
          console.error('Ошибка при добавлении комментария:', error);
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
  mounted() {
    this.getPost();
  },
  data() {
    return {
      newComment: '',
      post: {},
      comments: []
    };
  },
};


