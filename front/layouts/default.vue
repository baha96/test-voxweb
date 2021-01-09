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
      padding: 1rem;
    }
    @media only screen and (min-width: 992px) {
      flex-direction: unset;
      justify-content: space-between;
      .content {
        padding: 4rem 2rem 1rem;
        width: calc(100% - #{$navigationW});
      }
    }
  }
</style>
