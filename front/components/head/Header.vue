<template>
  <nav class="navigation" :class="{show}">
    <div class="navigation-head">
      <Hamburger @click.native="show = !show" :open="show"/>
      <Logo/>
    </div>
    <div class="navigation-body">
      <NLink v-for="(item, idx) in items" :key="'navigation'+idx" :to="item.url">
        <img :src="require(`@images/icon/${item.img}.svg`)" :alt="item.name">
        <span>{{ item.name }}</span>
      </NLink>
    </div>
  </nav>
</template>

<script>
  export default {
    name: "Header",
    data() {
      return {
        items: [
          {
            name: 'Мой профиль',
            url: '/',
            img: 'work',
          },
          {
            name: 'Список задач',
            url: '/',
            img: 'product',
          },
          {
            name: 'Статистика',
            url: '/',
            img: 'statistics',
          },
        ],
        show: false
      }
    }
  }
</script>

<style scoped lang="scss">
  .navigation {
    position: relative;

    &-head {
      display: flex;
      align-items: center;
      padding: 1.5rem;

      .hamburger {
        margin-right: 2rem;
      }
    }

    &-body {
      position: absolute;
      top: 70px;
      left: -100%;
      transition: $transition;
      padding: 1rem 1.5rem;
      width: 100%;

      a {
        display: block;
        margin-bottom: 1rem;
        font-weight: 500;

        img {
          margin-right: 10px;
          width: 25px;
          height: 25px;
        }

        &:last-child {
          margin-bottom: 0;
        }
      }
    }

    &.show {
      .navigation-body {
        left: 0;
      }
    }
  }
</style>
