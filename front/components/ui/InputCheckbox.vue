<template>
    <div class="input-checkbox">
      <input type="checkbox"
             :id="inputID"
             :name="inputID"
             v-model.trim="value"/>
      <label :for="inputID">{{ text }}</label>
    </div>
</template>

<script>
  export default {
    name: "InputCheckbox",
    data() {
      return {
        inputID: null,
      }
    },
    mounted() {
      this.inputID = `input-checkbox${this._uid}`
    },
    props: {
      text: {
        type: String,
        required:true
      },
      model: {
        type: Boolean,
        required: true
      },
      modelName: {
        type: String,
        required: true
      },
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
  .input-checkbox {
    input {
      display: none;
    }
    label {
      display: flex;
      align-items: center;
      font-weight: 500;
      color: #C2C2C2;
    }
    input + label:before {
      content: '';
      color: transparent;
      border: 1px solid #ccc;
      font-size: 20px;
      font-weight: 900;
      line-height: 22px;
      margin-right: 7px;
      height: 20px;
      width: 20px;
      min-width: 20px;
      transition: color ease .3s;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }
    input:checked + label {
      color: $green;
      &:before {
        content: url('~assets/images/icon/mark.svg');
      }
    }
  }

</style>
