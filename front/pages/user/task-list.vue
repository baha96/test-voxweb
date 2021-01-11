<template>
  <div class="task-list">
    <h1>Список задач</h1>
    <div class="task-list__content">

      <div class="task-list__content-list">
        <div class="task-list__content-task">
          <h3>Задача</h3>
        </div>
        <div class="task-list__content-status">
          <h3>Статус</h3>
        </div>
      </div>

      <Loading v-if="items.length === 0 && loading"/>

      <div class="task-list__content-list" v-for="item in items" :key="'task-list__content-list'+item.id">
        <div class="task-list__content-task">
          <p>{{item.title}}</p>
        </div>
        <div class="task-list__content-status">
          <InputCheckbox text="Выполнено" :model="item.completed" modelName="completed"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

  let loading = false;

  export default {
    name: "task-list",
    middleware: 'auth',
    async asyncData({$axios}) {
      try {
        loading = true;
        const response = await $axios.$get('/api/v1/task/');
        return {
          items: response
        }
      } catch (e) {
        return {
          items: []
        }
      } finally {
        loading = false;
      }
    },
    data() {
      return {
        loading: loading,
      }
    },
  }
</script>

<style scoped lang="scss">
  .task-list {
    &__content {
      margin-top: 2rem;
      padding: 1rem;
      h3 {
        font-weight: 500;
        line-height: 114%;
        color: #BABABA;
        margin-bottom: .5rem;
      }

      &-list {
        display: flex;
        justify-content: space-between;
        margin-bottom: 1rem;
      }
      &-task {
        width: 52%;
        font-weight: 500;
      }
      &-status {
        width: 45%;
      }
      @media only screen and (min-width: 415px) {
        &-task {
          width: 60%;
        }
        &-status {
          width: 37%;
        }
      }
      @media only screen and (min-width: 767px) {
        &-task {
          width: 78%;
        }
        &-status {
          width: 20%;
        }
      }
    }
  }
</style>
