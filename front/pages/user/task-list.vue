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

      <div class="task-list__content-list" v-for="(item, idx) in items" :key="'task-list__content-list'+idx">
        <div class="task-list__content-task">
          <p>{{item.name}}</p>
        </div>
        <div class="task-list__content-status">
          <InputCheckbox text="Выполнено"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "task-list",
    data() {
      return {
        items: [
          {
            name: 'Текст задачи',
            performed: false
          },
          {
            name: 'laboriosam mollitia et enim quasi adipisci quia provident illum',
            performed: false
          }
        ]
      }
    }
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
