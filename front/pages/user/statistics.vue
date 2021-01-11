<template>
  <div class="statistics">
    <h1>Статистика</h1>
    <div class="statistics-content">
      <LineChart :chartData="chartData" ref="chart" :options="options"/>

      <div class="statistics-content__buttons">
        <Button text="Случайные данные" class="gray" @click.native="setRandomDatas()"/>
        <Button text="Добавить данные" class="gray" @click.native="addRandomData()"/>
        <Button text="Удалить данные" class="gray" @click.native="delAllData()"/>
        <Button text="Увеличить кол-во данных" class="gray" @click.native="enlargeData()"/>
        <Button text="Уменьшить кол-во данных" class="gray" @click.native="reduceData()"/>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "statistics",
    middleware: 'auth',
    data() {
      return {
        months: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        labels: [],
        limit: 3,
        datasets: [],
        options: {
          responsive: true,
          maintainAspectRatio: false,
        }
      }
    },
    created() {
      this.labels = this.months.slice(0, this.limit);
    },
    mounted() {
      this.setRandomDatas()
    },
    computed: {
      chartData() {
        return {
          labels: this.labels,
          datasets: this.datasets
        }
      }
    },
    methods: {
      templateData() {
        const color = '#'+(Math.random()* (50 - 12 + 190)).toString(16).slice(-6);
        return {
          label: 'Названия',
          data: [this.getRandomInt()],
          backgroundColor: "transparent",
          borderColor: color,
          pointBackgroundColor: color
        }
      },
      getRandomInt() {
        return Math.floor(Math.random() * (50 - 5 + 1)) + 5
      },
      setDatas() {
        return Array.from({length: this.labels.length}, () => this.getRandomInt())
      },
      setRandomDatas() {
        const limit = this.datasets.length > 0 ? this.datasets.length : this.limit;
        this.datasets = Array.from({length: limit}, () => ({
          ...this.templateData(),
          data: this.setDatas(),
        }));
        this.$refs.chart.updateChart()
      },
      addRandomData() {
        this.datasets = [...this.datasets, {
          ...this.templateData(),
          data: this.setDatas()
        }]
      },
      delAllData() {
        if (this.datasets.length) {
          this.datasets.splice(-1,1);
        }
      },
      enlargeData() {
        if (this.limit < 12) {
          this.limit++;
          this.labels.push(this.months[this.limit-1]);
          if (this.datasets.length) {
            this.datasets.forEach(i => {
              i.data.push(this.getRandomInt())
            });
          }
        }
      },
      reduceData() {
        if (this.limit > 0) {
          this.limit--;
          this.labels.splice(-1,1);
          if (this.datasets.length) {
            this.datasets.forEach(i => {
              i.data.splice(-1,1);
            });
          }
        }
      }
    },
  }
</script>

<style scoped lang="scss">
  .statistics {
    &-content {
      padding: 1rem;

      &__buttons button {
        margin-top: 1rem;
        font-size: 14px;
      }
    }
    @media only screen and (min-width: 1200px) {
      &-content {
        &__buttons button {
          margin-right: 1rem;
          font-size: 16px;
        }
      }
    }
  }
</style>
<style lang="scss">
  canvas {
    width: 100% !important;
    max-height: 500px;
    @media only screen and (min-width: 1200px) {
      max-width: 1050px;
    }

  }
</style>
