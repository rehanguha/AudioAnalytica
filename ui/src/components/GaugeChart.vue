<template>
<div>
    <RateOfSpeech :selectedFile="selectedFile"></RateOfSpeech>
    <div class='gauge-container'>
      <ArticulationRate :selectedFile="selectedFile"></ArticulationRate>
      <PronunciationPosteriorScore :selectedFile="selectedFile"></PronunciationPosteriorScore>
    </div>


</div>
  
</template>

<script>
import ArticulationRate from './ArticulationRate' 
import RateOfSpeech from './RateOfSpeech'
import PronunciationPosteriorScore from './PronunciationPosteriorScore'

export default {
  name: "GaugeChart",
  props: ["selectedFile"],
  components: {
    ArticulationRate,
    RateOfSpeech,
    PronunciationPosteriorScore
  }

};
</script>

<style>
.gauge-container{
  display: grid;
  grid-template-columns: 50% 50%;
}
.gauge-chart > h2 {
  margin: 0px !important;
}
</style>
