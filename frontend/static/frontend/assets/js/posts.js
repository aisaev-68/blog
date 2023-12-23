var mix = {
  methods: {
    getPosts() {
      this.getData('/api/posts/'
      ).then((data) => {
          this.postCards = data;
        })
        .catch(() => {
          console.warn('Ошибка при получении книг');
        });
    },

  },
  mounted() {
    this.getPosts();
  },
  data() {
    return {
      postCards: [],
    };
  },
};


