<template>
    <div class="hamburger" :class="{active: open}">
      <span></span>
      <span></span>
    </div>
</template>

<script>
  export default {
    name: "Hamburger",
    props: {
      open: {
        required: true,
        type: Boolean
      }
    }
  }
</script>

<style scoped lang="scss">
  .hamburger {
    width: 30px;
    height: 25px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    span {
      width: 100%;
      height: 3px;
      background: $site-color;
      display: block;
      transition: $transition;
      //transform-origin: 4px 0px;
      &:first-child {
        margin-bottom: 8px;
      }
    }
    &.active {
      span:first-child {
        transform: rotate(39deg) translate(3px, 4px);
      }
      span:last-child {
        transform: rotate(-37deg) translate(3px, -5px);
      }
    }
  }
</style>
