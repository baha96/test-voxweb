<template>
    <NLink to="/" class="logo" :class="{short: short}">
      <img src="@images/logo-short.svg" alt="logo-short.svg"/>
      <img src="@images/logo.svg" alt="logo.svg"/>
    </NLink>
</template>

<script>
  export default {
    name: "Logo",
    props: {
      short: Boolean
    }
  }
</script>

<style scoped lang="scss">
  .logo {
    display: inline-block;
    width: 35%;
    height: 33px;
    img {
      width: 100%;
      height: 100%;
      &[alt="logo-short.svg"] {
        display: none;
      }
    }
    @media only screen and (min-width: 500px) {
      width: 140px;
      height: 35px;
    }
    @media only screen and (min-width: 992px) {
      width: 130px;
      min-width: 25px;
      height: 33px;
      &.short img {
        display: none;
        &[alt="logo-short.svg"] {
          display: block;
        }
      }
    }
  }
</style>
