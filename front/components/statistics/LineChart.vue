<script>
  import { Line } from "vue-chartjs";
  export default {
    extends: Line,
    name: "LineChart",
    props: {
      options: Object,
      datasets: {
        type: Array,
        required: true
      },
      labels: {
        type: Array,
        required: true
      }
    },
    watch: {
      'datasets'() {
        this.renderChartDatas()
      }
    },
    mounted() {
      this.renderChartDatas()
    },
    methods: {
      renderChartDatas() {
        this.renderChart(
          {
            labels: this.labels,
            datasets: this.datasets
          },
          this.options
        );
      },
      updateChartDatas() {
        this.$data._chart.update()
      },
    }
  }
</script>

<style scoped>

</style>
