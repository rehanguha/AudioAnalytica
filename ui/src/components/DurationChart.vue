<template>
  <div>
    <h2>Audio Statistics</h2>
    <p>some discription</p>
    <highcharts :options="chartOptions"></highcharts>
  </div>
</template>

<script>
import Highcharts from "highcharts";
import highcharts from "highcharts-vue";
import More from "highcharts/highcharts-more";
import axios from "axios";
More(Highcharts);
export default {
  props: ["selectedFile"],
  mounted() {
    axios
      .get(
        "http://localhost:5001/quantileanalysis?filename=" + this.selectedFile
      )
      .then(response => {
        let data = JSON.parse(response["data"])[0];
        this.chartOptions.series = [
          {
            name: "Speaking Duration",
            data: [parseFloat(data["speaking_duration"])]
          },
          {
            name: "Original Duration",
            data: [parseFloat(data["original_duration"])]
          },
          { name: "Balance", data: [parseFloat(data["balance"])] }
        ];
      })
      .catch(error => {});
  },
  data() {
    return {
      chartOptions: {
        chart: {
          type: "bar"
        },
        title: {
          text: ""
        },
        xAxis: {
          categories: [""]
        },
        yAxis: {
          min: 0,
          title: {
            text: "Count"
          },
          stackLabels: {
            enabled: true,
            style: {
              fontWeight: "bold",
              color:
                // theme
                (Highcharts.defaultOptions.title.style &&
                  Highcharts.defaultOptions.title.style.color) ||
                "gray"
            }
          }
        },
        legend: {
          reversed: true
        },
        plotOptions: {
          series: {
            stacking: "normal"
          }
        },
        series: []
      }
    };
  }
};
</script>

<style></style>
