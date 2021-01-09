<template>
  <div class="wrapper">
    <Header />
    <Nuxt class="content"/>
  </div>
</template>

<style lang="scss">
  .wrapper {
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
    min-height: 100vh;
    min-width: 320px;
    .content {
      flex-grow: 1;
    }
  }
</style>
