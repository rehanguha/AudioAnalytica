<template>
  <div class='gauge-container'>
    <RateOfSpeech :selectedFile="selectedFile"></RateOfSpeech>
    <ArticulationRate :selectedFile="selectedFile"></ArticulationRate>
    <PronunciationPosteriorScore :selectedFile="selectedFile"></PronunciationPosteriorScore>
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
  grid-template-columns: 33% 34% 33%;
}
</style>
