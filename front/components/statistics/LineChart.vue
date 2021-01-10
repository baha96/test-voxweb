<script>
  import { Line, mixins } from "vue-chartjs";
  const { reactiveProp } = mixins;
  export default {
    extends: Line,
    name: "LineChart",
    mixins: [reactiveProp],
    props: {
      options: Object,
      chartData: {
        type: Object,
        required: true
      },
    },
    mounted() {
      this.renderChartDatas()
    },
    methods: {
      renderChartDatas() {
        this.renderChart(
          this.chartData,
          this.options);
      },
      updateChart() {
        this.$data._chart.update()
      }
    }
  }
</script>

<style scoped>

</style>
