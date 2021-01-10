<template>
  <nav class="navigation" :class="{show, hide}">
    <div class="navigation-head">
      <Hamburger @click.native="show = !show" :open="show"/>
      <Logo :short="hide"/>
      <img class="navigation-head__button"
           src="@images/icon/button-left-green.svg"
           alt="button-left-green.svg"
           :style="{'transform': hide ? 'translateY(-50%) scaleX(-1)': ''}"
           @click="hide = !hide" >
    </div>
    <div class="navigation-body">
      <template v-for="(item, idx) in items">
        <NavigationItem :item="item"
                        :key="'navigation'+idx"
                        :class="{'show-text': !hide}"/>
      </template>
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
            url: '/user',
            img: 'work',
          },
          {
            name: 'Список задач',
            url: '/user/task-list',
            img: 'product',
          },
          {
            name: 'Статистика',
            url: '/user/statistics',
            img: 'statistics',
          },
        ],
        show: false,
        hide: false
      }
    },
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
      &__button {
        display: none;
        position: absolute;
        top: 50%;
        right: -30px;
        transform: translateY(-50%);
        width: 40px;
        height: 40px;
        border-radius: 50%;
        padding: 10px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.51);
        cursor: pointer;
      }
    }

    &-body {
      position: absolute;
      top: 73px;
      left: -100%;
      transition: $transition;
      padding: 1rem 1.5rem;
      width: 100%;
      height: calc(100vh - 73px);
      background: #fff;
      z-index: 666;
    }

    &.show {
      .navigation-body {
        left: 0;
      }
    }
    @media only screen and (min-width: 992px) {
      width: $navigationW;
      &-head {
        padding: 1rem 1.5rem;
        position: relative;
        .hamburger {
          display: none;
        }
        &__button {
          display: block;
        }
      }
      &-body {
        position: static;
      }
      &.hide {
        width: 70px;
      }
    }
  }
</style>
