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
    }
  }
</script>

<style scoped lang="scss">
  .btn {
    display: block;
    width: 100%;
    padding: 14px 8px;
    font-weight: 500;
    color: #fff;
    border-radius: $bradius;
    background: $site-color;
  }
</style>
