<template>
  <div class="loading">
    <div class="lds-spinner">
      <div v-for="item in 12" :key="'lds-spinner-' + item"></div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Loading"
  }
</script>

<style scoped lang="scss">
  $width: 32px;
  $origin: 15px;
  .loading {
    width: 100%;
    &.small {
      width: auto;
      .lds-spinner {
        margin: 0;
        width: $width;
        height: $width;
        div {
          transform-origin: $origin $origin;
          &:after {
            top: 2px;
            left: 15px;
            width: 3px;
            height: 8px;
          }
        }
      }
    }
    &.very {
      .lds-spinner {
        width: 22px;
        height: 22px;
        div {
          transform-origin: 12px 12px;
          &::after {
            left: 10px;
            width: 2px;
            height: 6px;
          }
        }
      }
    }
  }
  .lds-spinner {
    display: block;
    position: relative;
    width: $width * 2;
    height: $width * 2;
    margin: 1rem auto;
    div {
      /*transform-origin: 32px 32px;*/
      transform-origin: $origin*2+2 $origin*2+2;
      animation: lds-spinner 1.2s linear infinite;
      &:after {
        content: " ";
        display: block;
        position: absolute;
        top: 3px;
        left: 29px;
        width: 5px;
        height: 14px;
        border-radius: 20%;
        background: #405BBA;
      }
      &:nth-child(1) {
        transform: rotate(0deg);
        animation-delay: -1.1s;
      }
      &:nth-child(2) {
        transform: rotate(30deg);
        animation-delay: -1s;
      }
      &:nth-child(3) {
        transform: rotate(60deg);
        animation-delay: -0.9s;
      }
      &:nth-child(4) {
        transform: rotate(90deg);
        animation-delay: -0.8s;
      }
      &:nth-child(5) {
        transform: rotate(120deg);
        animation-delay: -0.7s;
      }
      &:nth-child(6) {
        transform: rotate(150deg);
        animation-delay: -0.6s;
      }
      &:nth-child(7) {
        transform: rotate(180deg);
        animation-delay: -0.5s;
      }
      &:nth-child(8) {
        transform: rotate(210deg);
        animation-delay: -0.4s;
      }
      &:nth-child(9) {
        transform: rotate(240deg);
        animation-delay: -0.3s;
      }
      &:nth-child(10) {
        transform: rotate(270deg);
        animation-delay: -0.2s;
      }
      &:nth-child(11) {
        transform: rotate(300deg);
        animation-delay: -0.1s;
      }
      &:nth-child(12) {
        transform: rotate(330deg);
        animation-delay: 0s;
      }
    }
  }
  @keyframes lds-spinner {
    0% {
      opacity: 1;
    }
    100% {
      opacity: 0;
    }
  }
</style>
