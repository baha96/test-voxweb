<template>
  <NLink class="navigation-item" v-if="item" :to="item.url">
    <img :src="require(`@images/icon/${changeImg(active)}.svg`)" :alt="item.name">
    <span>{{ item.name }}</span>
  </NLink>
</template>

<script>
  export default {
    name: "NavigationItem",
    props: {
      item: Object,
    },
    methods: {
      changeImg(status) {
        return status ? this.item.img + 'Red' : this.item.img
      }
    },
    computed: {
      active() {
        return this.$route.path === this.item.url
      }
    }
  }
</script>

<style scoped lang="scss">
  .navigation-item {
    display: block;
    margin-bottom: 1rem;
    font-weight: 500;

    img {
      margin-right: 10px;
      $width: 25px;
      width: $width;
      height: $width;
      min-width: $width;
      min-height: $width;
    }

    &:last-child {
      margin-bottom: 0;
    }
    @media only screen and (min-width: 992px) {
      margin-bottom: 2rem;
      span {
        display: none;
      }
      &.show-text span {
        display: inline-block;
      }
    }
  }
</style>
