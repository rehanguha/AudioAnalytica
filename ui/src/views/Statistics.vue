



<template>
  <div>
    <BoxChart :selectedFile="selected_file"></BoxChart>
    <RadialChart :selectedFile="selected_file"></RadialChart>
    <GaugeChart :selectedFile="selected_file"></GaugeChart>
    <WordCloud :selectedFile="selected_file"></WordCloud>
    <Waveform :selectedFile="selected_file"></Waveform>
    <JsonCompare :selectedFile="selected_file"></JsonCompare>
  </div>
</template>

<script>
import BoxChart from "./../components/BoxChart";
import RadialChart from "./../components/RadialChart";
import GaugeChart from "./../components/GaugeChart";
import WordCloud from "./../components/WordCloud";
import Waveform from "./../components/Waveform";
import JsonCompare from "./../components/JsonCompare";

export default {
  name: "Body",
  props: ["selected", 'selected_file'],
  components: {
    BoxChart,
    RadialChart,
    GaugeChart,
    WordCloud,
    Waveform,
    JsonCompare
  },
  watch: {
    selected: {
      immediate: true,
      handler() {}
    }
  }
};
</script>

<style>
</style>