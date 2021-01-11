<template>
    <div class="button-exit" @click="logout()">
      <img src="@images/icon/logout.svg" alt="logout.svg">
      <span>Выйти</span>
    </div>
</template>

<script>

  import Cookies from 'js-cookie'

  export default {
    name: "ButtonExit",
    methods: {
      async logout() {
          try {
            await this.$axios.$post('/api/v1/account/logout/');
            Cookies.remove('sessionid');
            Cookies.remove('csrftoken');
            document.location.href = '/user/login'
          } catch (e) {
            console.error(e)
          }
      }
    }
  }
</script>

<style scoped lang="scss">
  .button-exit {
    color: #6F849C;
    font-weight: 500;
    display: flex;
    align-items: center;
    margin-top: auto;
    cursor: pointer;
    img {
      margin-right: 10px;
      $width: 25px;
      width: $width;
      height: $width;
      min-width: $width;
      min-height: $width;
    }
    @media only screen and (min-width: 992px) {
      span {
        display: none;
      }
      &.show-text span {
        display: inline-block;
      }
    }
  }
</style>
