<template>
  <div class="input">
    <label v-if="text" :for="inputID">{{ text }}</label>
    <input :type="type"
           :id="inputID"
           :required="required"
           :disabled="disabled"
           v-model.trim="value"/>
    <span></span>
    <small v-if="required">Пожалуйста заполните поле</small>
  </div>
</template>

<script>
  export default {
    name: "Input",
    props: {
      model: {
        type: String,
        required: true
      },
      modelName: {
        type: String,
        required: true
      },
      text: {
        type: String,
        default: ''
      },
      type: {
        type: String,
        default: 'text'
      },
      required: {
        type: Boolean,
        default: false
      },
      disabled: {
        type: Boolean,
        default: false
      }
    },
    data() {
      return {
        inputID: null,
      }
    },
    mounted() {
      this.inputID = `input${this._uid}`
    },
    computed: {
      value: {
        get: function () {
          return this.model
        },
        set: function (val) {
          this.$emit('get', {name: this.modelName , value: val} )
        }
      }
    },
  }
</script>

<style scoped lang="scss">
  .input {
    label {
      display: block;
      color: #6F849C;
      font-size: 90%;
    }
    input {
      display: block;
      width: 100%;
      border: 0;
      padding: 8px 0;
    }
    span {
      width: 100%;
      background: $light-blue;
      height: 2px;
      display: block;
    }
    small {
      color: $site-color;
      font-size: 80%;
    }
  }
</style>
