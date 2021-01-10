<template>
    <button :type="type" class="btn">
      {{ text }}
    </button>
</template>

<script>
  export default {
    name: "Button",
    props: {
      text: {
        type: String,
        required: true
      },
      type: {
        type: String,
        default: () => 'button',
      },
    },
  }
</script>

<style scoped lang="scss">
  .btn {
    display: inline-block;
    width: 100%;
    padding: 14px 10px;
    font-weight: 500;
    color: #fff;
    border-radius: $bradius;
    background: $site-color;
    &.gray {
      width: auto;
      border: $border-gray;
      color: $gray;
      background: transparent;
      padding: 8px 12px;
      &:hover {
        color: $site-color;
        border-color: $site-color;
      }
    }
  }
</style>
