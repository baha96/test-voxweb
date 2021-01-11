<template>
    <div class="register">
      <Logo/>
      <form @submit.prevent="register()" v-if="item">
        <input type="text" v-model.trim="item.first_name" placeholder="Имя" required>
        <input type="text" v-model.trim="item.last_name" placeholder="Фамилия" required>
        <input type="text" v-model.trim="item.username" placeholder="Логин" required>
        <input type="password" v-model.trim="item.password" placeholder="Пароль" required>
        <input type="password" v-model.trim="item.password2" placeholder="Повторите пароль" required>
        <p v-if="error.length" class="error" v-for="e in error">* {{ e }}</p>
        <div class="footer">
          <Button text="Создать" type="submit" :disabled="disabled"/>
          <Loading v-show="disabled" class="small"/>
        </div>
      </form>
    </div>
</template>

<script>
  export default {
    name: "register",
    layout: 'login',
    data() {
      return {
        disabled: false,
        item: {
          first_name: '',
          last_name: '',
          username: '',
          password: '',
          password2: '',
        },
        error: []
      }
    },
    methods: {
      async register() {
        try {
          this.disabled = true;
          this.error = [];
          await this.$axios.$post('account/register/', this.item);
          this.$router.push({name: 'user-login'})
        } catch (e) {
          console.error(e);
          const {data} = e.response;
            if (data && data.warning) this.error = data.warning;
            else if (data && data.non_field_errors) this.error = data.non_field_errors;

        } finally {
          this.disabled = false
        }
      }
    }
  }
</script>

<style scoped lang="scss">
  .register {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    max-width: 90%;
    margin: 0 auto;
    width: 100%;
    .logo  {
      margin-bottom: 3rem;
      width: 70%;
    }
    form {
      width: 100%;
      input {
        display: block;
        border: $border-gray;
        width: 100%;
        padding: 14px 16px;
        font-size: 16px;
        line-height: 20px;
        border-radius: $bradius;
        margin-bottom: 1rem;
        &::placeholder {
          color: #9496A6;
          font-size: 18px;
        }
      }
    }

    .footer {
      display: flex;
      align-items: center;
      .btn {
        margin-right: 10px;
      }
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
