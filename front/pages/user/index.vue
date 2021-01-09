<template>
    <div class="profile">
      <h1>Мой профиль</h1>
      <form class="profile-content">
        <div class="profile-content__inputs">
          <Input text="Имя" :model="form.name" modelName="name"/>
          <Input text="Фамилия" :model="form.surName" modelName="surName" required/>
          <Input text="Сменить пароль" :model="form.password" modelName="password"/>
          <Input text="Сменить логин" :model="form.login" modelName="login" required/>
        </div>
        <Button text="Сохранить" type="submit"/>
      </form>
    </div>
</template>

<script>
  export default {
    name: "index",
    data() {
      return {
        form: {
          name: '',
          surName: '',
          password: '',
          login: '',
        }
      }
    }
  }
</script>

<style scoped lang="scss">
  .profile {
    h1 {
      margin-bottom: 2rem;
    }
    &-content {
      padding: 1rem;
      &__inputs {
        .input {
          margin-bottom: 2rem;
        }
      }
    }
    @media only screen and (min-width: 992px) {
      &-content {
        padding: 3rem;
        &__inputs {
          display: flex;
          justify-content: space-between;
          flex-wrap: wrap;
          .input {
            width: 49%;
          }
        }
        .btn {
          width: 27%;
          margin-left: auto;
        }
      }
    }
  }
</style>
