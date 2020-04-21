<template>
  <div>
    <h2>Waveplot</h2>
    <p>Some Description</p>
    <img v-bind:src="wave_image">
    <h2>Spec</h2>
    <p>Some Description</p>
    <img :src="spec_image">
    <h2>Analysis</h2>
    <p>Some Description</p>
    <img :src="analyze_image">
  </div>

</template>

<script>

import axios from 'axios';

export default {
  props: ["selectedFile"],
  data(){
    return {
      wave_image: "",
      spec_image: "",
      analyze_image: ""
    }
  },
  mounted(){
    this.get_waveform_images();
  },
  methods: {
    get_waveform_images(){
      axios
        .get("http://localhost:5001/wave_image?filename=" + this.selectedFile, { responseType: "blob" })
        .then(response => {
          this.wave_image = URL.createObjectURL(response.data);
        })
        .catch(error => {});      
      axios
        .get("http://localhost:5001/spec_image?filename=" + this.selectedFile, { responseType: "blob" })
        .then(response => {
          this.spec_image = URL.createObjectURL(response.data);
        })
        .catch(error => {});      
      axios
        .get("http://localhost:5001/analyze_image?filename=" + this.selectedFile, { responseType: "blob" })
        .then(response => {
          this.analyze_image = URL.createObjectURL(response.data);
        })
        .catch(error => {});      

    }
  }
}
</script>

<style>
 img {
   width: 80%;
 }
</style>