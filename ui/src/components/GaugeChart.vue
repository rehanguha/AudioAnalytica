<template>
  <div class='gauge-container'>
    <RateOfSpeech :selectedFile="selectedFile"></RateOfSpeech>
    <ArticulationRate :selectedFile="selectedFile"></ArticulationRate>
  </div>
</template>

<script>
import ArticulationRate from './ArticulationRate' 
import RateOfSpeech from './RateOfSpeech'
export default {
  name: "GaugeChart",
  props: ["selectedFile"],
  components: {
    ArticulationRate,
    RateOfSpeech
  }

};
</script>

<style>
.gauge-container{
  display: grid;
  grid-template-columns: 50% 50%;
}
</style>
