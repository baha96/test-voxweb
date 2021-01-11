<template>
  <div class="login">
    <Logo/>
    <form @submit.prevent="login()" v-if="item">
      <input type="text" v-model.trim="item.username" placeholder="Логин" required>
      <input type="password" v-model.trim="item.password" placeholder="Пароль" required>
      <NLink to="/user/register">Зарегистрироваться</NLink>
      <p v-if="error.length" class="error" v-for="e in error">* {{ e }}</p>
      <div class="footer">
        <Button text="Войти" type="submit" :disabled="disabled"/>
        <Loading v-show="disabled" class="small"/>
      </div>
    </form>
  </div>
</template>

<script>

  import {mapMutations} from "vuex";

  export default {
    name: "login",
    layout: 'login',
    data() {
      return {
        disabled: false,
        error: [],
        item: {
          username: '',
          password: ''
        }
      }
    },
    methods: {
      ...mapMutations({
        setUser: 'users/SET_USER'
      }),
      async login() {
        try {
          this.disabled = true;
          this.error = [];
          const user = await this.$axios.$post('api/v1/account/auth/', this.item);
          this.setUser(user);
          this.$router.replace(this.$route.query.redirect || "/");
        } catch (e) {
          console.error(e);
          const {data} = e.response;
          if (data && data.warning) this.error.push(data.warning);
        } finally {
          this.disabled = false
        }
      }
    }
  }
</script>

<style scoped lang="scss">
  .login {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    max-width: 90%;
    margin: 0 auto;
    width: 100%;

    @include loginInput;

    .logo  {
      margin-bottom: 3rem;
      width: 70%;
    }
    form  a {
      text-align: right;
      font-weight: 500;
      font-size: 80%;
      color: $blue;
      display: block;
      margin-bottom: 1rem;
    }
    @media only screen and (min-width: 411px) {
      max-width: 80%;
    }
    @media only screen and (min-width: 767px) {
      max-width: 50%;
    }
    @media only screen and (min-width: 1200px) {
      max-width: 380px;
      .logo  {
        width: 50%;
      }
    }
  }
</style>
