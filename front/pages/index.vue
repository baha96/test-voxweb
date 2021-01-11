<template>
  <div class="home">
    <h1>Главная</h1>
    <p>Главная страница пустая</p>
  </div>
</template>

<script>
  export default {
    middleware: 'auth',
  }
</script>

<style lang="scss">
  .home {
    p {
      margin-top: 2rem;
      color: $gray;
      font-weight: 500;
    }
  }
</style>
