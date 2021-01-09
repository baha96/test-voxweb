<template>
    <NLink to="/" class="logo">
      <img src="@images/logo.svg" alt="logo.svg"/>
    </NLink>
</template>

<script>
  export default {
    name: "Logo"
  }
</script>

<style scoped lang="scss">
  .logo {
    display: inline-block;
    width: 35%;
    img {
      width: 100%;
    }
  }
</style>
