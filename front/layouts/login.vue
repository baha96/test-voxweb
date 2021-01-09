<template>
  <div class="wrapper">
    <Nuxt class="content"/>
  </div>
</template>

<script>
  export default {
    name: "login"
  }
</script>

<style lang="scss">
  .wrapper {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    min-height: 100vh;
    .content {
      flex-grow: 1;
    }
  }
</style>
