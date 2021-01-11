<template>
    <div class="profile">
      <h1>Мой профиль</h1>
      <form class="profile-content" @submit.prevent="changeData()">
        <div class="profile-content__inputs" v-if="item">
          <Input text="Имя" :model="item.first_name" @get="getChangedValue" modelName="first_name" required/>
          <Input text="Фамилия" :model="item.last_name" @get="getChangedValue" modelName="last_name" required/>
          <Input text="Сменить пароль" :model="item.password" @get="getChangedValue" modelName="password"/>
          <Input text="Сменить логин" :model="item.username" @get="getChangedValue" modelName="username" :disabled="true"/>
        </div>
        <p v-if="success" class="success">Данные изменены!</p>
        <Button text="Сохранить" type="submit"/>
      </form>
    </div>
</template>

<script>

  import {mapActions} from "vuex";
  import Cookies from 'js-cookie'

  export default {
    name: "index",
    middleware: 'auth',
    data() {
      return {
        item: {
          first_name: this.$store.getters['users/user'].first_name,
          last_name: this.$store.getters['users/user'].last_name,
          username: this.$store.getters['users/user'].username,
          password: ''
        },
        disabled: false,
        success: false
      }
    },
    methods: {
      ...mapActions({
        getUser: 'users/getUser',
      }),
      getChangedValue(val) {
        this.item[val.name] = val.value
      },
      async changeData() {
        try {
          this.disabled = true;
          this.success = false;
          this.error = [];
          await this.$axios.$put(`/api/v1/account/${this.$store.getters['users/user'].id}/change-data/`, this.item);
          await this.getUser();
          this.success = true;
          if (this.item.password) {
            Cookies.remove('sessionid');
            Cookies.remove('csrftoken');
            document.location.href = '/user/login'
          }
        } catch (e) {
          console.error(e);
        } finally {
          this.disabled = false
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
      .success {
        color: $green;
        font-weight: 500;
        margin-bottom: 1rem;
      }
      .btn {
        display: block;
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
        .success {
          text-align: right;
        }
        .btn {
          width: 27%;
          margin-left: auto;
        }
      }
    }
  }
</style>
