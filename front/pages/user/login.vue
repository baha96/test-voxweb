<template>
  <div class="login">
    <Logo/>
    <form>
      <input type="text" placeholder="Логин" required>
      <input type="text" placeholder="Пароль" required>
      <Button text="Войти" type="submit"/>
    </form>
  </div>
</template>

<script>
  export default {
    name: "login",
    layout: 'login'
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
