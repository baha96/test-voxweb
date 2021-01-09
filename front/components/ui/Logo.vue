<template>
    <NLink to="/" class="logo">
      <img v-show="short" src="@images/logo-short.svg" alt="logo-short.svg"/>
      <img v-show="!short" src="@images/logo.svg" alt="logo.svg"/>
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
    img {
      width: 100%;
      height: 100%;
    }
    @media only screen and (min-width: 500px) {
      width: 140px;
    }
    @media only screen and (min-width: 992px) {
      width: 130px;
      min-width: 25px;
      height: 33px;
    }
  }
</style>
